import os
import sys
import subprocess
import argparse
import shutil

DEPLOYMENT_PACKAGE_DIR = "C:/temp/deployment package"

def run_command(command, cwd=None):
    """Run a shell command and print the output."""
    result = subprocess.run(command, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Command failed with error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

def create_folder(path):
    """Create a folder if it does not exist."""
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Folder '{path}' created successfully.")
    except Exception as e:
        print(f"Failed to create folder '{path}': {e}")
        sys.exit(1)

def retrieve_branch_name(pull_request):
    """Retrieve branch name from the pull request. Simulating for example."""
    # In a real-world scenario, use GitHub API to retrieve this information.
    return f"feature/{pull_request}"

def main():
    parser = argparse.ArgumentParser(description="Tool for creating a deployment package from a GitHub pull request.")
    parser.add_argument('--repo-path', required=True, help='Path to the local repository')
    parser.add_argument('--pull-request', required=True, help='Pull request number')
    parser.add_argument('--unique-id', help='Unique ID to prefix the folder name')

    args = parser.parse_args()
    
    repo_path = args.repo_path
    pull_request = args.pull_request
    unique_id = args.unique_id

    branch_name = retrieve_branch_name(pull_request)
    folder_name = f"{unique_id}_{branch_name}" if unique_id else branch_name
    folder_path = os.path.join(DEPLOYMENT_PACKAGE_DIR, folder_name)

    # Create the folder for the deployment package
    create_folder(folder_path)

    # Change to the repository directory
    os.chdir(repo_path)

    # Pull master and the branch
    run_command("git checkout master")
    if run_command("git pull origin master") != 0:
        print("Failed to pull master branch.")
        sys.exit(1)

    run_command(f"git checkout {branch_name}")
    if run_command(f"git pull origin {branch_name}") != 0:
        print(f"Failed to pull branch {branch_name}.")
        sys.exit(1)

    # Merge master into the branch
    if run_command("git merge master") != 0:
        print(f"Failed to merge master into {branch_name}.")
        sys.exit(1)

    # Create the package file
    package_file = os.path.join(folder_path, f"{branch_name.replace('/', '_')}.package")
    try:
        with open(package_file, 'w') as f:
            f.write("")
        print(f"Package file '{package_file}' created successfully.")
    except Exception as e:
        print(f"Failed to create package file '{package_file}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
