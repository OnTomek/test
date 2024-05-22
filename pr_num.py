import os
import sys
import requests

def create_deployment_folder(branch_name):
    folder_path = f"C:/temp/deployment_package/{branch_name}"
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder: {folder_path}")

def get_branch_name_from_pull_request(pull_request_number):
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return None
    
    repo_owner = "OnTomek"
    repo_name = "test"

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
        print("Usage: python pr_num.py <pull_request_number>")
        sys.exit(1)

    pull_request_number = sys.argv[1]
    branch_name = get_branch_name_from_pull_request(pull_request_number)
    if branch_name:
        create_deployment_folder(branch_name)
    else:
        print("Unable to create deployment folder.")

if __name__ == "__main__":
    main()
