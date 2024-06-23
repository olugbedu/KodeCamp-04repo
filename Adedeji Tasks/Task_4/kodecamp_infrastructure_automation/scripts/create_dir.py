import os

def create_directories(directories):
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory {directory} created.")


def setup_directories():
    company_directories = [
        "Finance Budgets",
        "Contract Documents",
        "Business Projections",
        "Business Models",
        "Employee Data",
        "Company Vision and Mission Statement",
        "Server Configuration Script"
    ]
    create_directories(company_directories)

if __name__ == "__main__":
    setup_directories()
