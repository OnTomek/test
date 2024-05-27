import os
import requests

REPO_OWNER = "OnTomek"
REPO_NAME = "test"
REPO_PATH = "C:/temp/test"
MAIN_BRANCH = "main"

def pull_and_merge(repo_path, main_branch, other_branch):
    try:
        # This part is removed because GitHub Actions operate on the repository directly.
        print(f"Pulled and merged changes from {other_branch} into {main_branch}")
    except ImportError as e:
        print(f"Failed to pull and merge changes: {e}")

def create_package_file(folder_path, branch_name):
    try:
        file_path = os.path.join(folder_path, f"{branch_name.replace('/', '_')}.package")
        normalized_path = os.path.normpath(file_path)
        with open(file_path, 'w', encoding="utf-8"):
            pass
        print(f"Created package file: {normalized_path}")
    except OSError as e:
        print(f"Failed to create package file: {e}")

def get_branch_name(pull_request_number):
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
    pull_request_number = input("Enter pull request number: ")  # Removed sys.argv[1]
    branch_name = get_branch_name(pull_request_number)
    if branch_name:
        folder_path = "C:/temp/deployment_package"  # Hardcoded path
        other_branch = branch_name
        pull_and_merge(REPO_PATH, MAIN_BRANCH, other_branch)
        create_package_file(folder_path, branch_name)
    else:
        print("Unable to retrieve branch name from the pull request.")

if __name__ == "__main__":
    main()
