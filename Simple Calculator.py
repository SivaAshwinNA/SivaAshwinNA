import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operation == 'Power':
            result = num1 ** num2
        elif operation == 'Modulus':
            result = num1 % num2
        else:
            result = "Select an operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

def exit_app():
    root.destroy()

# GUI Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Input Fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation Dropdown
tk.Label(root, text="Choose Operation:").pack()
operation_var = tk.StringVar()
operation_var.set("Operation")  # default
operations = ["Add", "Subtract", "Multiply", "Divide", "Power", "Modulus"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack()

# Buttons
tk.Button(root, text="Calculate", command=calculate, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Exit", command=exit_app, bg="lightcoral").pack(pady=5)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()


