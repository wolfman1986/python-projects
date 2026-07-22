# Password Checker

A simple Python GUI app that checks password strength and gives feedback on how to improve it.

## Overview

This project uses `tkinter` to create a desktop app where the user enters a password and clicks a button to test its strength. The app scores the password based on common security rules and displays the result as **Strong**, **Medium**, or **Weak**.

## Features

- Graphical user interface built with Tkinter.
- Password masking with `*` while typing.
- Strength scoring based on:
  - Minimum length of 8 characters.
  - At least one uppercase letter.
  - At least one lowercase letter.
  - At least one number.
  - At least one special character.
- Feedback messages that show what the password is missing.
- Color-coded result display.

## How It Works

The `check_password()` function evaluates the password against five rules and adds a point for each rule that is met. If all five rules are met, the password is marked **Strong**. If three or four rules are met, it is marked **Medium**. Otherwise, it is marked **Weak**.

When the user clicks **Check Strength**, the app reads the password from the entry box, runs the check, and updates the result label. If the password is missing any requirements, a popup shows helpful feedback.

## Requirements

- Python 3
- Tkinter

## How to Run

1. Save the file as `password_checker.py`.
2. Open a terminal in the project folder.
3. Run:

```bash
python password_checker.py
```

## Example

If the password meets all the rules, the app will show:

```text
Strength: Strong
```

If the password is too short or missing character types, the app will show the missing requirements in a popup.

## File

- `password_checker.py` - main application file.
