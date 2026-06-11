import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _approval import assert_matches_golden, serialize_convert_result
from convert import convert

GOLDEN_T_FR_01 = Path(__file__).parent / "golden" / "T-FR-01.approved.txt"
GOLDEN_T_FR_02 = Path(__file__).parent / "golden" / "T-FR-02.approved.txt"
GOLDEN_T_FR_02_YARD = Path(__file__).parent / "golden" / "T-FR-02-YARD.approved.txt"
GOLDEN_T_FR_03 = Path(__file__).parent / "golden" / "T-FR-03.approved.txt"
GOLDEN_T_FR_03_CUBIT = Path(__file__).parent / "golden" / "T-FR-03-CUBIT.approved.txt"
GOLDEN_T_FR_04 = Path(__file__).parent / "golden" / "T-FR-04.approved.txt"
GOLDEN_T_FR_04_FEET = Path(__file__).parent / "golden" / "T-FR-04-FEET.approved.txt"
GOLDEN_T_FR_05_FORMAT = Path(__file__).parent / "golden" / "T-FR-05-FORMAT.approved.txt"
GOLDEN_T_FR_05_NUMBER = Path(__file__).parent / "golden" / "T-FR-05-NUMBER.approved.txt"

# PRD §8 기본(B) — B4 기대값 (비율 3.28084 / 1.09361, README 반올림)
B4_EXPECTED = {
    "meter:2.5": ["2.5 meter = 8.2 feet", "2.5 meter = 2.7 yard"],
    "feet:8.2": ["8.2 feet = 2.5 meter", "8.2 feet = 2.7 yard"],
    "yard:2.7": ["2.7 yard = 2.5 meter", "2.7 yard = 8.2 feet"],
}


def test_fr_01_meter_2_5_returns_pass():
    """FR-01 / B1 / T-FR-01: 단위:값 파싱 → pass"""
    # Arrange
    input_str = "meter:2.5"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "pass"
    assert result["error"] is None
    assert result["lines"] == B4_EXPECTED["meter:2.5"]
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_01)


def test_fr_02_feet_8_2_returns_pass():
    """FR-02 / B2 / T-FR-02: feet 변환 → pass"""
    # Arrange
    input_str = "feet:8.2"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "pass"
    assert result["error"] is None
    assert result["lines"] == B4_EXPECTED["feet:8.2"]
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_02)


def test_fr_02_yard_2_7_returns_pass():
    """FR-02 / B2 / T-FR-02-YARD: yard 변환 → pass"""
    # Arrange
    input_str = "yard:2.7"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "pass"
    assert result["error"] is None
    assert result["lines"] == B4_EXPECTED["yard:2.7"]
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_02_YARD)


def test_fr_03_meters_2_5_returns_fail():
    """FR-03 / Q5: 미지원 단위 meters → fail / unit"""
    # Arrange
    input_str = "meters:2.5"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "fail"
    assert result["lines"] == []
    assert result["error"] == {
        "type": "unit",
        "message": "Unknown unit: meters",
    }
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_03)


def test_fr_03_cubit_1_returns_fail():
    """FR-03: 미지원 단위 cubit → fail / unit"""
    # Arrange
    input_str = "cubit:1"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "fail"
    assert result["lines"] == []
    assert result["error"] == {
        "type": "unit",
        "message": "Unknown unit: cubit",
    }
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_03_CUBIT)


def test_fr_04_meter_negative_1_returns_fail():
    """FR-04 / Q3: 음수 meter → fail / negative"""
    # Arrange
    input_str = "meter:-1"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "fail"
    assert result["lines"] == []
    assert result["error"] == {
        "type": "negative",
        "message": "Negative value not allowed: -1",
    }
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_04)


def test_fr_04_feet_negative_1_returns_fail():
    """FR-04 / Q3: 음수 feet → fail / negative"""
    # Arrange
    input_str = "feet:-1"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "fail"
    assert result["lines"] == []
    assert result["error"] == {
        "type": "negative",
        "message": "Negative value not allowed: -1",
    }
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_04_FEET)


def test_fr_05_format_returns_fail():
    """FR-05 / Q4: 콜론 형식 누락 → fail / format"""
    # Arrange
    input_str = "2.5 meter"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "fail"
    assert result["lines"] == []
    assert result["error"] == {
        "type": "format",
        "message": "Invalid format. Use unit:value (ex: meter:2.5)",
    }
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_05_FORMAT)


def test_fr_05_number_abc_returns_fail():
    """FR-05 / Q4: 숫자 변환 실패 → fail / number"""
    # Arrange
    input_str = "meter:abc"

    # Act
    result = convert(input_str)

    # Assert
    assert result["status"] == "fail"
    assert result["lines"] == []
    assert result["error"] == {
        "type": "number",
        "message": "Invalid number: abc",
    }
    assert_matches_golden(serialize_convert_result(result), GOLDEN_T_FR_05_NUMBER)
