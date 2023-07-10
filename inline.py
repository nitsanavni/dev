import argparse
from patch import patch_change


def make_change_description(symbol):
    with open('inline.change_description', 'r') as f:
        template = f.read()
    return template.format(symbol=symbol)


def inline(file, symbol):
    patch_change(file, make_change_description(symbol))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True,
                        help="The file to be patched.")
    parser.add_argument('--symbol', required=True,
                        help="The symbol to inline.")
    args = parser.parse_args()

    inline(args.file, args.symbol)


if __name__ == "__main__":
    main()
