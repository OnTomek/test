"""
def create_package_file(branch_name):
    filename = f"{branch_name}.package"
    with open(filename, 'w') as f:
        pass  # Create an empty file
    print(f"Empty package file '{filename}' created.")

def main():
    from test.pr_num.py import get_branch_name
    branch_name = get_branch_name()
    create_deployment_folder(branch_name)

if __name__ == "__main__":
    main()
"""


"""
import os
import sys

def create_package_file(branch_name, folder_name):
    filename = os.path.join(folder_name, f"{branch_name}.package")
    with open(filename, 'w') as f:
        pass  # Create an empty file
    print(f"Empty package file '{filename}' created.")

def main():
    from pr_num import get_branch_name, get_folder_name
    branch_name = get_branch_name()
    folder_name = get_folder_name()
    create_package_file(branch_name, folder_name)

if __name__ == "__main__":
    main()
"""