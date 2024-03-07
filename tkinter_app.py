import os
import tkinter as tk
from tkinter import filedialog
from tkinter import font


class MyGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("My tkinter App")
        self.window.geometry("500x500")
        self.window.resizable(width=False, height=False)
        self.textfield_font = font.Font(slant="italic", size=12)

        # Browse frame
        self.main_frame = tk.Frame(self.window, highlightbackground="black", highlightthickness=0, relief=tk.RIDGE, bd=0)
        self.main_frame.pack(padx=10, pady=10, fill="x")
        # Define frame grid
        self.main_frame.columnconfigure(0, weight=0)
        self.main_frame.columnconfigure(1, weight=10)
        self.main_frame.columnconfigure(2, weight=0)
        self.main_frame.columnconfigure(3, weight=0)
        #Row: Label | Entry | Button
        browse_label = tk.Label(self.main_frame, text="Folder Path", bd=0, font=("normal", 12))
        browse_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.browse_entry = tk.Entry(self.main_frame)
        self.browse_entry.grid(row=0, column=1, padx=5, sticky=tk.W + tk.E)
        browse_button = tk.Button(self.main_frame, width=6, text="Browse", font=('normal', 12), command=self.browse_folder)
        browse_button.grid(row=0, column=2, sticky=tk.E, padx=2.5, pady=5)
        list_button = tk.Button(self.main_frame, width=6, text="List", font=('normal', 12), command=self.show_files_as_list)
        list_button.grid(row=0, column=3, sticky=tk.E, padx=2.5, pady=5)

        # Directory - LabelFrame [ListView]
        dir_frame = tk.LabelFrame(self.window, text="Directory")
        dir_frame.pack(fill="both", expand=1, padx=5, pady=5)
        self.dir_list = tk.Listbox(dir_frame)
        self.dir_list.pack(fill="both", expand=1, padx=10, pady=10)

        self.window.mainloop()

    def browse_folder(self):
        print("Browse")
        self.browse_entry.delete(0, tk.END)
        self.browse_entry.insert(0, filedialog.askdirectory())
        if len(self.browse_entry.get()) > 0:
            self.show_files_as_list()

    def show_files_as_list(self):
        if len(self.browse_entry.get()) == 0:
            self.browse_folder()
        else:
            try:
                all_files = [file for file in os.listdir(self.browse_entry.get())]
                self.dir_list.delete(0, tk.END)
                for index, file in enumerate(all_files):
                    self.dir_list.insert(index, file)
            except FileNotFoundError:
                print("No folder selected!!") #TODO: MessageBox


if __name__ == "__main__":
    my_app_window = MyGUI()