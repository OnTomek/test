# Pull Request Merger

- This [script](github_merger.py) is for merging an additional branch and the master branch with the help of a pull request number and API.
  First of all it creates a folder on a constant path to a local repository, with the desired branch name of the branch you want to merge with master.
  Then in the folder it creates an empty .package file also with the desired branch name and last but not least it merges the two branches together on github.

## Project Requirements

- Here we need requests, git library to be installed.
```python
def merge_pull_request(pull_request_number):
    github_token = os.getenv("GITHUB_TOKEN")
```

- Update this with your GitHub username or organization name and repository name.
```python
repo_owner = "OnTomek"
repo_name = "test"
```

- Update this with the path to your local repository and the name of your main branch.
```python
repo_path = "C:/temp/test"
main_branch = "main"
```

## How to Use the tool
- Example of the usage, e.g.  python github_merger.py <pr number>



- Example output
