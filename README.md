[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

# Pull Request Merger

- This [script](github_merger.py) is for merging an additional branch and the master branch with the help of a pull request number and API.
  First of all it creates a folder on a constant path to a local repository, with the desired branch name of the branch you want to merge with main/master.
  Then in the folder it creates an empty .package file also with the desired branch name and last but not least it merges the two branches together on github.

## Project Requirements
[requirements](requirements.txt)
- For this part of code we need to install *requests* git library.
```python
def merge_pull_request(pull_request_number):
    github_token = os.getenv("GITHUB_TOKEN")
```

```
pip install requests
```
- Update this with your GitHub username or organization name, repository name, path to your local repository and the name of your main/master branch.

```python
REPO_OWNER = "your_username"
REPO_NAME = "your_repository_name"
REPO_PATH = "C:/your_local_path"
MAIN_BRANCH = "your_main_branch"
```

## How to Use the tool
- Example input
```
$ python github_merger.py
Usage: python github_merger.py <pull_request_number>
$ python github_merger.py 10
```
- Example output
```
Created folder: C:\your_local_path\feature
Pulled and merged changes from feature into main
Created package file: C:\your_local_path\feature\feature.package
```
