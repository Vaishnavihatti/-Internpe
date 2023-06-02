import tkinter as tk
import time
from datetime import date

def clock():
    current_time = time.strftime("%H:%M:%S %p")
    current_date = date.today().strftime("%B %d, %Y")
    current_day = date.today().strftime("%A")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    day_label.config(text=current_day)
    clock_label.after(1000, clock)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("500x250")
window.resizable(False, False)
window.configure(bg="black")

# Create clock label
clock_label = tk.Label(window, font=("Bahnschrift", 50), fg="red", bg="black")
clock_label.pack(pady=5)
# Create date label
date_label = tk.Label(window, font=("Bahnschrift", 30), fg="red", bg="black")
date_label.pack()

# Create day label
day_label = tk.Label(window, font=("Bahnschrift", 30), fg="red", bg="black")
day_label.pack()

# Update the clock display
clock()

# Start the main loop
window.mainloop()