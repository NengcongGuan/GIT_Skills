import tkinter as tk
from tkinter import ttk

def add_digit(digit):
    current = calc_display.get()
    if current == '0':
        calc_display.delete(0, tk.END)
    calc_display.insert(tk.END, digit)

def add_operation(operator):
    current = calc_display.get()
    if current[-1] in '+-*/':
        return
    calc_display.insert(tk.END, operator)

def clear_display():
    calc_display.delete(0, tk.END)
    calc_display.insert(0, '0')

def calculate_result():
    try:
        result = eval(calc_display.get())
        calc_display.delete(0, tk.END)
        calc_display.insert(0, str(result))
    except Exception as e:
        clear_display()
        calc_display.insert(0, "Error")

def update_label(*args):
    typed_text.set(entry.get())

def create_calculator_tab(parent):
    frame = ttk.Frame(parent)
    global calc_display
    calc_display = tk.Entry(frame, justify='right', font=('Arial', 15))
    calc_display.insert(0, '0')
    calc_display.grid(row=0, column=0, columnspan=4, sticky="we")

    ttk.Button(frame, text='C', command=clear_display).grid(row=1, column=0)
    ttk.Button(frame, text='/', command=lambda: add_operation('/')).grid(row=1, column=3)
    ttk.Button(frame, text='*', command=lambda: add_operation('*')).grid(row=2, column=3)
    ttk.Button(frame, text='-', command=lambda: add_operation('-')).grid(row=3, column=3)
    ttk.Button(frame, text='+', command=lambda: add_operation('+')).grid(row=4, column=3)
    ttk.Button(frame, text='=', command=calculate_result).grid(row=5, column=3)

    for i in range(1, 4):
        ttk.Button(frame, text=str(i), command=lambda x=i: add_digit(str(x))).grid(row=2, column=i-1)
    for i in range(4, 7):
        ttk.Button(frame, text=str(i), command=lambda x=i: add_digit(str(x))).grid(row=3, column=i-4)
    for i in range(7, 10):
        ttk.Button(frame, text=str(i), command=lambda x=i: add_digit(str(x))).grid(row=4, column=i-7)
    ttk.Button(frame, text='0', command=lambda: add_digit('0')).grid(row=5, column=0, columnspan=3, sticky="we")

    return frame

def create_reader_tab(parent):
    frame = ttk.Frame(parent)
    global typed_text, entry
    typed_text = tk.StringVar()

    entry = tk.Entry(frame, font=('Arial', 14))
    entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    entry.bind("<KeyRelease>", update_label)

    label = tk.Label(frame, textvariable=typed_text, font=('Arial', 14))
    label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    return frame

def main():
    root = tk.Tk()
    root.title("Multi-Function Application")

    tab_control = ttk.Notebook(root)

    calculator_tab = create_calculator_tab(tab_control)
    reader_tab = create_reader_tab(tab_control)

    tab_control.add(calculator_tab, text='Calculator')
    tab_control.add(reader_tab, text='Reader')

    tab_control.pack(expand=1, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()