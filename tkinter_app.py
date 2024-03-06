import tkinter as tk

class MyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("My tkinter App")
        self.window.geometry("500x500")

        self.main_frame = tk.Frame(self.window, highlightbackground="black", highlightthickness=1, relief=tk.RIDGE)
        self.main_frame.pack(padx=20, pady=20)

        self.text_box = tk.Text(self.main_frame, height=3, font=("Bold",18) )
        self.text_box.pack(padx=5, pady=5)

        self.window.mainloop()


if __name__ == "__main__":
    my_app_window = MyGUI()