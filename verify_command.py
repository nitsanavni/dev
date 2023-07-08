import argparse
import difflib
import subprocess
import sys
import os


def main():
    parser = argparse.ArgumentParser(
        description="This is a command verification script.")
    parser.add_argument('--executor', type=str,
                        required=True, help="Command executor.")
    parser.add_argument('--command', type=str, required=True,
                        help="Command to be executed.")
    parser.add_argument('--name', type=str, required=True,
                        help="Name for the tests.")
    parser.add_argument('--approve', action='store_true',
                        help="Approve the command.")
    args = parser.parse_args()

    approved_file_name = args.name + ".approved"

    if args.approve:
        with open(approved_file_name, 'w') as file:
            file.write(args.command)
        sys.exit(0)

    approved_command = ''

    if os.path.isfile(approved_file_name):
        with open(approved_file_name, "r") as file:
            approved_command = file.read()

    if args.command == approved_command:
        print("=== NO DIFFERENCE FOUND. TEST PASSED ===")
        sys.exit(0)
        return

    difference_command = difflib.ndiff([args.command], [approved_command])

    command_result = subprocess.run(args.executor.split(
    ) + [args.command], capture_output=True, text=True).stdout

    if approved_command:
        approved_command_result = subprocess.run(args.executor.split(
        ) + [approved_command], capture_output=True, text=True).stdout
    else:
        approved_command_result = ''

    difference_result = difflib.ndiff(
        command_result.splitlines(), approved_command_result.splitlines())

    print("=== DIFFERENCE FOUND ===")
    print("\n=== Command difference ===")
    print('\n'.join(difference_command))
    print("\n=== Result difference ===")
    print('\n'.join(difference_result))
    sys.exit(1)


if __name__ == "__main__":
    main()
