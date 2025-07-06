import tkinter as tk
from tkinter import messagebox
import schedule
import time
import threading
import pyttsx3
from datetime import datetime

# Text-to-speech engine
engine = pyttsx3.init()

# Function to show and speak reminder
def show_reminder(med_name):
    msg = f"Time to take your medicine: {med_name}"
    messagebox.showinfo("Medicine Reminder", msg)
    engine.say(msg)
    engine.runAndWait()

# Function to schedule the reminder
def set_reminder():
    med_name = med_entry.get()
    time_str = time_entry.get()
    try:
        # Validate time format
        datetime.strptime(time_str, "%H:%M")
        schedule.every().day.at(time_str).do(show_reminder, med_name)
        status_label.config(text=f"Reminder set for {med_name} at {time_str}")
    except ValueError:
        messagebox.showerror("Invalid Time", "Time must be in HH:MM format")

# Function to run the scheduler in a separate thread
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# GUI
app = tk.Tk()
app.title("Medication Reminder")
app.geometry("350x200")

tk.Label(app, text="Medicine Name:").pack(pady=5)
med_entry = tk.Entry(app, width=30)
med_entry.pack()

tk.Label(app, text="Reminder Time (HH:MM):").pack(pady=5)
time_entry = tk.Entry(app, width=30)
time_entry.pack()

tk.Button(app, text="Set Reminder", command=set_reminder).pack(pady=10)
status_label = tk.Label(app, text="", fg="green")
status_label.pack()

# Start schedule thread
threading.Thread(target=run_schedule, daemon=True).start()

app.mainloop()
