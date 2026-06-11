import pytest

from convert import convert


def test_fr_01_meter_2_5_returns_pass():
    # Arrange
    input_str = "meter:2.5"

    # Act
    result = convert(input_str)

    # Assert
    pytest.fail("RED skeleton")
