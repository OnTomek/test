"""
import os
import sys
import requests
from git import Repo

def create_deployment_folder(branch_name):
    folder_path = f"C:/temp/deployment_package/{branch_name}"
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder: {folder_path}")
    return folder_path

def pull_and_merge(repo_path, main_branch, other_branch):
    repo = Repo(repo_path)
    origin = repo.remote(name='origin')
    origin.pull(main_branch)
    origin.pull(other_branch)
    repo.git.merge(other_branch)

def create_package_file(folder_path, branch_name):
    file_path = os.path.join(folder_path, f"{branch_name}.package")
    with open(file_path, 'w') as package_file:
        pass
    print(f"Created package file: {file_path}")

# get branch name from pull request
def get_branch_name(pull_request_number):
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
            print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
            return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python final.py <pull_request_number>")
        sys.exit(1)

    pull_request_number = sys.argv[1]
    branch_name = get_branch_name(pull_request_number)
    if branch_name:
        folder_path = create_deployment_folder(branch_name)
        repo_path = "C:/temp/test"
        main_branch = "main"  # Update this with the name of your main branch
        other_branch = branch_name
        pull_and_merge(repo_path, main_branch, other_branch)
        create_package_file(folder_path, branch_name)
    else:
        print("Unable to create deployment folder.")

if __name__ == "__main__":
    main()
"""


import os
import sys
import requests
from git import Repo

def create_deployment_folder(branch_name):
    folder_path = f"C:/temp/deployment_package/{branch_name}"
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder: {folder_path}")
    return folder_path

def pull_and_merge(repo_path, main_branch, other_branch):
    repo = Repo(repo_path)
    origin = repo.remote(name='origin')
    origin.pull(main_branch)
    origin.pull(other_branch)
    repo.git.merge(other_branch)

def create_package_file(folder_path, branch_name):
    file_path = os.path.join(folder_path, f"{branch_name}.package")
    with open(file_path, 'w') as package_file:
        pass
    print(f"Created package file: {file_path}")

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

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        branch_name = data['head']['ref']
        return branch_name
    else:
        print(f"Failed to retrieve pull request information. Status code: {response.status_code}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python final.py <pull_request_number>")
        sys.exit(1)

    pull_request_number = sys.argv[1]
    branch_name = get_branch_name(pull_request_number)
    if branch_name:
        folder_path = create_deployment_folder(branch_name)
        repo_path = "C:/temp/test"
        main_branch = "main"        # Update this with the name of your main branch
        other_branch = branch_name
        pull_and_merge(repo_path, main_branch, other_branch)
        create_package_file(folder_path, branch_name)
    else:
        print("Unable to create deployment folder.")

if __name__ == "__main__":
    main()
