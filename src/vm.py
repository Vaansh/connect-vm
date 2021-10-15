import json
import os
from typing import List
from subprocess import Popen, PIPE


def get_credentials(path: str) -> List[str]:
    file = open(path)
    data = json.load(file)
    company, username, password = data["company"], data["username"], data["password"]
    return [company, username, password]


def get_curr_files() -> None:
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print("Files in %r: %s" % (cwd, files))


def exec_applescript(script) -> None:
    p = Popen(["osascript", "-"], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(script)
