def get_github_repo_url(username, repo_name):
    """Construct the URL to the GitHub repository."""
    github_url = f"https://github.com/{username}/{repo_name}"
    return github_url

def main():
    # Prompt the user to input the GitHub username or organization name
    username = input("Enter your GitHub username or organization name: ").strip()

    # Prompt the user to input the name of the GitHub repository
    repo_name = input("Enter the name of the GitHub repository: ").strip()

    # Get the GitHub repository URL
    repo_url = get_github_repo_url(username, repo_name)

    # Print the GitHub repository URL
    print("GitHub repository URL:")
    print(repo_url)

if __name__ == "__main__":
    main()
