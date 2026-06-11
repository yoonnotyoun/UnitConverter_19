import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from convert import convert


def main():
    input_str = input("Insert value for converting (ex: meter:2.5): ")

    result = convert(input_str)

    if result["status"] == "pass":
        for line in result["lines"]:
            print(line)
    else:
        print(result["error"]["message"])


if __name__ == "__main__":
    main()
