                                #Task - 3 (#CODESOFT - PYTHON PROGRAMMING INTERNSHIP)

import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    len = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(len))
    password.set(password)
 
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")
tk.Label(root, text="Enter Password Length:").place(x=20, y=20)
length_entry = tk.Entry(root)
length_entry.place(x=180, y=20)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.place(x=150, y=60)
password_var = tk.StringVar()
tk.Label(root, text="Generated Password:").place(x=20, y=100)
password_entry = tk.Entry(root, textvariable=password_var, width=30, state='readonly')
password_entry.place(x=180, y=100)
root.mainloop()
