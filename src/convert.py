from constants import METER_TO_FEET, METER_TO_YARD, ROUND_DECIMALS


def convert(input_str):
    unit, value_str = input_str.split(":", 1)
    value = float(value_str)

    if unit == "meter":
        in_feet = round(value * METER_TO_FEET, ROUND_DECIMALS)
        in_yard = round(value * METER_TO_YARD, ROUND_DECIMALS)
        lines = [
            f"{value} {unit} = {in_feet} feet",
            f"{value} {unit} = {in_yard} yard",
        ]
    else:
        lines = []

    return {
        "status": "pass",
        "lines": lines,
        "error": None,
    }
