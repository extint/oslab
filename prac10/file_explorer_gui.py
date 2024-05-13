import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import subprocess

class FileSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File System Organiser")
        self.current_dir = os.getcwd()
        self.setup_gui()

    def setup_gui(self):
        self.root.configure(bg="orange")  # Set background color of root window

        path_frame = tk.Frame(self.root, bg="white")  # Frame for path display
        path_frame.pack(pady=10, fill=tk.X)

        path_label = tk.Label(path_frame, text="Current Directory:", bg="white", fg="black")  # Label for path display
        path_label.pack(side=tk.LEFT, padx=10)

        self.path_entry = tk.Entry(path_frame, width=50, bg="white", fg="black")  # Entry for path display
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, padx=10)
        self.path_entry.insert(0, self.current_dir)

        button_frame = tk.Frame(self.root, bg="white")  # Frame for buttons
        button_frame.pack(pady=10)

        create_dir_button = tk.Button(button_frame, text="Create Directory", command=self.create_directory, bg="blue", fg="white")  # Button to create directory
        create_dir_button.pack(side=tk.LEFT, padx=10)
        # utton(button_frame, text="Create Directory", command=self.create_directory, bg="blue", fg="white")  # Button to create directory
        # create_dir_button.pack(side

        create_file_button = tk.Button(button_frame, text="Create File", command=self.create_file, bg="blue", fg="white")  # Button to create file
        create_file_button.pack(side=tk.LEFT, padx=10)

        edit_file_button = tk.Button(button_frame, text="Edit File", command=self.edit_file, bg="blue", fg="white")  # Button to edit file
        edit_file_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(button_frame, text="Delete", command=self.delete_item, bg="red", fg="white")  # Button to delete item
        delete_button.pack(side=tk.LEFT, padx=10)

        delete_dir_button = tk.Button(button_frame, text="Delete Directory", command=self.delete_directory, bg="red", fg="white")  # Button to delete directory
        delete_dir_button.pack(side=tk.LEFT, padx=10)
        # delete_dir_button.pack(side=tk.LEFT, padx=10)

        self.listbox = tk.Listbox(self.root, width=70, height=20, bg="white", fg="black")  # Listbox to display files and directories
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        self.listbox.bind("<Double-Button-1>", self.on_double_click)

        self.populate_listbox()

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in os.listdir(self.current_dir):
            self.listbox.insert(tk.END, item)

    def create_directory(self):
        new_dir = filedialog.askdirectory(initialdir=self.current_dir, title="Create New Folder")
        if new_dir:
            try:
                os.makedirs(new_dir)
                messagebox.showinfo("Success", f"Directory '{new_dir}' created successfully.")
                self.populate_listbox()
            except FileExistsError:
                messagebox.showerror("Error", f"Directory '{new_dir}' already exists.")

    def create_file(self):
            selected_index = self.listbox.curselection()
            if selected_index:
                directory_name = self.listbox.get(selected_index)
            else:
                directory_name = os.getcwd()
            file_name = simpledialog.askstring("Create File", f"Enter file name in '{directory_name}':")
            # if selected_index:
            #     directory_name = self.listbox.get(selected_index)
            # else:
            #     directory_name = os.getcwd()
            # file_name = simpledialog.askstring("Create File", f"Enter file name in '{directory_name}':")
            if file_name:
                try:
                    if directory_name:
                        with open(os.path.join(directory_name, file_name), 'w'):
                            pass
                    else:
                        directory_name = os.getcwd()
                        with open(os.path.join(directory_name, file_name), 'w'):
                            pass
                    messagebox.showinfo("Success", f"File '{file_name}' created successfully in '{directory_name}'.")
                    self.populate_listbox()
                except OSError as e:
                    messagebox.showerror("Error", f"Failed to create file: {e}")

    def edit_file(self):
        selected_file = self.listbox.get(tk.ACTIVE)
        if selected_file:
            file_path = os.path.join(self.current_dir, selected_file)
            try:
                subprocess.Popen(['gedit', file_path])
            except FileNotFoundError:
                messagebox.showerror("Error", "Gedit is not installed on this system.")
        else:
            messagebox.showwarning("Warning", "Please select a file to edit.")

    def delete_item(self):
        selected_item = self.listbox.get(tk.ACTIVE)
        if selected_item:
            item_path = os.path.join(self.current_dir, selected_item)
            if os.path.isfile(item_path):
                os.remove(item_path)
                messagebox.showinfo("Success", f"File '{selected_item}' deleted successfully.")
            elif os.path.isdir(item_path):
                try:
                    self.recursive_delete(item_path)
                    messagebox.showinfo("Success", f"Directory '{selected_item}' deleted successfully.")
                except OSError:
                    messagebox.showerror("Error", f"Directory '{selected_item}' is not empty or does not exist.")
                #      try:
                #     self.recursive_delete(item_path)
                #     messagebox.showinfo("Success", f"Directory '{selected_item}' deleted successfully.")
                # except OSError:
                #     messagebox.showerror("Error", f"Directory '{selected_item}' is not empty or does not exist.")
            self.populate_listbox()
        else:
            messagebox.showwarning("Warning", "Please select an item to delete.")

    def delete_directory(self):
        selected_item = self.listbox.get(tk.ACTIVE)
        if selected_item:
            item_path = os.path.join(self.current_dir, selected_item)
            try:
                os.remove(item_path)
                messagebox.showinfo("Success", f"Directory '{selected_item}' deleted successfully.")
                self.populate_listbox()  
            except OSError:
                messagebox.showerror("Error", f"Directory '{selected_item}' is not empty or does not exist.")
        else:
            messagebox.showwarning("Warning", "Please select a directory to delete.")

    def recursive_delete(self, dir_path):
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                self.recursive_delete(file_path)
        os.rmdir(dir_path)

    def on_double_click(self):
        selection = self.listbox.curselection()
        if selection:
            selected_item = self.listbox.get(selection)
            item_path = os.path.join(self.current_dir, selected_item)
            if os.path.isdir(item_path):
                self.current_dir = item_path
                self.path_entry.delete(0, tk.END)
                self.path_entry.insert(0, self.current_dir)
                self.populate_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSystemGUI(root)
    root.mainloop()


