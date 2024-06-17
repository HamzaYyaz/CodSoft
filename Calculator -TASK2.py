import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
from PIL import Image, ImageTk
import os

window = tk.Tk()
window.title('Calculator - CodSoft - Task 2')

couleurs = {
    "bittersweet": "#C64449", 
    "space-cadet": "#372E5F"  
}

couleur_bittersweet = couleurs["bittersweet"]
couleur_spacecadet = couleurs["space-cadet"]

frame = tk.Frame(master=window, bg=couleur_spacecadet, padx=10)
frame.pack()

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)
image_path = "c:/Users/calls/Downloads/CodSoft/codsoft.png"
if not os.path.isfile(image_path):
    print(f"Image file not found at path: {image_path}")
else:
    top_logo_image = Image.open(image_path) 
    top_logo_image = top_logo_image.resize((70, 70))
    top_logo = ImageTk.PhotoImage(top_logo_image)
    top_logo_label = tk.Label(master=frame, image=top_logo, bg=couleur_spacecadet)
    top_logo_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=1, column=0, columnspan=3, ipady=2, pady=2)

button1 = tk.Button(master=frame, bg=couleur_bittersweet, text='1', padx=15, pady=5, width=3, command=lambda: myclick(1), fg="white")
button1.grid(row=2, column=0, pady=2)

button2 = tk.Button(master=frame, bg=couleur_bittersweet, text='2', padx=15, pady=5, width=3, command=lambda: myclick(2), fg="white")
button2.grid(row=2, column=1, pady=2)

button3 = tk.Button(master=frame, bg=couleur_bittersweet, text='3', padx=15, pady=5, width=3, command=lambda: myclick(3), fg="white")
button3.grid(row=2, column=2, pady=2)

button4 = tk.Button(master=frame, bg=couleur_bittersweet, text='4', padx=15, pady=5, width=3, command=lambda: myclick(4), fg="white")
button4.grid(row=3, column=0, pady=2)

button5 = tk.Button(master=frame, bg=couleur_bittersweet, text='5', padx=15, pady=5, width=3, command=lambda: myclick(5), fg="white")
button5.grid(row=3, column=1, pady=2)

button6 = tk.Button(master=frame, bg=couleur_bittersweet, text='6', padx=15, pady=5, width=3, command=lambda: myclick(6), fg="white")
button6.grid(row=3, column=2, pady=2)

button7 = tk.Button(master=frame, bg=couleur_bittersweet, text='7', padx=15, pady=5, width=3, command=lambda: myclick(7), fg="white")
button7.grid(row=4, column=0, pady=2)

button8 = tk.Button(master=frame, bg=couleur_bittersweet, text='8', padx=15, pady=5, width=3, command=lambda: myclick(8), fg="white")
button8.grid(row=4, column=1, pady=2)

button9 = tk.Button(master=frame, bg=couleur_bittersweet, text='9', padx=15, pady=5, width=3, command=lambda: myclick(9), fg="white")
button9.grid(row=4, column=2, pady=2)

button0 = tk.Button(master=frame, bg=couleur_bittersweet, text='0', padx=15, pady=5, width=3, command=lambda: myclick(0), fg="white")
button0.grid(row=5, column=1, pady=2)

buttonAdd = tk.Button(master=frame, bg=couleur_bittersweet, text="+", padx=15, pady=5, width=3, command=lambda: myclick('+'), fg="white")
buttonAdd.grid(row=6, column=0, pady=2)

buttonSubtract = tk.Button(master=frame, bg=couleur_bittersweet, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'), fg="white")
buttonSubtract.grid(row=6, column=1, pady=2)

buttonMultiply = tk.Button(master=frame, bg=couleur_bittersweet, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'), fg="white")
buttonMultiply.grid(row=6, column=2, pady=2)

buttonDiv = tk.Button(master=frame, bg=couleur_bittersweet, text="/", padx=15, pady=5, width=3, command=lambda: myclick('/'), fg="white")
buttonDiv.grid(row=7, column=0, pady=2)

buttonClear = tk.Button(master=frame, bg=couleur_bittersweet, text="clear", padx=15, pady=5, width=12, command=clear, fg="white")
buttonClear.grid(row=7, column=1, columnspan=2, pady=2)

buttonEqual = tk.Button(master=frame, bg=couleur_bittersweet, text="=", padx=15, pady=5, width=9, command=equal, fg="white")
buttonEqual.grid(row=8, column=0, columnspan=3, pady=2)

window.mainloop()

