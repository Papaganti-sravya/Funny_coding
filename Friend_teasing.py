import tkinter as tk
import random

# Create the tkinter window
window = tk.Tk()
window.geometry("300x250")

# Define a function to move the "No" button to a random position
def move_no_button():
    x = random.randint(50, 250)
    y = random.randint(50, 150)
    no_button.place(x=x, y=y)

# Define a function to handle the "Yes" button click event
def handle_yes_button_click():
    message_label.config(text="Awwww", font=("Helvetica", 12))

# Define a function to handle the "No" button click event
def handle_no_button_click():
    move_no_button()

# Create the label with the question
question_label = tk.Label(window, text="Are you in love?", font=("Arial", 14))
question_label.pack(pady=10)

# Create the "Yes" button and add the click event handler
yes_button = tk.Button(window, text="Yes", command=handle_yes_button_click)
yes_button.pack(side=tk.LEFT, padx=20, pady=10)

# Create the "No" button and add the click event handler
no_button = tk.Button(window, text="No", command=handle_no_button_click)
no_button.pack(side=tk.RIGHT, padx=20, pady=10)

# Create the message label
message_label = tk.Label(window, text="")
message_label.pack(pady=20)

# Start the tkinter event loop
window.mainloop()
