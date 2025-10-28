#!/usr/bin/env python3
"""
Temperature converter: Fahrenheit -> Celsius and Kelvin
- Accepts a number (int or float) from stdin interactively or via piping
- Validates input and prints results with sensible formatting

Note: You wrote "Kevin" in the prompt — I assume you meant Kelvin.
"""
import sys


def read_temperature(prompt_text="Enter temperature in °F: "):
    try:
        s = input(prompt_text)
    except EOFError:
        print("\nNo input received. Exiting.", file=sys.stderr)
        sys.exit(1)
    if s is None:
        print("No input. Exiting.", file=sys.stderr)
        sys.exit(1)
    s = s.strip()
    if not s:
        print("Empty input. Exiting.", file=sys.stderr)
        sys.exit(1)
    # allow floats and integers, with optional + or -
    try:
        return float(s)
    except ValueError:
        print("Please enter a valid number for Fahrenheit (e.g. 72 or 98.6).", file=sys.stderr)
        return None


def f_to_c(f):
    return (f - 32.0) * 5.0 / 9.0


def f_to_k(f):
    return f_to_c(f) + 273.15


def main():
    f = read_temperature()
    # keep prompting until valid
    while f is None:
        f = read_temperature()

    c = f_to_c(f)
    k = f_to_k(f)

    # Print results with nice formatting
    print()
    print(f"Input: {f} °F")
    print(f"Celsius: {c:.2f} °C")
    print(f"Kelvin: {k:.2f} K")


if __name__ == '__main__':
    main()
