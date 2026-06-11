import sys
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
ROOT_DIR = TESTS_DIR.parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from _approval import assert_matches_golden
from UnitConverter import main

GOLDEN_T_UI_01 = Path(__file__).parent / "golden" / "T-UI-01.approved.txt"


def test_ui_01_main_meter_2_5_prints_pass_lines(monkeypatch, capsys):
    """T-UI-01 / FR-01 / B1: main() pass 시 convert lines를 stdout에 출력"""
    # Arrange
    monkeypatch.setattr("builtins.input", lambda _: "meter:2.5")

    # Act
    main()

    # Assert
    captured = capsys.readouterr()
    assert captured.err == ""
    assert_matches_golden(captured.out, GOLDEN_T_UI_01)
