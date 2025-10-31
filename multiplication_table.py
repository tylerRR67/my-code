#!/usr/bin/env python3
"""
multiplication_table.py
Prints the multiplication table for a given number.

Usage:
  Interactive:
    python3 multiplication_table.py
    Enter number: 7

  Pipe:
    printf '7\n' | python3 multiplication_table.py

  CLI args:
    python3 multiplication_table.py 7       # prints 1..10
    python3 multiplication_table.py 7 12    # prints 1..12

The script accepts integers or floats for the base number. The table length
(default 10) can be provided as a second argument or entered when prompted.
"""
import sys


def parse_number(s):
    try:
        return float(s)
    except Exception:
        return None


def parse_int(s):
    try:
        i = int(s)
        return i
    except Exception:
        return None


def read_input(prompt_text):
    try:
        return input(prompt_text)
    except EOFError:
        # No stdin available
        return None


def print_table(number, upto=10):
    # If number is integral value like 7.0, print as int
    base_fmt = "%g" if float(number).is_integer() else "{}"
    for i in range(1, upto + 1):
        result = number * i
        # Format nice: integers without .0
        def fmt(x):
            return str(int(x)) if float(x).is_integer() else f"{x}"
        print(f"{fmt(number)} x {i} = {fmt(result)}")


def main():
    number = None
    upto = 10

    # Try command-line args first
    if len(sys.argv) >= 2:
        number = parse_number(sys.argv[1])
        if len(sys.argv) >= 3:
            upto_candidate = parse_int(sys.argv[2])
            if upto_candidate is not None and upto_candidate > 0:
                upto = upto_candidate
    else:
        # Try reading from stdin non-interactively (piped)
        # Peek by attempting to read a line without blocking
        line = read_input("Enter number: ")
        if line is not None:
            line = line.strip()
            if line != "":
                # If the user typed both number and optionally upto separated by space
                parts = line.split()
                number = parse_number(parts[0]) if parts else None
                if len(parts) >= 2:
                    upto_candidate = parse_int(parts[1])
                    if upto_candidate is not None and upto_candidate > 0:
                        upto = upto_candidate

    # If still no number, prompt interactively
    if number is None:
        while True:
            s = read_input("Enter number: ")
            if s is None:
                print("No input received. Exiting.", file=sys.stderr)
                sys.exit(1)
            s = s.strip()
            if s == "":
                continue
            parts = s.split()
            number = parse_number(parts[0])
            if number is None:
                print("Please enter a valid number (integer or decimal).")
                continue
            if len(parts) >= 2:
                upto_candidate = parse_int(parts[1])
                if upto_candidate is not None and upto_candidate > 0:
                    upto = upto_candidate
            break

    # Final validation for upto
    if upto <= 0:
        print("Table length must be a positive integer. Using 10.")
        upto = 10

    print_table(number, upto)


if __name__ == '__main__':
    main()
