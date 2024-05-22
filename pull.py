import os
import subprocess

def run_command(command, cwd=None):
    """Run a shell command and print the output."""
    result = subprocess.run(command, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Command failed with error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

def main():
    # Change to the repository directory
    repo_path = input("Enter the path to the local repository: ").strip()
    os.chdir(repo_path)

    # Pull main branch
    print("Pulling main branch...")
    if run_command("git checkout main") != 0:
        print("Failed to checkout main branch.")
        return

    if run_command("git pull origin main") != 0:
        print("Failed to pull main branch.")
        return

    # Pull another branch
    branch_name = input("Enter the name of the branch to pull: ").strip()
    print(f"Pulling branch '{branch_name}'...")
    if run_command(f"git checkout {branch_name}") != 0:
        print(f"Failed to checkout branch '{branch_name}'.")
        return

    if run_command(f"git pull origin {branch_name}") != 0:
        print(f"Failed to pull branch '{branch_name}'.")
        return

    print("Pull operation completed successfully.")

if __name__ == "__main__":
    main()
