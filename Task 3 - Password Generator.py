#Password Generating Application
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate():
    le=length.get()
    up=upper.get()
    lo=lower.get()
    n=num.get()
    s=spl.get()
    c=""
    if up:
        c += string.ascii_uppercase
    if lo:
        c += string.ascii_lowercase
    if n:
        c += string.digits
    if s:
        c += string.punctuation
    if not any([up,lo,n,s]):
        messagebox.showerror("Error","At least on check-box should be selected")
        return
    if le<=0:
        messagebox.showerror("Error","length should be atleast 1")
        return
    p=""
    for i in range(le):
        p += random.choice(c)
    print("Your Password :",p)
    messagebox.showinfo("Generated Password",f"Your Password: {p}")
def close():
    win.destroy()

win=tk.Tk()
win.title("Password Generator")

length=tk.IntVar(value=10)
upper=tk.BooleanVar(value=True)
lower=tk.BooleanVar(value=True)
num=tk.BooleanVar(value=True)
spl=tk.BooleanVar(value=True)

main=ttk.Frame(win)
main.grid(column=0,row=0,sticky=(tk.W, tk.E, tk.N, tk.S))
ttk.Label(main,text="Password Length").grid(column=0,row=0,padx=10,sticky=tk.W)
input_len=ttk.Entry(main,textvariable=length,width=10)
input_len.grid(column=1,row=0,padx=20,sticky=tk.W)

ttk.Checkbutton(main, text="Include Uppercase", variable=upper).grid(column=0,padx=10,row=1, sticky=tk.W)
ttk.Checkbutton(main, text="Include Lowercase", variable=lower).grid(column=0, row=2,padx=10,sticky=tk.W)
ttk.Checkbutton(main, text="Include Numbers", variable=num).grid(column=0, row=3,padx=10,sticky=tk.W)
ttk.Checkbutton(main, text="Include Special Characters", variable=spl).grid(column=0, row=4,padx=10, sticky=tk.W)

btn=ttk.Button(main,text="Generate Password",command=generate)
btn.grid(column=0,row=5,pady=10)

close_btn=ttk.Button(main,text="Close",command=close)
close_btn.grid(column=1,row=5,padx=20,pady=10)

win.mainloop()