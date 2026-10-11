
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.configure(bg="yellow")

def time():
    string = strftime('%H:%M:%S %p\n%d-%m-%Y')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(
    root,
    font=('Calibri', 35, 'bold'),
    background='yellow',
    foreground='black'
)
label.pack(anchor='center', expand=True)

time()

root.mainloop()
