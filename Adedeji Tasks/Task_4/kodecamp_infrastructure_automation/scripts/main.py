import os
from create_dir import setup_directories, create_directories #module from create_dir script
from create_user_and_group import create_users               #module from create_user_and_group script

# create a file in a valid company directory
def create_file_in_directory(file_name, directory, company_directories):
    if directory in company_directories:
        file_path = os.path.join(directory, file_name)    
        with open(file_path, 'w') as file:
            file.write("")  # Create an empty file
        print(f"File {file_name} created in {directory}.")
        
    else:
        print(f"Directory {directory} is not a valid company directory.")

def main():
    # Create users
    create_users()

    # Create directories
company_directories = [
        "Finance Budgets",
        "Contract Documents",
        "Business Projections",
        "Business Models",
        "Employee Data",
        "Company Vision and Mission Statement",
        "Server Configuration Script"
    ]
setup_directories()

    # Get user input for file creation
file_name = input("Enter the name of the file: ")

# a loop for the user to keep trying if the wrong directory is provided
directory = ""
while directory not in company_directories:
        directory = input("Enter the directory to create the file in: ").strip().title()
        if directory not in company_directories:
            print(f"Directory {directory} is not a valid company directory. Please try again!")

create_file_in_directory(file_name, directory, company_directories)

if __name__ == "__main__":
    main()
