# 🔐 Python User Authentication System

This project demonstrates a simple command-line user authentication system in Python, featuring user registration, password management, and access control using decorators.

## ✨ Features

- 🧾 **User Registration:** Register new users with a unique username and password.
- 🔑 **Password Change:** Securely update an existing user's password.
- 🔐 **Login Authentication:** Validate credentials before accessing protected features.
- 🛡 **Decorator-Based Protection:** Use decorators to enforce login on sensitive functions.

## 🧠 Code Overview

```python
from functools import wraps
import getpass

Valid_users = {
    "admin": "2555",
    "user": "1234"
}

def registration():
    username = input("Enter your username: ")
    if username in Valid_users:
        print(f"❗ Username '{username}' already exists.")
        return

    pwd = input("Enter your password: ")
    Valid_users[username] = pwd
    print(f"✓ Registered '{username}' successfully.\nNow you can login.")
    print("-" * 40)

def change_password():
    usernam = input("Enter user name: ")
    if usernam not in Valid_users:
        print(f"❗ User '{usernam}' not found.")
        return

    oldpwd = input("Enter old password: ")
    if Valid_users[usernam] != oldpwd:
        print("❗ Old password is incorrect.")
        return

    newpwd = input("Enter new password: ")
    Valid_users[usernam] = newpwd
    print("✓ Password changed successfully.")
    print("-" * 40)

def aunthenticator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for _ in range(3):
            username = input("Username: ")
            password = input("Password: ")
            if Valid_users.get(username) == password:
                print("Authentication Successful")
                return func(*args, **kwargs)
            print("Authentication Failed")
        print("Too many attempts, Try again")
        print("-" * 40)
    return wrapper

@aunthenticator
def view_dashboard():
    print("Welcome to the admin dashboard.")
    print("Its a dummy dashboard for now.\n")
    print("-" * 40)

if __name__ == "__main__":
    while True:
        print("1. New User? Register Yourself")
        print("2. Change Password")
        print("3. Login to Dashboard")
        print("4. Exit")
        print("-" * 40)

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
```

## ▶️ Usage

1. 🛠 **Clone the Repository**
   ```bash
   git clone https://github.com/muhammad-usman-py/user-auth-system.git
   cd user-auth-system
   ```

2. 🚀 **Run the Script**
   ```bash
   python user_auth_system.py
   ```

3. 📋 **Interact with Menu Options:**
   - Register a new user
   - Change existing password
   - Authenticate and access dashboard
   - Exit the app

## 🤝 Contributing

Contributions are welcome! Open issues or submit pull requests for improvements or new features.

## 📄 License

This project is licensed under the MIT License.

---

💻 *Created by Muhammad Usman*
