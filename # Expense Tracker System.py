import tkinter as tk
from tkinter import messagebox
import csv
import os

# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("550x550")
root.resizable(False, False)
root.config(bg="#EAF4FC")

# -----------------------------
# Variables
# -----------------------------

expenses = []
FILE_NAME = "expenses.csv"

# -----------------------------
# Functions
# -----------------------------

def add_expense():
    """Add expense and update total"""

    category = category_entry.get()

    try:
        amount = float(amount_entry.get())

        if category == "":
            messagebox.showwarning("Warning", "Please enter a category")
            return

        expense_data = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense_data)

        expense_listbox.insert(
            tk.END,
            f"{category} - ₱{amount:.2f}"
        )

        update_total()

        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

        save_data()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


def delete_expense():
    """Delete selected expense"""

    selected = expense_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Please select an expense")
        return

    index = selected[0]

    expenses.pop(index)

    expense_listbox.delete(index)

    update_total()

    save_data()


def clear_expenses():
    """Clear all expenses"""

    confirm = messagebox.askyesno(
        "Clear All",
        "Are you sure you want to clear all expenses?"
    )

    if confirm:

        expenses.clear()

        expense_listbox.delete(0, tk.END)

        update_total()

        save_data()


def update_total():
    """Compute and display total expenses"""

    total = sum(expense["amount"] for expense in expenses)

    total_label.config(
        text=f"Total Expenses: ₱{total:.2f}"
    )


def save_data():
    """Save expenses to CSV file"""

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        for expense in expenses:
            writer.writerow([
                expense["category"],
                expense["amount"]
            ])


def load_data():
    """Load expenses from CSV file"""

    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            category = row[0]
            amount = float(row[1])

            expense_data = {
                "category": category,
                "amount": amount
            }

            expenses.append(expense_data)

            expense_listbox.insert(
                tk.END,
                f"{category} - ₱{amount:.2f}"
            )

    update_total()

# -----------------------------
# Main Frame
# -----------------------------

frame = tk.Frame(root, bg="#FFFFFF", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    frame,
    text="Expense Tracker System",
    font=("Arial", 18, "bold"),
    fg="#0B5394",
    bg="#FFFFFF"
)

title_label.pack(pady=10)

# -----------------------------
# Category Input
# -----------------------------

category_label = tk.Label(
    frame,
    text="Category:",
    font=("Arial", 11, "bold"),
    fg="#38761D",
    bg="#FFFFFF"
)

category_label.pack(pady=5)

category_entry = tk.Entry(
    frame,
    width=30,
    font=("Arial", 11)
)

category_entry.pack(pady=5)

# -----------------------------
# Amount Input
# -----------------------------

expense_label = tk.Label(
    frame,
    text="Enter Expense Amount:",
    font=("Arial", 11, "bold"),
    fg="#990000",
    bg="#FFFFFF"
)

expense_label.pack(pady=5)

amount_entry = tk.Entry(
    frame,
    width=30,
    font=("Arial", 11)
)

amount_entry.pack(pady=5)

# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(frame, bg="#FFFFFF")
button_frame.pack(pady=15)

add_button = tk.Button(
    button_frame,
    text="Add Expense",
    width=12,
    bg="#6AA84F",
    fg="white",
    font=("Arial", 10, "bold"),
    command=add_expense
)

add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete",
    width=12,
    bg="#CC0000",
    fg="white",
    font=("Arial", 10, "bold"),
    command=delete_expense
)

delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear All",
    width=12,
    bg="#E69138",
    fg="white",
    font=("Arial", 10, "bold"),
    command=clear_expenses
)

clear_button.grid(row=0, column=2, padx=5)

# -----------------------------
# Expense List
# -----------------------------

expense_listbox = tk.Listbox(
    frame,
    width=45,
    height=12,
    font=("Arial", 11),
    bg="#F3F3F3",
    fg="#000000"
)

expense_listbox.pack(pady=10)

# -----------------------------
# Total Label
# -----------------------------

total_label = tk.Label(
    frame,
    text="Total Expenses: ₱0.00",
    font=("Arial", 13, "bold"),
    fg="#0B5394",
    bg="#FFFFFF"
)

total_label.pack(pady=10)

# -----------------------------
# Load Existing Data
# -----------------------------

load_data()

# -----------------------------
# Run Program
# -----------------------------

print("Expense Tracker System Started")

root.mainloop()