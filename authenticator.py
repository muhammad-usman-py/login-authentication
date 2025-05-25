# I WIll use decorators to make this user authenticator

from functools import wraps
import getpass
Valid_users = {
    "admin": "2555",
    "user": "1234"
}


"""Thsi will Used to resgistor new users"""
def registration():
    username = input("Enter your username: ")
    if username in Valid_users:
        print(f"❗ Username '{username}' already exists.")
        return
        
    pwd=input("Enter your password: ")
    Valid_users[username] = pwd
    print(f"✓ Registered '{username}' successfully.\nNow you can login.")
    print("-"*40)


"""This will be used to change passwords"""
def change_password():
    usernam=input("Enter user name: ")
    if usernam not in Valid_users:
        print(f"❗ User '{usernam}' not found.")
        return
    
    oldpwd=input("Enter old password: ")
    if Valid_users[usernam]!=oldpwd:
        print(f"❗ Old password is incorrect.")
        return
    newpwd=input("Enter new password: ")
    Valid_users[usernam]=newpwd
    print("✓ Password changed successfully.")
    print("-"*40)

"""This will be use to validate user"""
def aunthenticator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        

        for _ in range(3):
            username = input("Username: ")
            password = input("Password: ")
            if Valid_users.get(username)==password:
                print("Aunthertication Successfull")
                return func(*args,**kwargs)
            print("Aunthertication Failed")
        print("Too many attempts, Try again")
        print("-"*40)
    return wrapper

@aunthenticator
def view_dashboard():
    print("Welcome to the admin dashboard.")
    
    print("Its a dummy dashboard for now.\n")
    print("-"*40)

while True:
    print("1. New User? Register Yourself")
    print("2. Change Password")
    print("3. Login to Dashboard")
    print("4. Exit")
    print("-"*40)
    
    choice = input("Enter your choice: ")
    if choice == "1":
        registration()
    elif choice == "2":
        change_password()
    elif choice == "3":
        view_dashboard()
    elif choice == "4":
        print("👋 Goodbye!")

        break
    else:
        print("❗ Invalid choice. Please enter 1, 2, 3, or 4.\n")
        
