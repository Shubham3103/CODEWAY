import tkinter

def calculate():
    try:
        n1=float(input_num1.get())
        n2=float(input_num2.get())
        opr=op.get()
        if opr=='+':
            res=n1+n2
        elif opr=='-':
            res=n1-n2
        elif opr=='*':
            res=n1*n2
        elif opr=='power':
            try:
                res=n1**n2
            except OverflowError:
                result.set("Result is too large")
                return
        elif opr=='/':
            try:
                res=n1/n2
            except ZeroDivisionError:
                result.set("Cannot divide by zero.")
                return
        else:
            result.set("Invalid Operation")
            return
        result.set(f"Result : {res}")
    except ValueError as val:
        result.set("Error: Invalid Operands.")
def close():
    win.destroy()

win=tkinter.Tk()
win.title("Basic Calculator")
win.geometry("400x170")

input_num1=tkinter.Entry(win, width=20)
input_num1.grid(row=0, column=0, padx=10,pady=10)

op=tkinter.StringVar()
op_choices=['+','-','*','/','power']
op_menu=tkinter.OptionMenu(win,op,*op_choices)
op_menu.config(width=7)
op_menu.grid(row=0,column=1,padx=10,pady=10)

input_num2=tkinter.Entry(win, width=20)
input_num2.grid(row=0, column=2, padx=10,pady=10)

calc_btn=tkinter.Button(win,text="Calculate",font=("arial",11),command=calculate)
calc_btn.grid(row=1,column=0,columnspan=3,pady=5)

result =tkinter.StringVar()
result_label=tkinter.Label(win, textvariable=result,font=("arial",13))
result_label.grid(row=2,column=0,columnspan=3,pady=5)

close_btn=tkinter.Button(win,text="Close",font=("arial",11),command=close)
close_btn.grid(row=3,column=0,columnspan=3,pady=5)

win.mainloop()
