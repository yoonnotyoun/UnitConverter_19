import io
import os
from pathlib import Path

ERROR_CODES = {
    "format": "E001",
    "number": "E002",
    "unit": "E003",
    "negative": "E004",
}


def convert_result_to_int6(result: dict) -> list[str]:
    lines = [result["status"]]

    result_lines = result.get("lines") or []
    for index in range(3):
        lines.append(result_lines[index] if index < len(result_lines) else "")

    error = result.get("error")
    if error:
        error_type = error.get("type", "")
        lines.append(ERROR_CODES.get(error_type, "E005"))
        lines.append(error.get("message", ""))
    else:
        lines.extend(["", ""])

    if len(lines) != 6:
        raise ValueError("int[6] serialization requires exactly 6 lines")

    return lines


def serialize_convert_result(result: dict) -> str:
    return "".join(line + "\n" for line in convert_result_to_int6(result))


def parse_int6(text: str) -> list[str]:
    return [line.rstrip("\n") for line in io.StringIO(text).readlines()]


def assert_matches_golden(actual: str, golden_path: Path) -> None:
    golden_path.parent.mkdir(parents=True, exist_ok=True)

    if os.environ.get("UPDATE_GOLDEN") == "1":
        golden_path.write_text(actual, encoding="utf-8")
        return

    if not golden_path.exists():
        raise AssertionError(f"Golden file missing: {golden_path}")

    expected = golden_path.read_text(encoding="utf-8")
    if actual == expected:
        return

    actual_lines = parse_int6(actual)
    expected_lines = parse_int6(expected)
    diff_parts = []
    for index in range(6):
        line_no = index + 1
        got = actual_lines[index] if index < len(actual_lines) else ""
        want = expected_lines[index] if index < len(expected_lines) else ""
        if got != want:
            diff_parts.append(f"line {line_no}: expected {want!r}, got {got!r}")

    summary = "; ".join(diff_parts[:2]) if diff_parts else "content mismatch"
    raise AssertionError(f"Golden mismatch ({golden_path.name}): {summary}")
