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
    elif unit == "feet":
        in_meter = round(value / METER_TO_FEET, ROUND_DECIMALS)
        in_yard = round(in_meter * METER_TO_YARD, ROUND_DECIMALS)
        lines = [
            f"{value} {unit} = {in_meter} meter",
            f"{value} {unit} = {in_yard} yard",
        ]
    elif unit == "yard":
        in_meter = round(value / METER_TO_YARD, ROUND_DECIMALS)
        in_feet = round(in_meter * METER_TO_FEET, ROUND_DECIMALS)
        lines = [
            f"{value} {unit} = {in_meter} meter",
            f"{value} {unit} = {in_feet} feet",
        ]
    else:
        lines = []

    return {
        "status": "pass",
        "lines": lines,
        "error": None,
    }
