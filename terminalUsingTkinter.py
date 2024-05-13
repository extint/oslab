import tkinter as tk
from tkinter import ttk
import subprocess
import os
from os.path import join, expanduser


global history
# history=[]

def run_command(command):
    if command=='history':
        with open(join(expanduser('~'), '.bash_history'), 'r') as f:
            for line in f:  
                Command_output.insert(tk.END, f"$ {line}\n")
    else :
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
        Command_output.insert(tk.END, f"$ {command}\n")
        Command_output.insert(tk.END, result.stdout)
        Command_output.insert(tk.END, result.stderr)
# def prevCommand(event=None):
#     if len(history):
#         # print(history_index)
#         # if(history_index>-1):
#         comm = history[history_index-1]
#         history_index-=1
#         command_input.insert(tk.END, comm)
def execute_command(event=None):
    command = command_input.get("1.0", tk.END).strip()

    if command.startswith("cd "):
        new_directory = command[3:]
        try:
            os.chdir(new_directory)
        except FileNotFoundError:
            Command_output.insert(tk.END, f"Directory not found: {new_directory}\n")
    elif command.startswith("clear"):
        Command_output.delete(1.0, tk.END)
    else:
        run_command(command)

    command_input.delete("1.0", tk.END)

root = tk.Tk()
root.title("Command GUI")

# Input 
command_input = tk.Text(root, height=1, width=80, bg="black", fg="white", insertbackground="white", font=("Courier", 10))
command_input.pack(pady=1, padx=10)
command_input.bind('<Return>', execute_command)
# command_input.bind('<Up>', prevCommand)

# Output 
Command_output = tk.Text(root, height=20, width=80, bg="purple", fg="white", insertbackground="white", font=("Courier", 10))
Command_output.pack(pady=0, padx=10)
Command_output.insert(tk.END, "")


root.mainloop()
