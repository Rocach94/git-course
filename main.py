import tkinter as tk

# Initialize the main application window
root = tk.Tk()

# Set the title of the window
root.title("Simple Tkinter Window")

# Specify the size and position of the window
# Format: 'width x height + x_offset + y_offset'
root.geometry("1024x600+100+100")

# Run the application, waiting for user interaction
root.mainloop()
