import string
import tkinter as tk
from tkinter import messagebox

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("At least one uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("At least one lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("At least one number.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("At least one special character.")

    if score == 5:
        return "Strong", feedback
    elif score >= 3:
        return "Medium", feedback
    else:
        return "Weak", feedback

def show_result():
    password = entry.get()
    strength, feedback = check_password(password)

    result_label.config(text=f"Strength: {strength}")

    if strength == "Strong":
        result_label.config(fg="green")
    elif strength == "Medium":
        result_label.config(fg="orange")
    else:
        result_label.config(fg="red")

    if feedback:
        messagebox.showinfo("Password Feedback", "\n".join(feedback))
    else:
        messagebox.showinfo("Password Feedback", "Your password looks good!")

root = tk.Tk()
root.title("Password Checker")
root.geometry("400x220")
root.resizable(False, False)

title = tk.Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(root, text="Check Strength", command=show_result, font=("Arial", 12))
button.pack(pady=10)

result_label = tk.Label(root, text="Strength: ", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()