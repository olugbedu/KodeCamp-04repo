import subprocess

# using positional arg.
def create_user(username, group):
        subprocess.run(["sudo", "useradd", "-m", username], check=True)
        subprocess.run(["sudo", "groupadd", group], check=False)
        subprocess.run(["sudo", "usermod", "-aG", group, username], check=True)
        print(f"User {username} created and added to group {group}.")
   

def create_users():
    employees = [
        ("Andrew", "SystemAdministrator"),
        ("Julius", "Legal"),
        ("Chizi", "HumanResourceManager"),
        ("Jeniffer", "SalesManager"),
        ("Adeola", "BusinessStrategist"),
        ("Bach", "CEO"),
        ("Gozie", "ITintern"),
        ("Ogochukwu", "FinanceManager")
    ]
    for username, group in employees:
        create_user(username, group)

if __name__ == "__main__":
    create_users()
