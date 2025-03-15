import sqlite3
import os

from log_management import writing_in_log


import sqlite3

db_path = os.path.dirname(__file__)
db_path = db_path.split('gui')[0]
db_path = db_path + "\mydatabase.db"


class User:
    def __init__(self, email):
        self.email = email
        self._password = None
        self._name = None
        self._profile_picture = None
        self._admin = 0  # Default to false
        self.load_user_data()

    def load_user_data(self):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT email, password, name, profile_picture, admin FROM users WHERE email = ?", (self.email,))
        result = cursor.fetchone()

        if result:
            self._password, self._name, self._profile_picture, self._admin = result[1], result[2], result[3], bool(result[4])
        else:
            print(f"User with email {self.email} not found.")

        conn.close()

    def __repr__(self):
        return f"User(email={self.email}, name={self.name}, password={self.password}, profile_picture={self.profile_picture}, admin={self.admin})"

    # Password getter and setter
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        # Add any password validation logic here if needed
        self._password = new_password
        self._update_db_field("password", new_password)

    # Name getter and setter
    @property
    def name(self):
        return self._name if self._name else "unknown user"

    @name.setter
    def name(self, new_name):
        if not new_name or len(new_name) < 2:
            raise ValueError("Name must be at least 2 characters long.")
        self._name = new_name
        self._update_db_field("name", new_name)

    # Profile picture getter and setter
    @property
    def profile_picture(self):
        return self._profile_picture if self._profile_picture else "no_picture.png"

    @profile_picture.setter
    def profile_picture(self, new_picture):
        self._profile_picture = new_picture
        self._update_db_field("profile_picture", new_picture)

    # Admin getter and setter
    @property
    def admin(self):
        return self._admin

    @admin.setter
    def admin(self, is_admin):
        if not isinstance(is_admin, bool):
            raise ValueError("Admin must be a boolean value.")
        self._admin = is_admin
        self._update_db_field("admin", int(is_admin))

    # Update the database field
    def _update_db_field(self, field, value):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET {field} = ? WHERE email = ?", (value, self.email))
        conn.commit()
        conn.close()

    def is_admin(self):
        """Returns true if the user is an admin, false otherwise"""
        return self._admin


def remove_user_by_email(email_to_remove,admin_email):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE email = ?", (email_to_remove,))

    conn.commit()


    writing_in_log(f"User {email_to_remove} has been removed, by {admin_email}")

    conn.close()

def grant_admin(email):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET admin = 1 WHERE email = ?", (email,))
    conn.commit()
    conn.close()
    writing_in_log(f"User : {email} is now an admin.")

def un_grant_admin(email):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET admin = 0 WHERE email = ?", (email,))
    conn.commit()
    conn.close()
    writing_in_log(f"User : {email} is no longer an admin.")


def UserExist(email):
    writing_in_log(f"Checking if user : {email} exists")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

def get_user_by_name(name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT email FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        email = result[0]
        conn.close()
        return User(email)
    else:
        print(f"User with name {name} not found.")
        conn.close()
        return False


def AddUser(email, password, name, profile_picture, admin=0):
    if UserExist(email):
        print(f"User with email {email} already exists.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (email, password, name, profile_picture, admin) VALUES (?, ?, ?, ?, ?)",
                   (email, password, name, profile_picture, admin))
    conn.commit()
    conn.close()
    writing_in_log(f"User with email {email} added successfully.")
    print(f"User with email {email} added successfully.")
    return User(email)

def delete_all_users():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    writing_in_log(f"All users have been deleted")

def change_user_password(email, new_password):
    """
    Securely updates the user's password in the database.

    :param email: The user's email
    :param new_password: The new password to set
    """
    if not UserExist(email):
        writing_in_log(f"Password change failed: User {email} not found.")
        print(f"Error: User {email} not found.")
        return False

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET password = ? WHERE email = ?", (new_password, email))
    conn.commit()
    conn.close()

    writing_in_log(f"Password for user {email} has been changed successfully.")
    print(f"Password for user {email} has been changed successfully.")
    return True  # Indicating success


def get_all_users_details():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fetch all users' data from the database
    cursor.execute("SELECT email, name, profile_picture, admin FROM users")
    users = cursor.fetchall()

    if not users:
        return "No users found in the database."

    # Format the result as a nicely formatted string
    user_details = "All Users:\n"
    user_details += "-" * 50 + "\n"

    for user in users:
        email, name, profile_picture, admin = user
        admin_status = "Admin" if admin else "Regular User"

        user_details += f"Email: {email}\n"
        user_details += f"Name: {name}\n"
        user_details += f"Profile Picture: {profile_picture}\n"
        user_details += f"Role: {admin_status}\n"
        user_details += "-" * 50 + "\n"

    conn.close()
    return user_details
