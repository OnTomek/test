import os
import requests

folder_path = 'C:/temp/depolyment_package'

# Function to get branch name from a pull request
def get_branch_name_from_pr(owner, repo, pr_number, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        pr_data = response.json()
        branch_name = pr_data['head']['ref']
        return branch_name
    else:
        print(f'Failed to fetch pull request: {response.status_code}')
        return None

# Function to create a folder with the branch name
def create_folder(branch_name):
    if branch_name:
        try:
            os.makedirs(branch_name, exist_ok=True)
            print(f'Folder "{branch_name}" created successfully.')
        except Exception as e:
            print(f'Failed to create folder: {e}')
    else:
        print('No branch name provided.')

if __name__ == "__main__":
    # Repository details and token
    owner = 'OnTomek'
    repo = 'test'
    pr_number = 2
    token = '' # Add token

    branch_name = get_branch_name_from_pr(owner, repo, pr_number, token)
    create_folder(branch_name)
