"""JSON to CSV — Flatten a JSON array of objects into a CSV with a stable header."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='json_to_csv',
        description='Flatten a JSON array of objects into a CSV with a stable header.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('JSON to CSV')
    print('Objects back into a sheet.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
