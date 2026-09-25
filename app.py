import tkinter as tk
root = tk.Tk()

#setting window properties
root.title("OCRtunes")
root.configure(background="white")
root.minsize(200, 200)
root.maxsize(2500, 2000)
root.geometry("300x300+50+50")

#create two labels
tk.Label(root, text="Welcome to OCRtunes").pack()
tk.Label(root, text="Please select an option below").pack()

