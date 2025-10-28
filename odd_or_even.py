#!/usr/bin/env python3
"""
odd_or_even.py
Simple script that asks for a whole number and prints whether it's odd or even.
Handles EOF (Ctrl-D) and validates input.
"""
import sys


def read_int(prompt_text="Enter a whole number: "):
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
        return None
    # Accept optional leading + or - and digits
    if (s[0] in '+-' and s[1:].isdigit()) or s.isdigit():
        try:
            return int(s)
        except ValueError:
            return None
    return None


def main():
    n = read_int()
    while n is None:
        print("Please enter a valid whole number.")
        n = read_int()

    if n % 2 == 0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd.")


if __name__ == '__main__':
    main()
