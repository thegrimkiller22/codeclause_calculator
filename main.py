import tkinter as tk

def on_click(btn_text):
    if btn_text == '=':
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif btn_text == 'C':
        display_var.set("")
    else:
        display_var.set(display_var.get() + btn_text)

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create a variable to store the display text
display_var = tk.StringVar()
display_var.set("")

# Create the display label
display_label = tk.Label(root, textvariable=display_var, font=('Helvetica', 20), bd=5, relief=tk.RIDGE, anchor=tk.E)
display_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the buttons and their grid positions
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0),
]

# Create the buttons and set their click event
for btn_text, row, col in buttons:
    btn = tk.Button(root, text=btn_text, font=('Helvetica', 18), bd=5, relief=tk.GROOVE,
                    command=lambda t=btn_text: on_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

# Make the grid cells expandable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()
