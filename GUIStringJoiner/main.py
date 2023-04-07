import tkinter as tk

# Define colors for the dark mode theme
bg_color = "#2b2b2b"
fg_color = "#f0f0f0"
entry_bg_color = "#3a3a3a"
entry_fg_color = "#f0f0f0"
button_bg_color = "#555555"
button_fg_color = "#f0f0f0"
output_fg_color = "#f0f0f0"

def merge_strings():
    # Merge the two strings using the join() method
    merged_str = ''.join([entry1.get(), entry2.get()])
    
    # Display the merged string in the output label
    output_label.config(text=merged_str)

# Create the main window
root = tk.Tk()
root.title("String Merger")
root.configure(bg=bg_color)

# Create the input labels and entry widgets
tk.Label(root, text="First string:", bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root, bg=entry_bg_color, fg=entry_fg_color)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Second string:", bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root, bg=entry_bg_color, fg=entry_fg_color)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Create the button to merge the strings
merge_button = tk.Button(root, text="Merge", command=merge_strings, bg=button_bg_color, fg=button_fg_color)
merge_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create the output label
output_label = tk.Label(root, text="", font=("Arial", 12), fg=output_fg_color, bg=bg_color)
output_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Set focus on the first entry widget
entry1.focus()

# Start the main event loop
root.mainloop()