import os
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do List - CodSoft - Task 1")
        self.root.geometry("600x600")

        colors = {
            "bittersweet": "#C64449",
            "space-cadet": "#372E5F"
        }

        self.color_bittersweet = colors["bittersweet"]
        self.color_spacecadet = colors["space-cadet"]

        self.root.configure(bg=self.color_spacecadet)
        self.task_items = []
        self.initialize_widgets()
        self.center_window()

    def initialize_widgets(self):
        self.frame = tk.Frame(self.root, bg=self.color_spacecadet)
        self.frame.pack(pady=10)

        image_path = "c:/Users/calls/Downloads/CodSoft/codsoft.png"
        if not os.path.isfile(image_path):
            print(f"Image file not found at path: {image_path}")
        else:
            top_logo_image = Image.open(image_path)
            top_logo_image = top_logo_image.resize((70, 70))
            self.top_logo = ImageTk.PhotoImage(top_logo_image)
            top_logo_label = tk.Label(master=self.frame, image=self.top_logo, bg=self.color_spacecadet)
            top_logo_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        self.task_listbox = tk.Listbox(self.root, bg='white', fg='black', font=('Helvetica', 12))
        self.task_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(self.root, bg=self.color_spacecadet)
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, bg='white', fg='black', font=('Helvetica', 12))
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.date_entry = DateEntry(self.entry_frame, bg='white', fg='black', font=('Helvetica', 12), date_pattern='y-mm-dd')
        self.date_entry.pack(side=tk.LEFT, padx=10)

        self.hour_spinbox = tk.Spinbox(self.entry_frame, from_=0, to=23, wrap=True, width=2, format="%02.0f", font=('Helvetica', 12))
        self.hour_spinbox.pack(side=tk.LEFT, padx=5)

        self.minute_spinbox = tk.Spinbox(self.entry_frame, from_=0, to=59, wrap=True, width=2, format="%02.0f", font=('Helvetica', 12))
        self.minute_spinbox.pack(side=tk.LEFT, padx=5)

        self.add_task_button = tk.Button(self.entry_frame, text="Add ", bg=self.color_bittersweet, fg='white', command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(self.root, bg=self.color_spacecadet)
        self.button_frame.pack(pady=10)

        self.update_task_button = tk.Button(self.button_frame, text="Update ", bg=self.color_bittersweet, fg='white', width=20, command=self.update_task)
        self.update_task_button.grid(row=0, column=0, padx=5, pady=5)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete ", bg=self.color_bittersweet, fg='white', width=20, command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=5, pady=5)

        self.clear_all_tasks_button = tk.Button(self.button_frame, text="Clear All List", bg=self.color_bittersweet, fg='white', width=20, command=self.clear_all_tasks)
        self.clear_all_tasks_button.grid(row=1, column=0, padx=5, pady=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", bg=self.color_bittersweet, fg='white', width=20, command=self.exit_app)
        self.exit_button.grid(row=1, column=1, padx=5, pady=5)

        self.load_tasks()

    def add_task(self):
        task_description = self.task_entry.get()
        task_date = self.date_entry.get()
        task_hour = self.hour_spinbox.get()
        task_minute = self.minute_spinbox.get()
        if task_description:
            task_full_description = f"{task_description} (due on {task_date} at {task_hour}:{task_minute})"
            self.task_items.append(task_full_description)
            self.task_listbox.insert(tk.END, task_full_description)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task_description = self.task_entry.get()
            new_task_date = self.date_entry.get()
            new_task_hour = self.hour_spinbox.get()
            new_task_minute = self.minute_spinbox.get()
            if new_task_description:
                updated_task_full_description = f"{new_task_description} (due on {new_task_date} at {new_task_hour}:{new_task_minute})"
                self.task_items[selected_task_index[0]] = updated_task_full_description
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task_full_description)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.task_items[selected_task_index[0]]
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_all_tasks(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
            self.task_items.clear()
            self.task_listbox.delete(0, tk.END)

    def load_tasks(self):
        for task in self.task_items:
            self.task_listbox.insert(tk.END, task)

    def exit_app(self):
        self.root.quit()

    def center_window(self):
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        position_x = (self.root.winfo_screenwidth() // 2) - (window_width // 2)
        position_y = (self.root.winfo_screenheight() // 2) - (window_height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(window_width, window_height, position_x, position_y))

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
