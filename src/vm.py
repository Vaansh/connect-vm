import json
import os

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
    p = Popen(["osascript", "-"], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(script)

    # debug
    if script_flag:
        print(script)

    if err_flag:
        print(stdout, stderr)


def open_spotlight() -> None:
    with open(base + "open-spotlight.applescript", "r") as f:
        script = f.read()

    exec_applescript(script)


def open_rdp() -> None:
    with open(base + "open-rdp.applescript", "r") as f:
        script = f.read()

    exec_applescript(script)


def open_vm() -> None:
    open_spotlight()
    open_rdp()
