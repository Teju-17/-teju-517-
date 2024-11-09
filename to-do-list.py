                                #Task - 1 (#CODESOFT - PYTHON PROGRAMMING INTERNSHIP)
import tkinter as tk
from tkinter import messagebox
task_frames = []
def Add_task():
    task = entry_box.get()
    if task.strip():
        task_frame = tk.Frame(task_container)
        task_frame.pack(fill="x", pady=5)
        task_label = tk.Label(task_frame, text=task, font=('Arial', 12), anchor="w", width=30)
        task_label.pack(side="left", padx=5)
        delete_button = tk.Button(task_frame, text="Delete", command=lambda: delete_task(task_frame))
        delete_button.pack(side="right", padx=5)
        task_frames.append(task_frame)
        entry_box.delete(0, tk.END)  
    else:
        messagebox.showwarning("Input Error", "Please enter a valid task.")
def delete_task(task_frame):
    task_frame.destroy()
    task_frames.remove(task_frame)

root = tk.Tk()
root.geometry("400x300")
root.title("Task-Manager")
entry_box = tk.Entry(root, width=40, font=('Arial', 12))
entry_box.pack(pady=10)
submit_button = tk.Button(root, text="Add Task", command=Add_task)
submit_button.pack(pady=5)
task_container = tk.Frame(root)
task_container.pack(fill="both", expand=True, pady=10)
root.mainloop()