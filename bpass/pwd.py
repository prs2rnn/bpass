#!/usr/bin/env python3

import argparse
import secrets
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import pyclip

__all__ = ["generate_password", "generate_passwords", "VERSION"]

VERSION = "0.1.0"


def generate_password(length: int) -> str:
    """Generate strong password by length"""
    all_chars = f"{ascii_lowercase}{ascii_uppercase}{digits}{punctuation}"

    if length < 4:
        return "".join(secrets.choice(all_chars) for _ in range(length))

    while True:
        password = "".join(secrets.choice(all_chars) for _ in range(length))
        if (any(c.isupper() for c in password) \
            and any(c.islower() for c in password) \
            and any(c.isdigit() for c in password) \
            and any(c in punctuation for c in password)):

            return password


def generate_passwords(length: int, amount: int) -> str:
    """Generate strong passwords by amount"""
    return "\n".join(generate_password(length) for _ in range(amount))


def integer(text: str) -> int:
    """Handle invalid arguments with argparse"""
    number = int(text)
    if number < 1:
        raise argparse.ArgumentTypeError("the number should be greater than zero")
    elif number > 10**5:
        raise argparse.ArgumentTypeError("the number is too large")
    return number


def args_parsing():
    """Parse arguments from the command line"""
    description = "bpass - simple cli password-generator"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} {VERSION}"
    )
    parser.add_argument(
        "-l",
        dest="length",
        type=integer,
        default=25,
        help="password length",
        metavar="integer",
    )
    parser.add_argument(
        "-a",
        dest="amount",
        type=integer,
        default=1,
        help="password amount",
        metavar="integer",
    )
    parser.add_argument(
        "-c", dest="copy", action="store_true", help="copy to clipboard"
    )

    return parser.parse_args()


def main():
    args = args_parsing()
    password = generate_passwords(args.length, args.amount)
    if args.copy:
        try:
            pyclip.copy(password)
        except:
            pass
    print(password)


if __name__ == "__main__":
    main()
