import os

def get_repo_path(repo_name):
    """Construct the path to the local repository."""
    # Get the current directory
    current_dir = os.getcwd()

    # Construct the path to the repository
    repo_path = os.path.join(current_dir, repo_name)

    return repo_path

def main():
    # Prompt the user to input the name of the repository
    repo_name = input("Enter the name of the repository: ").strip()

    # Get the path to the repository
    repo_path = get_repo_path(repo_name)

    # Print the path to the repository
    print("Path to the local repository:")
    print(repo_path)

if __name__ == "__main__":
    main()
