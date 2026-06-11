from constants import METER_TO_FEET, METER_TO_YARD, ROUND_DECIMALS, SUPPORTED_UNITS


def convert(input_str):
    if ":" not in input_str:
        return {
            "status": "fail",
            "lines": [],
            "error": {
                "type": "format",
                "message": "Invalid format. Use unit:value (ex: meter:2.5)",
            },
        }

    unit, value_str = input_str.split(":", 1)

    try:
        value = float(value_str)
    except ValueError:
        return {
            "status": "fail",
            "lines": [],
            "error": {
                "type": "number",
                "message": f"Invalid number: {value_str}",
            },
        }

    if unit in SUPPORTED_UNITS and value < 0:
        return {
            "status": "fail",
            "lines": [],
            "error": {
                "type": "negative",
                "message": f"Negative value not allowed: {value_str}",
            },
        }

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
        return {
            "status": "fail",
            "lines": [],
            "error": {
                "type": "unit",
                "message": f"Unknown unit: {unit}",
            },
        }

    return {
        "status": "pass",
        "lines": lines,
        "error": None,
    }
