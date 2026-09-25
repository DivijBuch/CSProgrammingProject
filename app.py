import tkinter as tk
from tkinter import messagebox
root = tk.Tk()



class OCRtunes:
    "Application to play, add music"

    def __init__(self, root):
        self.root = root
        self.root.title("OCRtunes")
        self.root.geometry("400x300")
        # Configure window properties
        self.root.resizable(True, True)
        self.root.minsize(300, 200)

        # Initialize UI components
        self.setup_ui()

    def setup_ui(self):
        """Create and arrange widgets."""
        # Title label with custom styling
        self.title_label = tk.Label(
            self.root,
            text="Welcome to OCRTunes",
            font=("Helvetica", 18, "bold"),
            fg="#2c3e50",
            pady=20
        )
        self.title_label.pack()
        # Input frame for organized layout
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter your name:").grid(row=0, column=0, padx=5)

        self.name_entry = tk.Entry(input_frame, width=25)
        self.name_entry.grid(row=0, column=1, padx=5)
        self.name_entry.bind('', lambda e: self.on_submit())

        # Action button
        self.submit_button = tk.Button(
            self.root,
            text="Submit",
            command=self.on_submit,
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.submit_button.pack(pady=20)

        # Status label
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 12),
            fg="#27ae60"
        )
        self.status_label.pack()

    def on_submit(self):
        """Handle submit button click."""
        name = self.name_entry.get().strip()

        if not name:
            messagebox.showwarning("Input Error", "Please enter your name")
            return

        self.status_label.config(text=f"Hello, {name}!")
        print(f"User submitted: {name}")

def main():
    root = tk.Tk()
    app = OCRtunes(root)
    root.mainloop()

if __name__ == '__main__':
    main()
