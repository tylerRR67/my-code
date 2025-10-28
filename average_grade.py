#!/usr/bin/env python3
"""
average_grade.py
Reads three exam scores (A, B, C), validates them, computes the average,
and prints whether the student is approved (average >= 7) or not.

Usage (interactive):
  python3 average_grade.py

Usage (non-interactive):
  printf '8\n7\n6\n' | python3 average_grade.py

Optional: you can pass three scores as command-line arguments:
  python3 average_grade.py 8 7 6
"""
import sys


def parse_score(s):
    try:
        return float(s)
    except Exception:
        return None


def read_score(prompt_text):
    try:
        s = input(prompt_text)
    except EOFError:
        print("\nNo input received. Exiting.", file=sys.stderr)
        sys.exit(1)
    if s is None:
        return None
    s = s.strip()
    if s == "":
        return None
    return parse_score(s)


def main():
    # Allow passing scores as command-line arguments for convenience
    if len(sys.argv) >= 4:
        vals = [parse_score(x) for x in sys.argv[1:4]]
        if None not in vals:
            a, b, c = vals
        else:
            # fall back to interactive prompts if args invalid
            a = b = c = None
    else:
        a = b = c = None

    if a is None:
        a = read_score("Enter score A: ")
        while a is None:
            print("Please enter a valid number for score A.")
            a = read_score("Enter score A: ")

    if b is None:
        b = read_score("Enter score B: ")
        while b is None:
            print("Please enter a valid number for score B.")
            b = read_score("Enter score B: ")

    if c is None:
        c = read_score("Enter score C: ")
        while c is None:
            print("Please enter a valid number for score C.")
            c = read_score("Enter score C: ")

    avg = (a + b + c) / 3.0

    print()
    print(f"Scores: A={a:.2f}, B={b:.2f}, C={c:.2f}")
    print(f"Average: {avg:.2f}")

    if avg >= 7.0:
        print("Result: Approved")
    else:
        print("Result: Not approved")


if __name__ == '__main__':
    main()
