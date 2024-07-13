import tkinter as tk
from tkinter import messagebox
import sqlite3
import cgpaaaaaa
import student


# Function to create login page
def main():

    # Create a database connection
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS marks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER NOT NULL,
                        semester INTEGER NOT NULL,
                        subject TEXT NOT NULL,
                        marks INTEGER NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS sgpa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id INTEGER NOT NULL,
                        semester INTEGER NOT NULL,
                        sgpa REAL NOT NULL)''')

    # Insert default staff and student data for testing
    cursor.execute("INSERT OR IGNORE INTO students (username, password, role) VALUES (?, ?, ?)", ("staff", "staff_password", "staff"))
    cursor.execute("INSERT OR IGNORE INTO students (username, password, role) VALUES (?, ?, ?)", ("student1", "student1_password", "student"))
    cursor.execute("INSERT OR IGNORE INTO students (username, password, role) VALUES (?, ?, ?)", ("student2", "student2_password", "student"))

    conn.commit()
    login_window = tk.Tk()
    login_window.title("Login")
    
    # Function to handle login button click
    def login():
        username = username_entry.get()
        password = password_entry.get()
        
        # Check if the user exists in the database
        cursor.execute("SELECT * FROM students WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        
        if user:
            role = user[3]
            if role == "student":
                login_window.destroy()
                cursor.close()
                conn.close()
                student_dashboard(username)
            elif role == "staff":
                login_window.destroy()
                cursor.close()
                conn.close()
                staff_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    # Create login form elements
    username_label = tk.Label(login_window, text="Username:")
    username_label.pack()
    
    username_entry = tk.Entry(login_window)
    username_entry.pack()
    
    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()
    
    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack()
    
    login_window.mainloop()

def student_dashboard(username):
    student.main(username)


def staff_dashboard():
    cgpaaaaaa.main()

if __name__ == "__main__":
    main()
