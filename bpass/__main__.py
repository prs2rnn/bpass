import argparse
import secrets
from os import path, popen
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from sys import executable
from typing import Iterator

import pyclip


def generate_password(length: int) -> str:
    """Generate strong password by length"""
    all_chars = f"{ascii_lowercase}{ascii_uppercase}{digits}{punctuation}"

    if length < 4:
        return "".join(secrets.choice(all_chars) for _ in range(length))

    while True:
        password = "".join(secrets.choice(all_chars) for _ in range(length))
        if (
            any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in punctuation for c in password)
        ):
            return password


def generate_passwords(length: int, amount: int) -> Iterator[str]:
    """Generate strong passwords by amount"""
    return (generate_password(length) for _ in range(amount))


def control_numbers(args: argparse.Namespace) -> tuple[int, int]:
    """Handle arguments value > 10**4"""
    if args.length > 10**4 or args.amount > 10**4:
        try:
            choice = input(f"Type 'yes' if you want to proceed? ").lower()
            if choice != "yes":
                exit()
        except (KeyboardInterrupt, EOFError):
            print()
            exit()

    return args.length, args.amount


def integer(text: str) -> int:
    """Handle arguments < 1 with argparse"""
    number = int(text)
    if number < 1:
        raise argparse.ArgumentTypeError("value < 1")
    return number


def args_parsing() -> argparse.Namespace:
    """Parse arguments from the command line"""
    description = "bpass - simple cli password-generator"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "-l",
        dest="length",
        type=integer,
        default=25,
        metavar="integer",
        help="password length",
    )
    parser.add_argument(
        "-a",
        dest="amount",
        type=integer,
        default=1,
        metavar="integer",
        help="password amount",
    )

    return parser.parse_args()


def main() -> None:
    length, amount = control_numbers(args_parsing())
    if amount == 1:
        password = next(generate_passwords(length, amount))
        print(password)
        try:
            pyclip.copy(password)
            # run other process to clear clipboard
            popen(
                f"{executable} \
            {path.join(path.abspath(path.dirname(__file__)), 'clear.py')}"
            )
        except Exception:
            pass
        return

    print(*generate_passwords(length, amount), sep="\n")


if __name__ == "__main__":
    main()
