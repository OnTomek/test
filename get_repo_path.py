import os

def get_repo_path(base_dir, repo_name):
    """Construct the path to the local repository."""
    # Construct the full path to the repository
    repo_path = os.path.join(base_dir, repo_name)
    return repo_path

def main():
    # Fixed part of the path
    fixed_base = os.path.sep  # This represents the root of the file system

    # Prompt the user to input the base directory where repositories are located
    base_dir = input("Enter the base directory: ").strip()

    # Print the base directory for debugging
    print(f"Base directory: '{base_dir}'")

    # Prompt the user to input the name of the repository
    repo_name = input("Enter the name of the repository: ").strip()

    # Print the repository name for debugging
    print(f"Repository name: '{repo_name}'")

    # Get the path to the repository
    repo_path = get_repo_path(os.path.join(fixed_base, base_dir), repo_name)

    # Print the path to the repository
    print("Constructed path to the local repository:")
    print(repo_path)

    # Check if the constructed repository path exists
    if not os.path.isdir(repo_path):
        print(f"The repository path '{repo_path}' does not exist.")
    else:
        print(f"The repository path '{repo_path}' exists.")

if __name__ == "__main__":
    main()
