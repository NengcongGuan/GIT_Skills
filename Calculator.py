import tkinter as tk

def add_digit(digit):
    current = display.get()
    if current == '0':
        display.delete(0, tk.END)
    display.insert(tk.END, digit)

def add_operation(operator):
    current = display.get()
    if current[-1] in '+-*/':
        return
    display.insert(tk.END, operator)

def clear_display():
    display.delete(0, tk.END)
    display.insert(0, '0')

def calculate_result():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        clear_display()
        display.insert(0, "Error")

def create_button(parent, text, command, row, column, columnspan=1):
    button = tk.Button(parent, text=text, command=command)
    button.grid(row=row, column=column, columnspan=columnspan, sticky="nsew")
    return button

def main():
    root = tk.Tk()
    root.title("Calculator")

    global display
    display = tk.Entry(root, justify='right', font=('Arial', 15))
    display.insert(0, '0')
    display.grid(row=0, column=0, columnspan=4, stick="we")

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)

    create_button(root, 'C', clear_display, 1, 0)
    create_button(root, '/', lambda: add_operation('/'), 1, 3)
    for i in range(1, 4):
        create_button(root, str(i), lambda x=i: add_digit(str(x)), 2, i-1)
    create_button(root, '*', lambda: add_operation('*'), 2, 3)
    for i in range(4, 7):
        create_button(root, str(i), lambda x=i: add_digit(str(x)), 3, i-4)
    create_button(root, '-', lambda: add_operation('-'), 3, 3)  # Fixed -- the sign is not correct
    for i in range(7, 10):
        create_button(root, str(i), lambda x=i: add_digit(str(x)), 4, i-7)
    create_button(root, '+', lambda: add_operation('+'), 4, 3)  # Fixed -- the sign is not correct
    create_button(root, '=', calculate_result, 5, 3)
    create_button(root, '0', lambda: add_digit('0'), 5, 0, 3)

    root.mainloop()

if __name__ == "__main__":
    main()