#!/usr/bin/env python3
"""
input_inspector.py
Read a single input string (CLI arg, piped, or interactive) and print a detailed
analysis: length, counts (letters, digits, whitespace, punctuation), word count,
unique characters, frequency table, per-character codepoints and Unicode names,
numeric detection (int/float), ASCII check, byte lengths, palindrome check, etc.
"""
import sys
import unicodedata
import string
from collections import Counter


def get_input():
    # CLI args: take the rest joined as a single string
    if len(sys.argv) >= 2:
        return ' '.join(sys.argv[1:])
    # Try reading a piped line or interactive input
    try:
        line = input()
        return line
    except EOFError:
        return ''


def is_printable(ch):
    # consider non-control printable
    return ch.isprintable()


def analyze(s):
    info = {}
    info['original'] = s
    info['length_chars'] = len(s)
    info['length_bytes_utf8'] = len(s.encode('utf-8'))
    info['ascii_only'] = s.isascii()

    # whitespace trimming
    info['leading_whitespace'] = len(s) - len(s.lstrip('\t\n\r '))
    info['trailing_whitespace'] = len(s) - len(s.rstrip('\t\n\r '))

    # words (split on whitespace)
    words = s.split()
    info['word_count'] = len(words)
    info['words'] = words

    # counts
    counts = {
        'letters': 0,
        'digits': 0,
        'whitespace': 0,
        'punctuation': 0,
        'upper': 0,
        'lower': 0,
        'others': 0
    }
    punct_set = set(string.punctuation)
    freq = Counter()
    for ch in s:
        freq[ch] += 1
        if ch.isalpha():
            counts['letters'] += 1
            if ch.isupper():
                counts['upper'] += 1
            if ch.islower():
                counts['lower'] += 1
        elif ch.isdigit():
            counts['digits'] += 1
        elif ch.isspace():
            counts['whitespace'] += 1
        elif ch in punct_set:
            counts['punctuation'] += 1
        else:
            counts['others'] += 1
    info['counts'] = counts

    # unique chars and frequency sorted
    info['unique_chars'] = len(freq)
    info['freq_top'] = freq.most_common(20)

    # per-character details (codepoint, hex, category, name)
    char_details = []
    for ch, cnt in freq.items():
        cp = ord(ch)
        try:
            name = unicodedata.name(ch)
        except ValueError:
            name = '<no name>'
        cat = unicodedata.category(ch)
        char_details.append({
            'char': ch,
            'count': cnt,
            'codepoint_dec': cp,
            'codepoint_hex': hex(cp),
            'category': cat,
            'name': name,
            'printable': is_printable(ch)
        })
    info['char_details'] = sorted(char_details, key=lambda d: (-d['count'], d['codepoint_dec']))

    # numeric detection
    info['is_int'] = False
    info['is_float'] = False
    try:
        iv = int(s)
        info['is_int'] = True
        info['int_value'] = iv
    except Exception:
        try:
            fv = float(s)
            info['is_float'] = True
            info['float_value'] = fv
        except Exception:
            pass

    # palindrome (ignore whitespace and case)
    stripped = ''.join(ch for ch in s if not ch.isspace())
    info['is_palindrome_case_sensitive'] = stripped == stripped[::-1]
    info['is_palindrome_case_insensitive'] = stripped.lower() == stripped.lower()[::-1]

    return info


def pretty_print(info):
    s = info['original']
    print('\n=== Input Inspector ===')
    print(f"Original (raw): {repr(s)}")
    print(f"Characters: {info['length_chars']}")
    print(f"UTF-8 bytes: {info['length_bytes_utf8']}")
    print(f"ASCII only: {info['ascii_only']}")
    print(f"Leading whitespace chars: {info['leading_whitespace']}")
    print(f"Trailing whitespace chars: {info['trailing_whitespace']}")
    print(f"Word count: {info['word_count']}")
    if info['word_count'] > 0:
        print(f"Words: {info['words']}")
    print('\n-- Character counts --')
    for k, v in info['counts'].items():
        print(f"{k.capitalize():12}: {v}")
    print(f"Unique characters: {info['unique_chars']}")

    print('\n-- Top character frequencies --')
    for ch, cnt in info['freq_top']:
        # make non-printable visible
        display = ch if ch.isprintable() and ch != ' ' else repr(ch)
        print(f"{display!s:6} : {cnt}")

    print('\n-- Character details (top first) --')
    for d in info['char_details'][:50]:
        ch = d['char']
        display = ch if ch.isprintable() and ch != ' ' else repr(ch)
        print(f"{display:6} count={d['count']:3} cp={d['codepoint_dec']:6} ({d['codepoint_hex']}) cat={d['category']} name={d['name']}")

    print('\n-- Numeric detection --')
    if info.get('is_int'):
        print(f"String is an integer: {info['int_value']}")
    elif info.get('is_float'):
        print(f"String is a float: {info['float_value']}")
    else:
        print('Not a pure number (int/float).')

    print('\n-- Palindrome checks --')
    print(f"Palindrome (case-sensitive, ignore spaces): {info['is_palindrome_case_sensitive']}")
    print(f"Palindrome (case-insensitive, ignore spaces): {info['is_palindrome_case_insensitive']}")

    print('\nDone.\n')


def main():
    s = get_input()
    info = analyze(s)
    pretty_print(info)

if __name__ == '__main__':
    main()
