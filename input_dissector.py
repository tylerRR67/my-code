#!/usr/bin/env python3
"""
input_dissector.py
Read a single input (CLI args, piped, or interactive) and report:
- only whitespace
- contains only numbers (digits only)
- alphabetical only (letters only)
- alphanumeric (letters or digits only)
- all upper case
- all lower case
- capitalized (first letter uppercase, rest lowercase)
- title case (each word capitalized)

Assumptions:
- "only numbers" means only decimal digits (no sign, no decimal point).
- "capitalized" means the string equals s.capitalize() and first char is uppercase.
- Title case uses str.istitle() (each word capitalized).
"""
import sys


def get_input():
    if len(sys.argv) >= 2:
        # join remaining args with spaces to allow multi-word inputs
        return ' '.join(sys.argv[1:])
    # Try reading a line from stdin (works for piped input)
    try:
        return input()
    except EOFError:
        # No input
        return ''


def analyze(s):
    # We'll keep the original string
    original = s
    # For many checks we consider the raw string (including spaces).
    # Some checks require presence of at least one character of relevant type.

    results = {}
    results['original'] = original

    # Only whitespace: non-empty and all whitespace
    results['only_whitespace'] = (len(original) > 0 and original.strip() == '')

    # Only numbers: all characters are digits (0-9)
    results['only_numbers'] = original.isdigit()

    # Alphabetical only: letters only (no spaces)
    results['only_alpha'] = original.isalpha()

    # Alphanumeric: letters or digits only
    results['alphanumeric'] = original.isalnum()

    # All upper / lower: these methods return False if there are no cased characters
    results['all_upper'] = original.isupper()
    results['all_lower'] = original.islower()

    # Capitalized: first char uppercase and the rest lowercase -> use capitalize()
    # Note: s.capitalize() lowercases the rest of the string, so 'HELLO' -> 'Hello' (not equal)
    # We'll require that the string equals s.capitalize() and that first char is alpha and uppercase
    if len(original) >= 1 and original[0].isalpha():
        results['capitalized'] = (original == original.capitalize())
    else:
        results['capitalized'] = False

    # Title case: each word capitalized -> use istitle()
    results['title_case'] = original.istitle()

    return results


def pretty_print(res):
    s = res['original']
    print('\nInput dissector results:')
    print(f"Original: {repr(s)}")
    print(f"Only whitespace: {res['only_whitespace']}")
    print(f"Only numbers (digits only): {res['only_numbers']}")
    print(f"Alphabetical only: {res['only_alpha']}")
    print(f"Alphanumeric: {res['alphanumeric']}")
    print(f"All upper case: {res['all_upper']}")
    print(f"All lower case: {res['all_lower']}")
    print(f"Capitalized (first upper, rest lower): {res['capitalized']}")
    print(f"Title case (each word capitalized): {res['title_case']}")
    print()


def main():
    s = get_input()
    res = analyze(s)
    pretty_print(res)

if __name__ == '__main__':
    main()
