import re
from pathlib import Path


def load_exclusion_rules(path):
    """
    Loads regex expressions from a file
    Each line represents a regex expression
    """

    if not path:
        return []

    path = Path(path)
    if not path.is_file():
        raise Exception("path either does not exist or is not file")

    with open(path, "r") as f:
        return [re.compile(line.strip()) for line in f if line.strip() != ""]
