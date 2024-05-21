import os

def get_branch_name_from_pull_request(pull_request_number):
    github_token = os.getenv("GITHUB_TOKEN")  # Fetch the token from environment variables
    if not github_token:
        print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return None
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pull_request_number}"
    repo_owner = "OnTomek"
    repo_name = "test"

def create_deployment_folder(repo_name):
    os.makedirs(parent_directory, exist_ok=True)

parent_directory = f"C:/temp/depolyment_folder_path/{repo_name}"

new_folder_path = os.path.join(parent_directory, repo_name)

try:
    os.makedirs(new_folder_path, exist_ok=True)
    print(f"Folder '{new_folder_name}' created successfully in '{parent_directory}'")
except Exception as e:
    print(f"An error occurred: {e}")
