import tkinter as tk
from math import sqrt
import time
start_time = time.time()
# Function to evaluate the expression
def evaluate_expression(event=None):
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to handle button click
def on_button_click(value):
    display.insert(tk.END, value)

# Function to clear the display
def clear_display():
    display.delete(0, tk.END)

# Function to calculate square root
def calculate_square_root():
    try:
        result = str(sqrt(float(display.get())))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Function to calculate percentage
def calculate_percentage():
    try:
        result = str(float(display.get()) / 100)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the display widget
display = tk.Entry(root, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Create button widgets
buttons = [
    ('9', 1, 0), ('8', 1, 1), ('7', 1, 2), ('6', 2, 0), ('5', 2, 1), ('4', 2, 2),
    ('3', 3, 0), ('2', 3, 1), ('1', 3, 2), ('0', 4, 0),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('√', 4, 1), ('%', 4, 2), ('=', 4, 4), ('C', 4, 5)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=clear_display)
    elif text == '√':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=calculate_square_root)
    elif text == '%':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=calculate_percentage)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda value=text: on_button_click(value))
    button.grid(row=row, column=col)

# Bind the Enter key to evaluate the expression
root.bind('<Return>', evaluate_expression)
root.update_idletasks()
end_time = time.time()

print(f"Tiempo de inicio del programa: {end_time - start_time} segundos")
# Run the application
root.mainloop()
