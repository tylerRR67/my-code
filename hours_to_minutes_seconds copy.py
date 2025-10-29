#!/usr/bin/env python3
"""
hours_to_minutes_seconds.py
Reads a number of hours from stdin (or command-line argument), validates the input,
then prints the equivalent minutes and seconds.

Examples:
  Interactive:
    python3 hours_to_minutes_seconds.py
    Enter hours: 2

  Non-interactive (pipe):
    printf '2\n' | python3 hours_to_minutes_seconds.py

  Command-line args:
    python3 hours_to_minutes_seconds.py 2
"""
import sys


def parse_number(s):
    try:
        return float(s)
    except Exception:
        return None


def read_hours(prompt_text="Enter hours: "):
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
    # Allow passing hours as a single command-line argument
    hours = None
    if len(sys.argv) >= 2:
        hours = parse_number(sys.argv[1])
        if hours is None:
            # ignore invalid arg and fall back to interactive
            hours = None

    if hours is None:
        hours = read_hours()
        while hours is None:
            print("Please enter a valid number for hours (can be integer or decimal).")
            hours = read_hours()

    minutes = hours * 60.0
    seconds = hours * 3600.0

    print()
    print(f"Input: {hours} hour(s)")
    print(f"Minutes: {minutes:.2f} min")
    print(f"Seconds: {seconds:.2f} s")


if __name__ == '__main__':
    main()
