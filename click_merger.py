import os
import requests
import click
from pathlib import Path
from git import Repo

@click.command()
@click.option('--owner', type=str, required=True, help='Owner of the GitHub repository')
@click.option('--repo', type=str, required=True, help='Name of the GitHub repository')
@click.option('--path', type=click.Path(exists=True, path_type=Path), required=True, help='Local path to the repository')
@click.option('--main', type=str, required=True, help='Main branch of the repository')
@click.argument('pr_num', type=int)
def main(owner, repo, path, main, pr_num):
    """Script to merge a GitHub pull request and create a deployment package."""
    
    def create_deployment_folder(branch_name):
        """Function creates folder on a constant path."""
        try:
            folder_path = Path("C:/temp/deployment_package") / branch_name.replace("/", "_")
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"Created folder: {folder_path}")
            return folder_path
        except OSError as e:
            print(f"Failed to create folder: {e}")
            return None

    def pull_and_merge(repo_path, main_branch, other_branch):
        """Merges the pull request locally."""
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
        """Function creating package file."""
        try:
            file_path = folder_path / f"{branch_name.replace('/', '_')}.package"
            file_path.write_text(f"Package for branch: {branch_name}", encoding="utf-8")
            print(f"Created package file: {file_path}")
        except OSError as e:
            print(f"Failed to create package file: {e}")

    def get_branch_name(owner, repo, pr_num):
        """Function gets the branch name from pull request."""
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
            return None

        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_num}"

        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()
            branch_name = data['head']['ref']
            return branch_name
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve pull request information: {e}")
            return None

    branch_name = get_branch_name(owner, repo, pr_num)
    if branch_name:
        folder_path = create_deployment_folder(branch_name)
        if folder_path:
            pull_and_merge(path, main, branch_name)
            create_package_file(folder_path, branch_name)
        else:
            print("Failed to create deployment folder.")
    else:
        print("Unable to retrieve branch name from the pull request.")

if __name__ == "__main__":
    main()
