# Python Security Toolkit

A beginner-friendly command-line toolkit of defensive security utilities, written in Python using only the standard library.

## Features

- **Password strength checker**: scores length and character variety, and rejects passwords found in a common-password list.
- **File integrity monitor**: stores SHA-256 hashes of chosen files and reports whether they are `OK`, `CHANGED`, or `MISSING`.
- **Log analyzer**: scans an SSH auth log and flags IP addresses with repeated failed logins.

## Project structure

```
python-security-toolkit/
├── main.py                  # command-line menu
├── tools/
│   ├── password_checker.py
│   ├── file_integrity.py
│   └── log_analyzer.py
├── data/
│   ├── common.txt           # sample common-password list
│   └── sample_auth.log      # fake log for demo purposes
├── tests/test_tools.py
└── requirements.txt
```

## Installation and usage

Requires Python 3.8+.

```bash
git clone https://github.com/dekthai11/python-security-toolkit.git
cd python-security-toolkit
python main.py
```

### Example

```
=== Python Security Toolkit ===
1. Check password strength
2. Save file integrity baseline
3. Verify file integrity
4. Analyze log for failed logins
0. Exit
Choose: 4
Log file path (Enter for sample log):
  Suspicious: 203.0.113.7 had 6 failed logins
```

*(Replace this with a real screenshot of your own run.)*

## Running the tests

```bash
pip install -r requirements.txt
python -m pytest
```

## What I learned

- Hashing with `hashlib` and why it detects tampering
- Parsing text with regular expressions
- Structuring a Python project into modules
- Writing unit tests with `pytest`

## Future improvements

- Command-line arguments with `argparse`
- Check passwords against the Have I Been Pwned API
- Email or desktop alerts for suspicious logs
- Simple file encryption tool using `cryptography`

## Author

Apiwat Srisawang - Dublin, Ireland
LinkedIn: https://www.linkedin.com/in/apiwat-srisawang/

## Disclaimer

For educational and defensive use only. Sample data in this repo is fake.
