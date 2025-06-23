import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)  # update every 1000 ms = 1 second

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Configure window size and background
root.geometry("300x100")
root.configure(bg="black")

# Create and style label
label = tk.Label(root, font=('Arial', 40), fg='cyan', bg='black')
label.pack(anchor='center')

# Start updating time
update_time()

# Start the GUI event loop
root.mainloop()
