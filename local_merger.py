import os
import sys
import requests
import click
from pathlib import Path
from git import Repo

REPO_OWNER = "OnTomek"
REPO_NAME = "test"
REPO_PATH = "C:/temp/test"
MAIN_BRANCH = "main"

"""@click.command()
@click.option('--owner', type=str, required=True, help='A string prompt')
@click.option('--repo', type=str, required=True, help='A string prompt')
@click.option('--path', type=click.Path(exists=True, path_type=Path), required=True, help='')
@click.option('--main', type=str, required=True, help='A string prompt')

def validate_inputs(owner, repo, path, main):
    ""Validate and print the inputs.""
    # Print the inputs
    click.echo(f'Owner: {owner}')
    click.echo(f'Repo: {repo}')
    click.echo(f'Path: {path}')
    click.echo(f'Main: {main}')"""

def create_deployment_folder(branch_name):
    """Function creates folder on a constant path."""
    try:
        folder_path = os.path.join("C:/temp/deployment_package", branch_name.replace("/", "_"))
        normalized_path = os.path.normpath(folder_path)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {normalized_path}")
        return folder_path
    except OSError as e:
        print(f"Failed to create folder: {e}")
        return None

# Merges the pull request locally
def pull_and_merge(repo_path, main_branch, other_branch):
    """Pulls and merges the branches together."""
    try:
        repo = Repo(repo_path)
        origin = repo.remote(name='origin')
        origin.pull(main_branch)
        origin.pull(other_branch)
        repo.git.checkout(main_branch)
        repo.git.merge(other_branch)
        print(f"Pulled and merged changes from {other_branch} into {main_branch}")
    except ImportError as e:
        print(f"Failed to pull and merge changes: {e}")

def create_package_file(folder_path, branch_name):
    """Function creating package file."""
    try:
        file_path = os.path.join(folder_path, f"{branch_name.replace('/', '_')}.package")
        normalized_path = os.path.normpath(file_path)
        with open(file_path, 'w', encoding="utf-8"):
            pass
        print(f"Created package file: {normalized_path}")
    except OSError as e:
        print(f"Failed to create package file: {e}")

"""
def merge_pull_request(pull_request_number):
    # Function merges pull request via github token.
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return

    repo_owner = "OnTomek"  # Update this with your GitHub username or organization name
    repo_name = "test"      # Update this with your repository name

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pull_request_number}/merge"

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "commit_title": f"Merge pull request #{pull_request_number}",
        "commit_message": f"Merging pull request #{pull_request_number} via script",
        "merge_method": "merge"
    }

    response = requests.put(url, json=data, headers=headers, timeout=5)
    if response.status_code == 200:
        print("Pull request merged successfully on GitHub.")
    else:
        print(f"Failed to merge pull request on GitHub. Status code: {response.status_code}")
"""

def get_branch_name(pull_request_number):
    """Function gets the branch name from pull request."""
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return None

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{pull_request_number}"

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        branch_name = data['head']['ref']
        return branch_name
    except ImportError as e:
        print(f"Failed to retrieve pull request information: {e}")
        return None

def main():
    """Main function, puts it together."""
    if len(sys.argv) < 2:
        print("Usage: python local_merger.py <pull_request_number>")
        sys.exit(1)

    pull_request_number = sys.argv[1]
    branch_name = get_branch_name(pull_request_number)
    if branch_name:
        folder_path = create_deployment_folder(branch_name)
        if folder_path:
            other_branch = branch_name
            pull_and_merge(REPO_PATH, MAIN_BRANCH, other_branch)
            create_package_file(folder_path, branch_name)
            """merge_pull_request(pull_request_number)"""
        else:
            print("Failed to create deployment folder.")
    else:
        print("Unable to retrieve branch name from the pull request.")

if __name__ == "__main__":
    main()
    """validate_input()"""
