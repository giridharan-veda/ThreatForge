#!/usr/bin/env python3
import sys, paramiko
def main():
    if len(sys.argv) < 4:
        print("Usage: ssh_exec.py <host> <user> <password> [command...]")
        sys.exit(1)
    host = sys.argv[1]
    user = sys.argv[2]
    password = sys.argv[3]
    command = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else "touch /tmp/pwned"
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, username=user, password=password, timeout=10)
        _, stdout, stderr = client.exec_command(command)
        out = stdout.read().decode() + stderr.read().decode()
        print(out)
        sys.exit(0)
    except Exception as e:
        print(f"SSH error: {e}")
        sys.exit(1)
    finally:
        client.close()
if __name__ == "__main__":
    main()
