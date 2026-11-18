"""Password strength checker with common-password detection."""
import re
from pathlib import Path

COMMON_FILE = Path(__file__).resolve().parent.parent / "data" / "common.txt"


def load_common(path=COMMON_FILE):
    """Load common passwords into a set. Returns an empty set if the file is missing."""
    try:
        with open(path, encoding="utf-8") as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        return set()


def check_password(password, common=None):
    """Return (strength_label, list_of_tips)."""
    if common is None:
        common = load_common()

    if password.lower() in common:
        return "Very weak", ["This is a very common password. Pick something unique."]

    score = 0
    tips = []

    if len(password) >= 12:
        score += 1
    else:
        tips.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Mix uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("Add numbers.")

    if re.search(r"[^\w\s]", password):
        score += 1
    else:
        tips.append("Add special characters.")

    levels = {0: "Very weak", 1: "Weak", 2: "Fair", 3: "Good", 4: "Strong"}
    return levels[score], tips
