import tkinter as tk

def update_label(*args):
    # Update the label to show what is currently in the entry box
    typed_text.set(entry.get())

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Reader")

    # Set up a StringVar to hold the text that is typed
    global typed_text
    typed_text = tk.StringVar()

    # Create an entry widget for text input
    global entry
    entry = tk.Entry(root, font=('Arial', 14))
    entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Bind the entry widget to update the label on any change
    entry.bind("<KeyRelease>", update_label)

    # Create a label to display what is typed
    label = tk.Label(root, textvariable=typed_text, font=('Arial', 14))
    label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()