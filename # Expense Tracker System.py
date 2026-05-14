import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x300")

expenses = []


# Expense Tracker System

# -----------------------------
# Functions
# -----------------------------

def add_expense():
    """Add expense and update total"""
    try:
        amount = float(amount_entry.get())
        expenses.append(amount)
        update_total()
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")


def delete_expense():
    pass


def clear_expenses():
    pass


def update_total():
    """Compute and show total"""
    total = sum(expenses)
    total_label.config(text=f"Total Expenses: ₱{total:.2f}")


def save_data():
    pass


def load_data():
    pass


frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")


tk.Label(frame, text="Enter Expense:").pack(pady=5)

amount_entry = tk.Entry(frame)
amount_entry.pack(pady=5)

tk.Button(frame, text="Add Expense", command=add_expense).pack(pady=10)

total_label = tk.Label(
    frame,
    text="Total Expenses: ₱0.00",
    font=("Arial", 12, "bold")
)
total_label.pack(pady=10)

root.mainloop()
# -----------------------------
# Main Program
# -----------------------------

print("Expense Tracker System Started")