import os
import sys
import requests
from git import Repo

def create_deployment_folder(branch_name):
    try:
        folder_path = os.path.join("C:/temp/deployment_package", branch_name.replace("/", "_"))
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created folder: {folder_path}")
        return folder_path
    except OSError as e:
        print(f"Failed to create folder: {e}")
        return None

def pull_and_merge(repo_path, main_branch, other_branch):
    try:
        repo = Repo(repo_path)
        origin = repo.remote(name='origin')
        origin.pull(main_branch)
        origin.pull(other_branch)
        repo.git.checkout(main_branch)
        repo.git.merge(other_branch)
        print(f"Pulled and merged changes from {other_branch} into {main_branch}")
    except Exception as e:
        print(f"Failed to pull and merge changes: {e}")

def create_package_file(folder_path, branch_name):
    try:
        file_path = os.path.join(folder_path, f"{branch_name.replace('/', '_')}.package")
        with open(file_path, 'w') as package_file:
            pass
        print(f"Created package file: {file_path}")
    except OSError as e:
        print(f"Failed to create package file: {e}")

# Merge pull request using GitHub API
def merge_pull_request(pull_request_number):
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return

    repo_owner = "OnTomek"  # Update this with your GitHub username or organization name
    repo_name = "test"       # Update this with your repository name

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

    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Pull request merged successfully on GitHub.")
    else:
        print(f"Failed to merge pull request on GitHub. Status code: {response.status_code}")

# get branch name from pull request
def get_branch_name(pull_request_number):
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return None
    
    repo_owner = "OnTomek"  # Update this with your GitHub username or organization name
    repo_name = "test"       # Update this with your repository name

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pull_request_number}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        branch_name = data['head']['ref']
        return branch_name
    except Exception as e:
        print(f"Failed to retrieve pull request information: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python final.py <pull_request_number>")
        sys.exit(1)

    pull_request_number = sys.argv[1]
    branch_name = get_branch_name(pull_request_number)
    if branch_name:
        folder_path = create_deployment_folder(branch_name)
        if folder_path:
            repo_path = "C:/temp/test"  # Update this with the path to your local repository
            main_branch = "main"        # Update this with the name of your main branch
            other_branch = branch_name
            pull_and_merge(repo_path, main_branch, other_branch)
            create_package_file(folder_path, branch_name)
            
            # Merge the pull request on GitHub
            merge_pull_request(pull_request_number)
        else:
            print("Failed to create deployment folder.")
    else:
        print("Unable to retrieve branch name from the pull request.")

if __name__ == "__main__":
    main()
