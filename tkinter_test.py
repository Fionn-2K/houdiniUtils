from tkinter import *
from tkinter import filedialog
import  zipfile
import os
import sys
import glob
import pandas as pd

THEME_COLOUR = "#444953"
SEARCH_FILE_TYPE = "*.obj"

class MyInterface():
    def __init__(self):
        self.window = Tk() # will close immediately if no value is given
        self.window.title("test")
        self.window.config(padx=20, pady=20, bg=THEME_COLOUR)

        self.opened_dir = None
        self.zip_files = None

        self.folder_name_label = Label(text="Select Folder: ", bg=THEME_COLOUR, fg="white")
        self.folder_name_label.grid(row=0, column=1)

        ## Open Button
        self.open_btn_image = PhotoImage(file="images/button.png")
        self.openDir_btn = Button(bg=THEME_COLOUR, image=self.open_btn_image, bd=0, highlightbackground=THEME_COLOUR, highlightthickness=0) #, command=self.openDirectory
        self.openDir_btn.grid(row=1, column=1)

        ## Central canvas
        self.central_canvas = Canvas(width=200, height=200, highlightthickness=0,bg="white")
        self.central_text = self.central_canvas.create_text(150, 75, width=200, text="", fill="#000000",font=("Arial", 20, "italic"))
        self.central_canvas.grid(row=2, column=0, columnspan=3, pady=50)

        ## unzip button
        self.unzip_btn_image = PhotoImage(file="images/button_unzip.png")
        self.unzip_btn = Button(image=self.unzip_btn_image, bd=0, highlightthickness=0, bg=THEME_COLOUR) #, command=self.unzipAllBtn
        self.unzip_btn.grid(row=5, column=1)

        ## csv export
        self.csv_btn_image = PhotoImage(file="images/button_csv.png")
        self.csv_btn = Button(image=self.csv_btn_image, bd=0, highlightthickness=0, bg=THEME_COLOUR) #, command=self.exportCsv
        self.csv_btn.grid(row=6, column=1)

        ## delete button
        self.delete_btn_image = PhotoImage(file="images/button_delete.png")
        self.delete_btn = Button(image=self.delete_btn_image, bd=0, highlightthickness=0, bg=THEME_COLOUR)#, command=self.deleteZipFiles
        self.delete_btn.grid(row=7, column=1)

        self.window.mainloop()

if __name__ == "__main__":
    ui = MyInterface()