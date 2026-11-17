from tools.password_checker import check_password
from tools.file_integrity import save_baseline, check_baseline
from tools.log_analyzer import analyze_log


def test_common_password_is_very_weak():
    level, _ = check_password("password", common={"password"})
    assert level == "Very weak"


def test_strong_password():
    level, tips = check_password("T7#kLp9!vQ2x", common=set())
    assert level == "Strong"
    assert tips == []


def test_weak_password_gives_tips():
    level, tips = check_password("abc", common=set())
    assert level in ("Very weak", "Weak")
    assert len(tips) > 0


def test_file_integrity_detects_change(tmp_path):
    f = tmp_path / "a.txt"
    f.write_text("hello")
    baseline = tmp_path / "baseline.json"
    save_baseline([f], baseline)
    assert check_baseline(baseline)[0][1] == "OK"
    f.write_text("hello!")
    assert check_baseline(baseline)[0][1] == "CHANGED"
    f.unlink()
    assert check_baseline(baseline)[0][1] == "MISSING"


def test_log_analyzer_flags_repeat_offender(tmp_path):
    log = tmp_path / "auth.log"
    line = "Failed password for root from 10.0.0.5 port 22 ssh2\n"
    log.write_text(line * 6 + "Failed password for bob from 10.0.0.9 port 22 ssh2\n")
    assert analyze_log(log) == [("10.0.0.5", 6)]
