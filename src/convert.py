from constants import METER_TO_FEET, METER_TO_YARD, ROUND_DECIMALS, SUPPORTED_UNITS


def _fail(error_type, message):
    return {
        "status": "fail",
        "lines": [],
        "error": {
            "type": error_type,
            "message": message,
        },
    }


def _lines_for_unit(unit, value):
    if unit == "meter":
        in_feet = round(value * METER_TO_FEET, ROUND_DECIMALS)
        in_yard = round(value * METER_TO_YARD, ROUND_DECIMALS)
        return [
            f"{value} {unit} = {in_feet} feet",
            f"{value} {unit} = {in_yard} yard",
        ]
    if unit == "feet":
        in_meter = round(value / METER_TO_FEET, ROUND_DECIMALS)
        in_yard = round(in_meter * METER_TO_YARD, ROUND_DECIMALS)
        return [
            f"{value} {unit} = {in_meter} meter",
            f"{value} {unit} = {in_yard} yard",
        ]
    in_meter = round(value / METER_TO_YARD, ROUND_DECIMALS)
    in_feet = round(in_meter * METER_TO_FEET, ROUND_DECIMALS)
    return [
        f"{value} {unit} = {in_meter} meter",
        f"{value} {unit} = {in_feet} feet",
    ]


def convert(input_str):
    if ":" not in input_str:
        return _fail(
            "format",
            "Invalid format. Use unit:value (ex: meter:2.5)",
        )

    unit, value_str = input_str.split(":", 1)

    try:
        value = float(value_str)
    except ValueError:
        return _fail("number", f"Invalid number: {value_str}")

    if unit in SUPPORTED_UNITS and value < 0:
        return _fail("negative", f"Negative value not allowed: {value_str}")

    if unit not in SUPPORTED_UNITS:
        return _fail("unit", f"Unknown unit: {unit}")

    return {
        "status": "pass",
        "lines": _lines_for_unit(unit, value),
        "error": None,
    }
