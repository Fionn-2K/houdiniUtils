import tkinter as tk
from tkinter import font
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Scale

BLACK_COLOUR = "#000000"
DARKER_GREY = "#141414"
DARK_GREY = "#1c1c1c"
LIGHT_GREY = "#404040"
WINDOW_COLOUR = "#00102b"

class MyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.italic_font = font.Font(slant="italic", size=18)

        self.window.title("Assignment 4")
        # self.window.attributes("-alpha", 0.5) ## Transparent
        # self.window.overrideredirect(True) ## Remove title bar
        # self.window.state("zoomed") ## Maximized at start
        self.window.geometry("500x1000")
        self.window.config(bg=DARKER_GREY)

        ## Menu bar
        self.menubar = tk.Menu(self.window)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="Close", command=self.on_closing)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Close With Question", command=exit)

        self.action_menu = tk.Menu(self.menubar, tearoff=0)
        self.action_menu.add_command(label="Show Message", command=self.showMessage)
        self.action_menu.add_separator()
        self.action_menu.add_command(label="Clear Textfield", command=self.clearTextBox)

        self.menubar.add_cascade(menu=self.file_menu, label="File")
        self.menubar.add_cascade(menu=self.action_menu, label="Action")

        self.window.config(menu=self.menubar)

        ## Label
        self.label  = tk.Label(self.window, text="My Test", font=('Bold', 20))
        self.label.pack(padx=40, pady=20)

        ## Textbox
        self.textbox = tk.Text(self.window, height=3, font=self.italic_font) # Multiline textbox. Cam scroll. height, example 3 = 3 lines high
        self.textbox.pack(padx=10, pady=10)

        ## Entry - textfield. example username/password field
        self.entry = tk.Entry(self.window)
        self.entry.pack()

        ## Button
        self.button_test = tk.Button(self.window, text="Press Me!", font=('Arial', 18), relief=tk.GROOVE) # relief styles (FLAT,RAISE,SUNKEN,GROOVE,RIDGE)
        self.button_test.pack(pady=10)

        ## Frame (Keypad) - START
        self.keypad_frame = tk.Frame(self.window)
        self.keypad_frame.columnconfigure(0, weight=1)
        self.keypad_frame.columnconfigure(1, weight=1)
        self.keypad_frame.columnconfigure(2, weight=1)

        self.button1 = tk.Button(self.keypad_frame, text="1", font=('Arial', 18))
        self.button1.grid(row=0, column=0, sticky="we") # or sticky=tk.W+tk.E

        self.button2 = tk.Button(self.keypad_frame, text="2", font=('Arial', 18))
        self.button2.grid(row=0, column=1, sticky="we") # or sticky=tk.W+tk.E

        self.button3 = tk.Button(self.keypad_frame, text="3", font=('Arial', 18))
        self.button3.grid(row=0, column=2, sticky="we") # or sticky=tk.W+tk.E

        self.button4 = tk.Button(self.keypad_frame, text="4", font=('Arial', 18))
        self.button4.grid(row=1, column=0, sticky="we") # or sticky=tk.W+tk.E

        self.button5 = tk.Button(self.keypad_frame, text="5", font=('Arial', 18))
        self.button5.grid(row=1, column=1, sticky="we") # or sticky=tk.W+tk.E

        self.button6 = tk.Button(self.keypad_frame, text="6", font=('Arial', 18))
        self.button6.grid(row=1, column=2, sticky="we") # or sticky=tk.W+tk.E

        self.button7 = tk.Button(self.keypad_frame, text="7", font=('Arial', 18))
        self.button7.grid(row=2, column=0, sticky="we") # or sticky=tk.W+tk.E

        self.button8 = tk.Button(self.keypad_frame, text="8", font=('Arial', 18))
        self.button8.grid(row=2, column=1, sticky="we") # or sticky=tk.W+tk.E

        self.button9 = tk.Button(self.keypad_frame, text="9", font=('Arial', 18))
        self.button9.grid(row=2, column=2, sticky="we") # or sticky=tk.W+tk.E

        ## Frame - END. Pack buttons into frame
        self.keypad_frame.pack(fill="x") # x = stretch left to right

        ## placed button
        self.placed_button = tk.Button(self.window, text="Placed")
        self.placed_button.place(x=350, y=50, height=50, width=100)

        ## Button with image
        self.base_image = PhotoImage(file="images/button_base.png")
        self.image_button = tk.Button(self.window, text="Image Button", bg="#000000", image=self.base_image, bd=0, compound="center", highlightbackground="#444953", highlightthickness=0)
        self.image_button.pack(padx=10, pady=10)

        ## Check button
        self.check_box_state = tk.IntVar()
        self.check_button = tk.Checkbutton(self.window, text="Show Messagebox", font=('Arial', 8,), variable=self.check_box_state)
        self.check_button.pack(padx=10, pady=10)

        ## Message Box
        self.message_box_button = tk.Button(self.window, text="Evaluate Checkbox", font=('Italic', 16), command=self.showMessage)
        self.message_box_button.pack(padx=10, pady=10)

        ## Frame - textfield and button
        self.password_frame = tk.Frame(self.window, bg="#006e6c", padx=15, pady=15)
        self.password_frame.columnconfigure(0, weight=1)
        self.password_frame.columnconfigure(1, weight=1)
        self.password_textfield = tk.Entry(self.password_frame, font=self.italic_font)
        self.password_textfield.bind("<KeyPress>", self.enterPasswordEvent)
        self.password_textfield.grid(row=0, column=0, padx=10, sticky="we")
        self.password_enter_button = tk.Button(self.password_frame, text="Enter Password", font=("Bold", 14), command=self.enterPassword)
        self.password_enter_button.grid(row=0, column=1, padx=10)
        self.password_frame.pack(fill="x")

        ## Listbox
        listbox = tk.Listbox(self.window)
        listbox.insert(1, "Value 1")
        listbox.insert(2, "Number 2")
        listbox.insert(3, "And so on...")
        listbox.pack()

        ## Slider
        self.slider_value_1 = tk.DoubleVar()
        self.horizontal_slider = Scale(self.window, from_=0, to=100, orient=tk.HORIZONTAL, length=400, tickinterval=10, variable=self.slider_value_1, command=self.slider_changed)
        self.horizontal_slider.pack()

        self.vertical_slider = Scale(self.window, from_=-25, to=25)
        self.vertical_slider.pack()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def showMessage(self):
        if self.check_box_state.get() == 1:
            message = self.textbox.get('1.0', tk.END) if len(self.textbox.get('1.0', 'end-1c')) > 0 else "No text in TextBox"
            messagebox.showinfo(title="Unchecked message", message=message)  # show textbox text in messagebox
        else:
            print("Check unchecked")

    def enterPasswordEvent(self, event):
        if event.keysym == "Return":
            self.enterPassword()

    def enterPassword(self):
        if len(self.password_textfield.get()) > 0:
            print(self.password_textfield.get())
        else:
            messagebox.showinfo(title="Password Field", message="No password enter into password field")

    def clearTextBox(self):
        self.textbox.delete('1.0', tk.END)

    def slider_changed(self, event):
        print(event)


    def on_closing(self):
        #TODO: run code
        if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
            print("Window Closing!!!")
            self.window.destroy()

if __name__ == "__main__":
    myGui = MyGUI()