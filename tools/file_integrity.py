"""File integrity monitor using SHA-256 hashes."""
import hashlib
import json
from pathlib import Path

BASELINE_FILE = Path(__file__).resolve().parent.parent / "baseline.json"


def sha256_file(path):
    """Return the SHA-256 hex digest of a file (read in chunks)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def save_baseline(files, baseline_path=BASELINE_FILE):
    """Hash each file and save the results. Returns the dict that was saved."""
    hashes = {str(Path(p)): sha256_file(p) for p in files}
    with open(baseline_path, "w", encoding="utf-8") as f:
        json.dump(hashes, f, indent=2)
    return hashes


def check_baseline(baseline_path=BASELINE_FILE):
    """Compare current hashes to the baseline. Returns list of (path, status)."""
    with open(baseline_path, encoding="utf-8") as f:
        saved = json.load(f)

    results = []
    for path, old_hash in saved.items():
        try:
            status = "OK" if sha256_file(path) == old_hash else "CHANGED"
        except FileNotFoundError:
            status = "MISSING"
        results.append((path, status))
    return results
