from tkinter import *
from core import calc

def run():
    expression = entry.get()
    result = calc(expression)
    label.config(text=result)

root = Tk()
root.title("Калькулятор")
root.geometry("300x200")

entry = Entry(root, font=('Arial', 14))
entry.pack(pady=10)

btn = Button(root, text='=', command=run, font=('Arial', 12))
btn.pack(pady=5)

label = Label(root, text="", font=('Arial', 14))
label.pack(pady=10)

root.mainloop()
