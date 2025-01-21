import tkinter as tk
import os
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        print(f"Selected file: {os.path.basename(file_path)}")
        root.title(os.path.basename(file_path))

# main window
root = tk.Tk()
root.title("File")
root.geometry("300x150")

# Button to open file location
open_button = tk.Button(root, text="Open Text File", command=open_file)
open_button.pack(pady=50)

root.mainloop()
