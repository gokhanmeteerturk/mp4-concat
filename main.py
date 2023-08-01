import os
import tkinter as tk
from tkinter import filedialog, ttk
import subprocess

import sv_ttk

import pywinstyles


def browse_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("MP4 Files", "*.mp4")])
    for file_path in file_paths:
        if file_path not in selected_files:
            selected_files.append(file_path)
            listbox.insert(tk.END, os.path.basename(file_path))

def move_up():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        if index > 0:
            selected_files[index], selected_files[index - 1] = selected_files[index - 1], selected_files[index]
            update_listbox()

def move_down():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        if index < len(selected_files) - 1:
            selected_files[index], selected_files[index + 1] = selected_files[index + 1], selected_files[index]
            update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for file_path in selected_files:
        listbox.insert(tk.END, os.path.basename(file_path))

def merge_files():
    output_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 File", "*.mp4")])
    if output_file:
        # Create a temporary text file to store the list of video files
        temp_list_file = "temp_list.txt"
        with open(temp_list_file, "w") as f:
            for file_path in selected_files:
                f.write(f"file '{file_path}'\n")
        # Use ffmpeg to concatenate the video files using the temporary list file
        cmd = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', temp_list_file, '-c', 'copy', output_file]
        subprocess.run(cmd)
        # Clean up the temporary list file
        os.remove(temp_list_file)


selected_files = []

root = tk.Tk()
root.title("MP4 File Merger")
root.geometry("300x400")

frame = tk.Frame(root)
frame.pack()

btn_browse = ttk.Button(frame, text="Browse Files", command=browse_files)
btn_browse.pack(padx=8, pady=8)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, )
listbox.pack(pady=8)

frame2 = tk.Frame(root)
frame2.pack()
btn_up = ttk.Button(frame2, text="UP", command=move_up)
btn_up.pack(side=tk.LEFT, padx=2, pady=8)

btn_down = ttk.Button(frame2, text="DOWN", command=move_down)
btn_down.pack(side=tk.LEFT, padx=2, pady=8)

btn_merge = ttk.Button(root, text="Merge", command=merge_files)
btn_merge.pack(pady=12)

root.resizable(False,False)
sv_ttk.set_theme("dark")

pywinstyles.apply_style(root, "mica")

root.mainloop()
