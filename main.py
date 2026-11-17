"""Python Security Toolkit - simple command-line menu.

Run with:  python main.py
For educational and defensive use only.
"""
from pathlib import Path

from tools.password_checker import check_password
from tools.file_integrity import save_baseline, check_baseline
from tools.log_analyzer import analyze_log

DEFAULT_LOG = Path(__file__).resolve().parent / "data" / "sample_auth.log"


def password_menu():
    pw = input("Enter a password to test: ")
    level, tips = check_password(pw)
    print(f"\nStrength: {level}")
    for tip in tips:
        print(f"  - {tip}")


def baseline_menu():
    raw = input("File paths to protect (separate with commas): ")
    files = [p.strip() for p in raw.split(",") if p.strip()]
    if not files:
        print("No files entered.")
        return
    try:
        hashes = save_baseline(files)
        print(f"Saved baseline for {len(hashes)} file(s).")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")


def verify_menu():
    try:
        results = check_baseline()
    except FileNotFoundError:
        print("No baseline found. Choose option 2 first.")
        return
    for path, status in results:
        print(f"  {path}: {status}")


def log_menu():
    path = input(f"Log file path (Enter for sample log): ").strip() or DEFAULT_LOG
    try:
        suspicious = analyze_log(path)
    except FileNotFoundError:
        print("Log file not found.")
        return
    if not suspicious:
        print("No suspicious activity found.")
    for ip, n in suspicious:
        print(f"  Suspicious: {ip} had {n} failed logins")


def main():
    actions = {
        "1": password_menu,
        "2": baseline_menu,
        "3": verify_menu,
        "4": log_menu,
    }
    while True:
        print("\n=== Python Security Toolkit ===")
        print("1. Check password strength")
        print("2. Save file integrity baseline")
        print("3. Verify file integrity")
        print("4. Analyze log for failed logins")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
