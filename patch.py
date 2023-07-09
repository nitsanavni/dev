import argparse
import subprocess
import os
from chat import chat_with_gpt4


def make_prompt(file_contents, change):
    with open('patch.prompt', 'r') as f:
        template = f.read()
    return template.format(file_contents=file_contents, change=change)


def patch(file_path, patch_content):
    proc = subprocess.run(['patch', '-l', file_path],
                          input=patch_content, text=True, capture_output=True)
    if proc.returncode != 0:
        raise Exception(
            f"Patching failed with the following message :\n {proc.stderr}")
    return proc.stdout


def git_diff(file_path):
    proc = subprocess.run(['git', 'diff', file_path],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise Exception(
            f"Git diff failed with the following message :\n {proc.stderr}")
    return proc.stdout


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True,
                        help="The file to be patched.")
    parser.add_argument('--change', required=True,
                        help="The change to be made.")
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        file_contents = f.read()

    prompt_text = make_prompt(file_contents, args.change)

    patch_content = chat_with_gpt4("api_key", prompt_text)

    patch(args.file, patch_content)
    print(git_diff(args.file))


if __name__ == "__main__":
    main()
