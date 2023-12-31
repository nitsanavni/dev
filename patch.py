import argparse
import logging
import os
import subprocess
from chat import chat_with_gpt4

if os.getenv("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)


def get_file_contents(file):
    if not os.path.isfile(file):
        open(file, "w").close()
    with open(file, "r") as f:
        contents = "\n".join(
            f"{i+1}: {line}" for i, line in enumerate(f.read().splitlines())
        )
    return contents


def make_prompt(file_contents, change):
    with open("patch.prompt", "r") as f:
        template = f.read()
    return template.format(file_contents=file_contents, change=change)


def patch(file_path, patch_content):
    proc = subprocess.run(
        ["patch", "-l", file_path], input=patch_content, text=True, capture_output=True
    )
    if proc.returncode != 0:
        raise Exception(f"Patching failed with the following message :\n {proc.stderr}")
    return proc.stdout


def git_diff(file_path):
    proc = subprocess.run(["git", "diff", file_path], capture_output=True, text=True)
    if proc.returncode != 0:
        raise Exception(f"Git diff failed with the following message :\n {proc.stderr}")
    return proc.stdout


def patch_change(file, change_description):
    """
    Given a change description in English, use a diff generated by GPT-4 to
    """

    patch_content = chat_with_gpt4(
        make_prompt(get_file_contents(file), change_description)
    )

    logging.debug(patch_content)

    patch(file, patch_content)
    print(git_diff(file))


def main():
    # TODO: extract a function for the argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="The file to be patched.")
    parser.add_argument("--change", required=True, help="The change to be made.")
    args = parser.parse_args()
    logging.debug(args.file)
    logging.debug(args.change)

    patch_change(args.file, args.change)


if __name__ == "__main__":
    main()
