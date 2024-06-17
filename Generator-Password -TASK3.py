import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random
import string

def create_password(length, include_letters, include_numbers, include_symbols):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one option must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_password():
    try:
        length = length_input.get()
        print(f"Input length: {length}")
        
        if not length.isdigit() or int(length) <= 0:
            messagebox.showerror("Error", "Password length must be a positive integer.")
            return
        
        length = int(length)
        use_letters = letters_check_var.get()
        use_numbers = numbers_check_var.get()
        use_symbols = symbols_check_var.get()
        
        print(f"Options selected - Letters: {use_letters}, Numbers: {use_numbers}, Symbols: {use_symbols}")
        
        if not (use_letters or use_numbers or use_symbols):
            messagebox.showerror("Error", "You must select at least one option (letters, numbers, or symbols).")
            return
        
        password = create_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
        
        password_output.config(state=tk.NORMAL)
        password_output.delete(0, tk.END)
        password_output.insert(0, password)
        password_output.config(state=tk.DISABLED)
    except ValueError as e:
        print(f"ValueError: {e}")
        messagebox.showerror("Error", "Please enter a valid number.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def position_window_center(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

root = tk.Tk()
root.title("Password Generator - CodSoft - Task 3")
root.geometry("600x400")
root.configure(bg='#C64449')

position_window_center(root, 600, 400)

main_frame = tk.Frame(root, bg='#C64449')
main_frame.pack(pady=10)

image_path = "c:/Users/calls/Downloads/CodSoft/codsoft.png"
if not os.path.isfile(image_path):
    print(f"Image file not found at path: {image_path}")
else:
    top_logo_img = Image.open(image_path)
    top_logo_img = top_logo_img.resize((70, 70))
    top_logo = ImageTk.PhotoImage(top_logo_img)
    top_logo_label = tk.Label(master=main_frame, image=top_logo, bg='#C64449')
    top_logo_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

colors = {
    "bittersweet": "#C64449",
    "space-cadet": "#372E5F"
}

color_bittersweet = colors["bittersweet"]
color_spacecadet = colors["space-cadet"]

input_frame = tk.Frame(root, bg=color_bittersweet)
input_frame.pack(pady=10)

length_label = tk.Label(input_frame, text="Password Length:", font=("Arial", 14, "bold"), bg=color_bittersweet, fg="white")
length_label.grid(row=0, column=0, padx=5, pady=5)

length_input = tk.Entry(input_frame, font=("Arial", 12), width=10, justify='center')
length_input.grid(row=0, column=1, padx=5, pady=5)

letters_check_var = tk.BooleanVar()
numbers_check_var = tk.BooleanVar()
symbols_check_var = tk.BooleanVar()

letters_checkbutton = tk.Checkbutton(input_frame, text="Letters", variable=letters_check_var, font=("Arial", 12), bg=color_bittersweet, fg="white", selectcolor="#372E5F")
letters_checkbutton.grid(row=1, column=0, padx=5, pady=5)

numbers_checkbutton = tk.Checkbutton(input_frame, text="Numbers", variable=numbers_check_var, font=("Arial", 12), bg=color_bittersweet, fg="white", selectcolor="#372E5F")
numbers_checkbutton.grid(row=1, column=1, padx=5, pady=5)

symbols_checkbutton = tk.Checkbutton(input_frame, text="Symbols", variable=symbols_check_var, font=("Arial", 12), bg=color_bittersweet, fg="white", selectcolor="#372E5F")
symbols_checkbutton.grid(row=1, column=2, padx=5, pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=on_generate_password, font=("Arial", 12, "bold"), width=20, bg=color_spacecadet, fg="white")
generate_btn.pack(pady=15)

output_frame = tk.Frame(root, bg=color_bittersweet)
output_frame.pack(pady=10)

password_label = tk.Label(output_frame, text="Generated Password:", font=("Arial", 12, "bold"), bg=color_bittersweet, fg="white")
password_label.pack(pady=5)

password_output = tk.Entry(output_frame, font=("Arial", 12), state=tk.DISABLED, width=30, justify='center', disabledforeground="#372E5F")
password_output.pack(pady=5)

root.mainloop()
