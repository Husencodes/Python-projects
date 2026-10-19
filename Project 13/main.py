#importing tkinter library
import tkinter as tk
reset_display=False

def click(event):
    global reset_display

    current=entry.get()
    button_text=event.widget["text"]

    if button_text=='C':
        entry.delete(0,tk.END)
        entry.insert(tk.END,'0')
        reset_display=False

    elif button_text=='=':
        try:
            expression=current.replace('%','/100')
            result=eval(expression)
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(result))
            reset_display=True

        except Exception:
            entry.delete(0,tk.END)
            entry.insert(tk.END,"Error!")
            reset_display=True

    else:
        if reset_display:
            entry.delete(0,tk.END)
            current=""
            reset_display=False

        if current=='0':
            current=""
        #Avoid 2 consecutive operators

        operators="+-*%"

        if current and current[-1] in operators and button_text in operators:
            current=current[:-1]

        #Avoid starting an expression with certain operators

        if current=="" and button_text in "*/":
            return


        #Finally Update the Entry Widget
        entry.delete(0,tk.END)
        entry.insert(tk.END,current+button_text)


root=tk.Tk()#main window
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False,False)
root.configure(bg="#EBDEDE")

#ENTRY WIDGET
entry=tk.Entry(root,bd=5,font=('Arial',20), justify='right', width=16, bg='#b6f2e9')
entry.pack(pady=5)

#Button frame
btnFrame=tk.Frame(root)
btnFrame.pack(padx=10,pady=10)

#claculater buttons
buttons=[['C','(',')','/'],
         ['7','8','9','*'],
         ['4','5','6','-'],
         ['1','2','3','+'],
         ['.','0','%','=']
         ]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn=tk.Button(btnFrame,text=buttons[i][j],font=('Arial',16),width=3,height=1)
        btn.grid(row=i,column=j,padx=10,pady=10)
        btn.bind('<Button-1>',click)


root.mainloop()