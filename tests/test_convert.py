import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _approval import assert_matches_golden, serialize_convert_result
from convert import convert

GOLDEN_T_FR_01 = Path(__file__).parent / "golden" / "T-FR-01.approved.txt"

# PRD §8 기본(B) — B4 기대값 (비율 3.28084 / 1.09361, README 반올림)
B4_EXPECTED = {
    "meter:2.5": ["2.5 meter = 8.2 feet", "2.5 meter = 2.7 yard"],
    "feet:8.2": ["8.2 feet = 2.5 meter", "8.2 feet = 2.7 yard"],
    "yard:2.7": ["2.7 yard = 2.5 meter", "2.7 yard = 8.2 feet"],
}


def test_b1_unit_value_to_other_units_pass():
    """B1: 단위:값 → 다른 단위 출력 (FR-01)"""
    # Arrange
    input_str = "meter:2.5"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "pass"
    assert result["error"] is None
    assert result["lines"] == B4_EXPECTED["meter:2.5"]
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_01)


def test_b2_feet_input_returns_pass():
    """B2: feet 단위 pass TC"""
    # Arrange
    input_str = "feet:8.2"

    # Act
    result = convert(input_str)

    # Assert
    # TODO: status=pass, lines == B4_EXPECTED["feet:8.2"]
    pytest.fail("RED skeleton: B2 — feet pass TC 미구현")


def test_b2_yard_input_returns_pass():
    """B2: yard 단위 pass TC"""
    # Arrange
    input_str = "yard:2.7"

    # Act
    result = convert(input_str)

    # Assert
    # TODO: status=pass, lines == B4_EXPECTED["yard:2.7"]
    pytest.fail("RED skeleton: B2 — yard pass TC 미구현")


def test_b3_extension_preserves_existing_meter_tc():
    """B3: 신규 단위 추가 후 기존 meter TC 무변경 (NFR-01)"""
    # Arrange
    input_str = "meter:2.5"

    # Act
    result = convert(input_str)

    # Assert
    # TODO: inch(또는 cubit) 등록 후에도 lines·status 동일
    pytest.fail("RED skeleton: B3 — 확장 시 기존 비침 회귀 TC 미구현")


def test_b4_conversion_accuracy_and_rounding():
    """B4: 변환 정확성 — 비율·반올림 기대값 명시"""
    # Arrange
    cases = B4_EXPECTED

    # Act & Assert
    for input_str, expected_lines in cases.items():
        result = convert(input_str)
        # TODO: result["status"] == "pass"
        # TODO: result["lines"] == expected_lines
        pytest.fail(f"RED skeleton: B4 — {input_str} 기대값 assert 미구현")
