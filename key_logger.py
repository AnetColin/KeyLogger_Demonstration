import tkinter as tk
from datetime import datetime

LOG_FILE = "keylog_demo.txt"

def log_key(event):
    key = event.keysym
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{time} - {key}\n")

    label.config(text=f"Last key pressed: {key}")

# Create window
root = tk.Tk()
root.title("Keylogger Demonstration (Educational)")
root.geometry("500x200")

label = tk.Label(
    root,
    text="Click inside this window and type.\nKeys are logged ONLY here.",
    font=("Arial", 12)
)
label.pack(pady=40)

# Bind key press event
root.bind("<KeyPress>", log_key)

root.mainloop()
