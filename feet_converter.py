#!/usr/bin/env python3
"""
feet_converter.py
Convert a given number of feet to yards, miles, inches, leagues and meters.

Assumptions:
- 1 yard = 3 feet
- 1 mile = 5280 feet
- 1 league = 3 miles (common definition)
- 1 foot = 0.3048 meters

The script accepts input interactively, via piping, or as a single command-line argument.
Examples:
  Interactive:
    python3 feet_converter.py
    Enter feet: 5280

  Pipe:
    printf '5280\n' | python3 feet_converter.py

  Command-line:
    python3 feet_converter.py 5280
"""
import sys


def parse_number(s):
    try:
        return float(s)
    except Exception:
        return None


def read_feet(prompt_text="Enter feet: "):
    try:
        s = input(prompt_text)
    except EOFError:
        print("\nNo input received. Exiting.", file=sys.stderr)
        sys.exit(1)
    if s is None:
        print("No input. Exiting.", file=sys.stderr)
        sys.exit(1)
    s = s.strip()
    if s == "":
        return None
    return parse_number(s)


def main():
    # Accept a single command-line argument as feet
    feet = None
    if len(sys.argv) >= 2:
        feet = parse_number(sys.argv[1])
        if feet is None:
            feet = None  # fall back to interactive

    if feet is None:
        feet = read_feet()
        while feet is None:
            print("Please enter a valid number for feet (integer or decimal).")
            feet = read_feet()

    # Conversion constants
    FEET_PER_YARD = 3.0
    FEET_PER_MILE = 5280.0
    FEET_PER_LEAGUE = FEET_PER_MILE * 3.0  # 3 miles per league
    METERS_PER_FOOT = 0.3048

    yards = feet / FEET_PER_YARD
    miles = feet / FEET_PER_MILE
    inches = feet * 12.0
    leagues = feet / FEET_PER_LEAGUE
    meters = feet * METERS_PER_FOOT

    print()
    print(f"Input: {feet} ft")
    print(f"Yards:   {yards:.6f} yd")
    print(f"Miles:   {miles:.6f} mi")
    # inches often integer but allow decimals
    if inches.is_integer():
        print(f"Inches:  {int(inches)} in")
    else:
        print(f"Inches:  {inches:.2f} in")
    print(f"Leagues: {leagues:.6f} league(s)")
    print(f"Meters:  {meters:.4f} m")


if __name__ == '__main__':
    main()
