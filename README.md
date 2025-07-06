# 💊 Medication Reminder App

A simple and effective Python desktop app that reminds users to take their medication through voice alerts and pop-up notifications. Built using Tkinter, `schedule`, and `pyttsx3`.

## 🧠 Features

- 🕒 **Daily Reminders** – Schedule alerts at user-defined times
- 💬 **Pop-Up Notifications** – Alerts using `tkinter.messagebox`
- 🗣️ **Text-to-Speech** – Speaks the reminder aloud with `pyttsx3`
- 🔁 **Runs in Background** – Uses multithreading to keep the UI responsive
- ✅ **Time Validation** – Accepts time in `HH:MM` (24-hour) format

## 🛠 Tech Stack

- `Tkinter` – GUI interface
- `schedule` – Time-based job scheduling
- `pyttsx3` – Offline text-to-speech
- `threading`, `datetime` – System utilities

## 🚀 How to Use

1. Clone the repo or download the code.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
