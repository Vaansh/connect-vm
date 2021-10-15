import os
import sys
import json

from typing import List
from subprocess import Popen, PIPE

base = "src/applescripts/"


def get_credentials(path: str) -> List[str]:
    file = open(path)
    data = json.load(file)
    company, username, password = data["company"], data["username"], data["password"]
    return [company, username, password]


def get_curr_files() -> None:
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print("Files in %r: %s" % (cwd, files))


def exec_applescript(script: str, script_flag: bool = False, err_flag: bool = False) -> None:
    try:
        p = Popen(["osascript", "-"], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        stdout, stderr = p.communicate(script)
    except:
        print("Error: Cannot execute AppleScript, check the script and try again")
        sys.exit()
    finally:
        print(script) if script_flag else None
        print(stdout, stderr) if err_flag else None


def generate_send_creds_applescript(
    path: str, to_replace: List[str], replace_with: List[str], script_flag: bool = False, err_flag: bool = False
) -> str:
    with open(base + path, "r") as f:
        script = f.read()

        try:
            for i in range(len(replace_with)):
                script = script.replace(to_replace[i], replace_with[i])
            exec_applescript(script, script_flag, err_flag)
        except:
            print("Error: Check the length of lists and try again")
            return None

        return script


def read_and_exec_applescript(path: str) -> None:
    with open(base + path, "r") as f:
        script = f.read()

    exec_applescript(script)


def open_spotlight() -> None:
    read_and_exec_applescript("open-spotlight.applescript")


def open_rdp() -> None:
    read_and_exec_applescript("open-rdp.applescript")


def send_creds() -> None:
    generate_send_creds_applescript(
        "send-creds.applescript", ["COMPANY", "USERNAME", "PASSWORD"], get_credentials("sample-secrets.json")
    )


def open_vm() -> None:
    open_spotlight()
    open_rdp()
    send_creds()
