import argparse

from fibonacci_tdd_kata import fibonacci


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="fibonacci-kata",
        description=("Print a Fibonacci number for one index, or a range of indices."),
    )
    parser.add_argument(
        "n",
        type=int,
        nargs="?",
        help="A single Fibonacci index (ignored if --start/--end are given).",
    )
    parser.add_argument("--start", type=int, help="Start index of a range (inclusive).")
    parser.add_argument("--end", type=int, help="End index of a range (inclusive).")
    return parser


def main() -> None:
    """Run the Fibonacci command-line interface."""
    parser = build_parser()
    args = parser.parse_args()

    if args.start is not None and args.end is not None:
        if args.start < 0 or args.end < args.start:
            parser.error("The range must satisfy 0 <= --start <= --end.")
        for i in range(args.start, args.end + 1):
            print(fibonacci(i))
    elif args.start is not None or args.end is not None:
        parser.error("Provide both --start and --end.")
    elif args.n is not None:
        try:
            print(fibonacci(args.n))
        except ValueError as error:
            parser.error(str(error))
    else:
        parser.error("Provide either a single index, or --start and --end.")


if __name__ == "__main__":
    main()
