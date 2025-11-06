#!/usr/bin/env python3
"""
calculator.py
Simple calculator that reads: <number> <operator> <number>
Supported operators: +, -, *, /

Usage examples:
    Interactive: run without args and type: 3 + 4
    Pipe:        printf '3 + 4\n' | python3 calculator.py
    CLI args:    python3 calculator.py 3 + 4

The script validates input and handles division by zero.
"""
import sys


def parse_number(s):
    try:
        if '.' in s:
            return float(s)
        return int(s)
    except Exception:
        try:
            return float(s)
        except Exception:
            return None


def compute(a, op, b):
    try:
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a / b
        raise ValueError(f"Unsupported operator: {op}. Supported operators are + - * /")
    except ZeroDivisionError:
        raise


def read_input_line(prompt='Enter expression (e.g. 3 + 4): '):
    try:
        return input(prompt)
    except EOFError:
        return None


def main():
    tokens = None
    # CLI args: calculator.py 3 + 4
    if len(sys.argv) >= 4:
        tokens = sys.argv[1:4]
    else:
        # Try reading a line (either piped or interactive)
        line = read_input_line()
        if line is None:
            print('No input received. Exiting.', file=sys.stderr)
            sys.exit(1)
        line = line.strip()
        # Split respecting '**'
        # naive split on spaces
        parts = line.split()
        if len(parts) >= 3:
            # join operators if user typed '**'
            if parts[1] == '*' and len(parts) >= 4 and parts[2] == '*':
                tokens = [parts[0], '**', parts[3]]
            else:
                tokens = parts[0:3]
        else:
            print('Please enter an expression with two operands and an operator, e.g. 3 + 4')
            sys.exit(1)

    a_s, op, b_s = tokens
    a = parse_number(a_s)
    b = parse_number(b_s)
    if a is None:
        print(f'Invalid number: {a_s}', file=sys.stderr)
        sys.exit(1)
    if b is None:
        print(f'Invalid number: {b_s}', file=sys.stderr)
        sys.exit(1)

    try:
        result = compute(a, op, b)
    except ZeroDivisionError:
        print('Error: division or modulo by zero', file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

    print(result)


if __name__ == '__main__':
    main()
