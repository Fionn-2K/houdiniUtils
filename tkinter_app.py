import os
import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import Scrollbar
from tkinter import ttk

WINDOW_COLOUR = "#212121"
TEXTFIELD_COLOUR = "#5c5c5c"
TEXT_COLOUR = "#ffffff"
BUTTON_COLOUR = "#1f4294"

class MyGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("My tkinter App")
        self.window.geometry("500x500")
        self.window.config(bg=WINDOW_COLOUR)
        self.window.resizable(width=False, height=False)
        self.textfield_font = font.Font(slant="italic", size=12)

        # Browse frame
        self.main_frame = tk.Frame(self.window, bg=WINDOW_COLOUR, highlightbackground="black", highlightthickness=0, relief=tk.RIDGE, bd=0)
        self.main_frame.pack(padx=10, pady=10, fill="x")
        # Define frame grid
        self.main_frame.columnconfigure(0, weight=0)
        self.main_frame.columnconfigure(1, weight=10)
        self.main_frame.columnconfigure(2, weight=0)
        self.main_frame.columnconfigure(3, weight=0)
        #Row: Label | Entry | Button
        browse_label = tk.Label(self.main_frame, bg=WINDOW_COLOUR, fg=TEXT_COLOUR, text="Folder Path", bd=0, font=("normal", 12))
        browse_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.browse_entry = tk.Entry(self.main_frame,bg=TEXTFIELD_COLOUR, fg=TEXT_COLOUR)
        self.browse_entry.bind("<KeyPress>", self.list_from_entry)
        self.browse_entry.grid(row=0, column=1, padx=5, sticky=tk.W + tk.E)
        browse_button = tk.Button(self.main_frame, width=6, text="Browse", bg=BUTTON_COLOUR, fg=TEXT_COLOUR, font=('normal', 12), command=self.browse_folder)
        browse_button.grid(row=0, column=2, sticky=tk.E, padx=2.5, pady=5)
        list_button = tk.Button(self.main_frame, width=6, text="List", bg=BUTTON_COLOUR, fg=TEXT_COLOUR, font=('normal', 12), command=self.show_files_as_list)
        list_button.grid(row=0, column=3, sticky=tk.E, padx=2.5, pady=5)

        # Directory - LabelFrame [ListBox/TreeView]
        dir_frame = tk.LabelFrame(self.window, text="Directory Lists", bg=WINDOW_COLOUR, fg=TEXT_COLOUR)
        dir_frame.pack(fill="both", expand=1, padx=5, pady=5)
        list_frame_1 = tk.Frame(dir_frame, bg=WINDOW_COLOUR)
        list_frame_1.pack(fill="both", expand=1)
        list_frame_2 = tk.Frame(dir_frame, bg=WINDOW_COLOUR)
        list_frame_2.pack(fill="both", expand=1)
        self.dir_list = tk.Listbox(list_frame_1, bg=TEXTFIELD_COLOUR, fg=TEXT_COLOUR)
        self.dir_list.pack(side="left", fill="both", expand=1, padx=10, pady=10)
        listbox_scrollbar = tk.Scrollbar(list_frame_1, orient=tk.VERTICAL)
        listbox_scrollbar.config(command=self.dir_list.yview)
        listbox_scrollbar.pack(side="right",fill="y")
        treeview_style = ttk.Style()
        treeview_style.theme_use("clam")
        # treeview_style.configure("My.TreeView", background="black", foreground="white")
        self.dir_treeview = ttk.Treeview(list_frame_2)
        self.dir_treeview.heading("#0", text="Directory Tree", anchor=tk.W)
        self.dir_treeview.pack(fill="both", expand=1, padx=10, pady=10)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    ## Open file explorer
    def browse_folder(self):
        self.browse_entry.delete(0, tk.END)
        self.browse_entry.insert(0, filedialog.askdirectory())
        if len(self.browse_entry.get()) > 0:
            self.show_files_as_list()

    ## Run show_files_as_list when return key presses in browser_entry field
    def list_from_entry(self, event):
        if event.keysym == "Return":
            self.show_files_as_list()

    ## Show files from selected directory as ListView and ListTree
    def show_files_as_list(self):
        if len(self.browse_entry.get()) == 0:
            self.browse_folder()
        else:
            try:
                self.clear_list()
                input_dir = self.browse_entry.get()
                all_files = [file for file in os.listdir(input_dir)]

                tree_root = input_dir
                tree_root = tree_root.split("/")[-1]
                self.dir_treeview.insert('', tk.END, text=tree_root, iid=0, open=True) ## TreeView root

                for index, file in enumerate(all_files):
                    self.dir_list.insert(index, file)

                    #/ TreeView
                    self.dir_treeview.insert('', tk.END, text=file, iid=index + 1, open=False)
                    self.dir_treeview.move(index + 1, 0, index)

                    ##TODO: implement a full TreeView for folder, sub-folders and files
                    # file_path = self.browse_entry.get() + "/" + file
                    # if os.path.isdir(file_path):
                    #     self.dir_treeview.insert('', tk.END, text=file, iid=index+1, open=False)
                    #     self.dir_treeview.move(index+1, 0, index)
                    #     print(f"{file} is a directory folder")
                    # else:
                    #     print(f"{file} is not a directory")
                    #     # self.dir_treeview.insert('', tk.END, text=file, iid=index, open=False)
                    #     # self.dir_treeview.move(index,)

            except FileNotFoundError:
                messagebox.showinfo(title="Entry field", message="No folder selected. Please try again.")

    ## Aysnc IO?
    def clear_list(self):
        self.dir_list.delete(0, tk.END)
        for item in self.dir_treeview.get_children():
            self.dir_treeview.delete(item)

    ## When closing application
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
            self.window.destroy()

if __name__ == "__main__":
    my_app_window = MyGUI()