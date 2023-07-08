import argparse
import difflib
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(
        description="This is a command verification script.")
    parser.add_argument('--executor', type=str,
                        required=True, help="Command executor.")
    parser.add_argument('--command', type=str, required=True,
                        help="Command to be executed.")
    parser.add_argument('--name', type=str, required=True,
                        help="Name for the tests.")
    args = parser.parse_args()

    approved_file_name = args.name + ".approved"
    with open(approved_file_name, "r") as file:
        approved_command = file.read()

    command_result = subprocess.run(
        [args.executor, args.command], capture_output=True, text=True).stdout
    approved_command_result = subprocess.run(
        [args.executor, approved_command], capture_output=True, text=True).stdout

    difference_command = difflib.ndiff([args.command], [approved_command])
    difference_result = difflib.ndiff(
        command_result.splitlines(), approved_command_result.splitlines())

    if difference_command or difference_result:
        print("=== DIFFERENCE FOUND ===")
        print("\n=== Command difference ===")
        print('\n'.join(difference_command))
        print("\n=== Result difference ===")
        print('\n'.join(difference_result))
        sys.exit(1)
    else:
        print("=== NO DIFFERENCE FOUND. TEST PASSED ===")
        sys.exit(0)


if __name__ == "__main__":
    main()
