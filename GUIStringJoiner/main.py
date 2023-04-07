import tkinter as tk
from tkinter import filedialog

class GUIStringJoiner(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUIStringJoiner")
        self.setup_widgets()
        self.setup_dark_mode()

    def setup_widgets(self):
        self.input1_label = tk.Label(self, text="Input 1:")
        self.input1_label.pack(fill=tk.X, padx=5, pady=5)
        
        self.input1_entry = tk.Entry(self)
        self.input1_entry.pack(fill=tk.X, padx=5, pady=5)

        self.input2_label = tk.Label(self, text="Input 2:")
        self.input2_label.pack(fill=tk.X, padx=5, pady=5)

        self.input2_entry = tk.Entry(self)
        self.input2_entry.pack(fill=tk.X, padx=5, pady=5)

        self.join_button = tk.Button(self, text="Join Strings", command=self.join_strings)
        self.join_button.pack(fill=tk.X, padx=5, pady=5)

        self.output_label = tk.Label(self, text="Output:")
        self.output_label.pack(fill=tk.X, padx=5, pady=5)

        self.output_entry = tk.Entry(self)
        self.output_entry.pack(fill=tk.X, padx=5, pady=5)

        self.copy_button = tk.Button(self, text="Copy Output", command=self.copy_output)
        self.copy_button.pack(fill=tk.X, padx=5, pady=5)

        self.save_button = tk.Button(self, text="Save Output to File", command=self.save_output)
        self.save_button.pack(fill=tk.X, padx=5, pady=5)

        self.theme_button = tk.Button(self, text="Toggle Dark Mode", command=self.toggle_theme)
        self.theme_button.pack(fill=tk.X, padx=5, pady=5)

    def join_strings(self):
        input1 = self.input1_entry.get()
        input2 = self.input2_entry.get()
        output = ' '.join([input1, input2])
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, output)

    def copy_output(self):
        self.clipboard_clear()
        self.clipboard_append(self.output_entry.get())

    def save_output(self):
        file = filedialog.asksaveasfile(defaultextension=".txt")
        if file:
            file.write(self.output_entry.get())
            file.close()

    def setup_dark_mode(self):
        self.dark_mode = False
        self.light_colors = {
            "bg": "white",
            "fg": "black",
            "button_bg": "light gray"
        }
        self.dark_colors = {
            "bg": "#222831",
            "fg": "#eeeeee",
            "button_bg": "#393e46"
        }

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        colors = self.dark_colors if self.dark_mode else self.light_colors
        self.configure(bg=colors["bg"])
        self.input1_label.configure(bg=colors["bg"], fg=colors["fg"])
        self.input1_entry.configure(bg=colors["bg"], fg=colors["fg"], insertbackground=colors["fg"])
        self.input2_label.configure(bg=colors["bg"], fg=colors["fg"])
        self.input2_entry.configure(bg=colors["bg"], fg=colors["fg"], insertbackground=colors["fg"])
        self.join_button.configure(bg=colors["button_bg"], fg=colors["fg"])
        self.output_label.configure(bg=colors["bg"], fg=colors["fg"])
        self.output_entry.configure(bg=colors["bg"], fg=colors["fg"], insertbackground=colors["fg"])
        self.copy_button.configure(bg=colors["button_bg"], fg=colors["fg"])
        self.save_button.configure(bg=colors["button_bg"], fg=colors["fg"])
        self.theme_button.configure(bg=colors["button_bg"], fg=colors["fg"])

if __name__ == "__main__":
    app = GUIStringJoiner()
    app.mainloop()