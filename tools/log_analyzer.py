"""Log analyzer that flags IPs with repeated failed SSH logins."""
import re
from collections import Counter

FAILED_PATTERN = re.compile(r"Failed password .* from (\d{1,3}(?:\.\d{1,3}){3})")


def analyze_log(path, threshold=5):
    """Return a list of (ip, count) with at least `threshold` failed logins."""
    counts = Counter()
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = FAILED_PATTERN.search(line)
            if match:
                counts[match.group(1)] += 1
    return [(ip, n) for ip, n in counts.most_common() if n >= threshold]
