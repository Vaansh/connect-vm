import json

from typing import List


def get_credentials(path: str) -> List[str]:
    file = open(path)
    data = json.load(file)
    company, username, password = data["company"], data["username"], data["password"]
    return [company, username, password]
