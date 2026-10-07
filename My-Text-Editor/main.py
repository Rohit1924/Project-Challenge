## tkinter module and library
import tkinter as tk
from tkinter import filedialog, messagebox


# Main window
root = tk.Tk()
root.title("My Text Editor")
root.geometry("800x700")


# Create text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 18)
)
text.pack(expand=True, fill=tk.BOTH)


##  MAIN LOGIC 

# Function 1 - Create a new file
def new_file():
    text.delete(1.0, tk.END)


# Function 2 - Open a file
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Text file", "*.txt"),
            ("All files", "*.*")
        ]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text.delete(1.0, tk.END)
                text.insert(tk.END, file.read())

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Could not open file:\n{e}"
            )


# Function 3 - Save a file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[
            ("Text file", "*.txt"),
            ("All files", "*.*")
        ]
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text.get(1.0, tk.END))

            messagebox.showinfo(
                "Info",
                "File saved successfully!"
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Could not save file:\n{e}"
            )


##  EDIT FUNCTIONS 

# Undo
def undo():
    try:
        text.edit_undo()
    except tk.TclError:
        pass


# Redo
def redo():
    try:
        text.edit_redo()
    except tk.TclError:
        pass


# Cut
def cut():
    text.event_generate("<<Cut>>")


# Copy
def copy():
    text.event_generate("<<Copy>>")


# Paste
def paste():
    text.event_generate("<<Paste>>")


# Select All
def select_all():
    text.tag_add("sel", "1.0", tk.END)


# Delete selected text
def delete_text():
    try:
        text.delete("sel.first", "sel.last")
    except tk.TclError:
        pass


##  VIEW FUNCTIONS 

# Zoom In
def zoom_in():
    current_font = text.cget("font")
    font_size = int(current_font.split()[-1])
    text.config(font=("Helvetica", font_size + 2))


# Zoom Out
def zoom_out():
    current_font = text.cget("font")
    font_size = int(current_font.split()[-1])

    if font_size > 6:
        text.config(font=("Helvetica", font_size - 2))


# Reset Zoom
def reset_zoom():
    text.config(font=("Helvetica", 18))


## MENU 

menu = tk.Menu(root)
root.configure(menu=menu)


#  FILE MENU 

file_menu = tk.Menu(menu, tearoff=0)

menu.add_cascade(
    label="File",
    menu=file_menu
)

file_menu.add_command(
    label="New",
    command=new_file
)

file_menu.add_command(
    label="Open",
    command=open_file
)

file_menu.add_command(
    label="Save",
    command=save_file
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=root.quit
)


#  EDIT MENU 

edit_menu = tk.Menu(menu, tearoff=0)

menu.add_cascade(
    label="Edit",
    menu=edit_menu
)

edit_menu.add_command(
    label="Undo",
    command=undo
)

edit_menu.add_command(
    label="Redo",
    command=redo
)

edit_menu.add_separator()

edit_menu.add_command(
    label="Cut",
    command=cut
)

edit_menu.add_command(
    label="Copy",
    command=copy
)

edit_menu.add_command(
    label="Paste",
    command=paste
)

edit_menu.add_separator()

edit_menu.add_command(
    label="Select All",
    command=select_all
)

edit_menu.add_command(
    label="Delete",
    command=delete_text
)


## VIEW MENU 

view_menu = tk.Menu(menu, tearoff=0)

menu.add_cascade(
    label="View",
    menu=view_menu
)

view_menu.add_command(
    label="Zoom In",
    command=zoom_in
)

view_menu.add_command(
    label="Zoom Out",
    command=zoom_out
)

view_menu.add_command(
    label="Reset Zoom",
    command=reset_zoom
)


# Run application
root.mainloop()