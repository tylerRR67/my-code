#!/usr/bin/env python3
"""
string_slicing_demo.py
Simple demonstration of Python string indexing and slicing.

Shows indices above characters, negative indices below, and several slice examples.
"""

s = "Example"

def print_index_map(s):
    # Print positive indices aligned with characters
    pos_indices = ' '.join(f"{i:>2}" for i in range(len(s)))
    chars = ' '.join(f" {c}" for c in s)
    neg_indices = ' '.join(f"{i:>3}" for i in range(-len(s), 0))
    print("String:")
    print(pos_indices)
    print(chars)
    print(neg_indices)
    print()


def demo_slices(s):
    examples = [
        ("s[0]", lambda: s[0]),
        ("s[-1]", lambda: s[-1]),
        ("s[0:3]", lambda: s[0:3]),
        ("s[1:4]", lambda: s[1:4]),
        ("s[:3]", lambda: s[:3]),
        ("s[3:]", lambda: s[3:]),
        ("s[:]", lambda: s[:]),
        ("s[::2]", lambda: s[::2]),
        ("s[::-1] (reverse)", lambda: s[::-1]),
    ]

    print("Slice examples:")
    for name, fn in examples:
        print(f"{name:20} -> {fn()}")
    print()


def main():
    print("=== String slicing demo ===")
    print(f"s = \"{s}\"\n")
    print_index_map(s)
    demo_slices(s)

    # Short exercises
    print("Quick exercises (answers shown):")
    print("1) First character: s[0] ->", s[0])
    print("2) Last character: s[-1] ->", s[-1])
    print("3) First three chars: s[:3] ->", s[:3])
    print("4) From index 2 length 3: s[2:2+3] ->", s[2:5])
    print("5) Reverse string: s[::-1] ->", s[::-1])

if __name__ == '__main__':
    main()
