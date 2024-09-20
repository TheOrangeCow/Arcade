import tkinter as tk
from tkinter import ttk
import time
from home import main

def hash(input_string):
    hash_value = 0
    for char in input_string:
        hash_value += ord(char) 
    return hash_value

def signup():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "" or password == "":
        signup_status.config(text="Please enter both username and password", foreground="red")
        return
    
    hashed_password = hash(password)
    
    with open("users.txt", "a") as file:
        file.write(f"{username}:{hashed_password}\n")
    
    signup_status.config(text="Signup successful", foreground="green")

def login():
    global root
    username = username_entry.get()
    password = password_entry.get()
    
    with open("users.txt", "r") as file:
        users = file.readlines()
    
    for user in users:
        stored_username, stored_password = user.strip().split(":")
        if username == stored_username and hash(password) == int(stored_password):
            with open("logged_in_users.txt", "w") as file:
                file.write(username)
            login_status.config(text="Login successful", foreground="green")
            time.sleep(0.5)
            root.destroy()
            main()
            return
    
    login_status.config(text="Invalid username or password", foreground="red")

root = tk.Tk()
root.title("Login")
ttk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)
ttk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
password_entry = ttk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)
signup_btn = ttk.Button(root, text="Sign Up", command=signup)
signup_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="we")
login_btn = ttk.Button(root, text="Login", command=login)
login_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")
signup_status = ttk.Label(root, text="", foreground="red")
signup_status.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")
login_status = ttk.Label(root, text="")
login_status.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")

root.mainloop()
