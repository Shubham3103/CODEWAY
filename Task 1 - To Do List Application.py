import tkinter as tk
from tkinter import ttk, messagebox
import os

class todolist:
    def __init__(self,main):
        self.main=main
        ttk.Label(self.main,text="To Do List Application",font=("calibri",15)).grid(row=0,column=0,pady=5,padx=30)
        ttk.Radiobutton(self.main,text="Create",command=self.create).grid(column=0,row=1,sticky=tk.W,padx=35,pady=5)
        ttk.Radiobutton(self.main,text="View",command=self.view).grid(column=0,row=2,sticky=tk.W,padx=35,pady=5)
        ttk.Radiobutton(self.main,text="Update",command=self.update).grid(column=0,row=3,sticky=tk.W,padx=35,pady=5)
        ttk.Radiobutton(self.main,text="Delete",command=self.delete).grid(column=0,row=4,sticky=tk.W,padx=35,pady=5)
    def view(self):
        view_win=tk.Tk()
        self.view_win=view_win
        view_win.title("List")
        view_main=ttk.Frame(view_win)
        view_main.grid(row=0,column=0,sticky=(tk.W, tk.E, tk.N, tk.S))
        ttk.Label(view_main,text="Enter the name of the list",font=("calibri",16)).grid(row=0,columnspan=2,column=0,sticky=tk.N,padx=30,pady=5)
        name_entry=ttk.Entry(view_main,width=25)
        name_entry.grid(row=1,columnspan=2,column=0,padx=35,pady=5)
        self.name_entry=name_entry
        self.mode="view"
        sub_btn=ttk.Button(view_main,text="Enter",command=self.check1)
        sub_btn.grid(row=2,column=0,padx=10,pady=5)
        self.view_win=view_win
        self.window=view_win
        close_btn=ttk.Button(view_main,text="Close",command=self.close).grid(row=2,column=1,pady=10,padx=10)
    def add(self):
        new_entry=ttk.Entry(self.up_main2,width=35)
        new_entry.grid(row=self.count,columnspan=2,column=0,padx=30,pady=5)
        self.new_entry.append(new_entry)
        self.add_btn.grid(row=self.count+1,column=0,padx=20,pady=5)
        self.sub_btn.grid(row=self.count+1,column=1,padx=20,pady=5)
        self.count +=1
    def save(self):
        replace_file="A.txt"
        f2=open(replace_file,'w+')
        c=1
        l=""
        for x,y in self.val:
            if x.get()==False:
                l=l+str(c)+". "+y[3:]+"\n"
                c+=1
        for x in self.new_entry:
            l=l+str(c)+". "+str(x.get())+'\n'
            c+= 1
        m=self.name_entry.get()
        n=m+'.txt'
        f2.write(l)
        f2.close()
        os.remove(n)
        os.rename(replace_file,n)
        messagebox.showinfo("Updated","List updated Successfully.")
        self.up_win2.destroy()
        self.up_win.destroy()
    def close(self):
        try:
            if self.window==self.view_win2:
                self.view_win.destroy()
            self.window.destroy()
        except:
            self.window.destroy()
    def check1(self):
        m=self.name_entry.get()
        n=m+'.txt'
        checking=os.path.exists(n)
        if checking ==True:
            if self.mode=="view":
                self.f=open(n,'r')
                lines=self.f.readlines()
                self.f.close()
                view_win2=tk.Tk()
                self.view_win2=view_win2
                view_win2.title("List")
                view_main2=ttk.Frame(view_win2)
                view_main2.grid(row=0,column=0,sticky=(tk.W, tk.E, tk.N, tk.S))
                ttk.Label(view_main2,text=m,font=("calibri",18)).grid(row=0,column=0,sticky=tk.N,padx=30,pady=10)
                c=1
                for i in lines:
                    ttk.Label(view_main2,text=i[0:-1],font=("arial",12)).grid(row=c,column=0,sticky=tk.W,padx=30,pady=5)
                    c+=1
                self.view_win2=view_win2
                self.window=view_win2
                close_btn=ttk.Button(view_main2,text="Close",command=self.close).grid(row=c,column=0,pady=10,padx=30)
            elif self.mode=="update":
                with open(n,'r+') as self.f:
                    lines=self.f.readlines()
                up_win2=tk.Tk()
                self.up_win2=up_win2
                up_win2.title("List")
                up_main2=ttk.Frame(up_win2)
                self.up_main2=up_main2
                up_main2.grid(row=0,column=0,sticky=(tk.W, tk.E, tk.N, tk.S))
                ttk.Label(up_main2,text=m,font=("calibri",16)).grid(row=0,columnspan=2,column=0,sticky=tk.N,padx=30,pady=5)
                c=1
                self.val=[]
                def update_var(index):
                    self.val[index][0].set(not self.val[index][0].get())
                self.valu=tk.IntVar()
                for x in lines:
                    val=tk.BooleanVar(value=False)
                    list1=[val,x[0:-1]]
                    self.val.append(list1)
                    current_val=tk.IntVar(value=0)
                    current_val.set(c)
                    self.valu= current_val
                    live=ttk.Checkbutton(up_main2, text=x[0:-1],variable=self.valu,command=lambda c=c-1 : update_var(c)).grid(column=0, row=c,padx=30,pady=5,sticky=tk.W)
                    c+=1
                self.new_entry=[]
                self.count=c
                self.add_btn=ttk.Button(up_main2,text="Add item",command=self.add)
                self.add_btn.grid(row=c,column=0,padx=20,pady=5)
                self.sub_btn=ttk.Button(up_main2,text="Save",command=self.save)
                self.sub_btn.grid(row=c,column=1,padx=20,pady=5)
            elif self.mode=="delete":
                os.remove(n)
                messagebox.showinfo("Deleted",f"{m} named List Deleted Successfully")
                self.del_win.destroy()
        else:
            messagebox.showerror("Error",f"{m} named List does not Exist.")
            if self.mode=="view":
                self.view_win.destroy()
            elif self.mode=="delete":
                self.del_win.destroy()
            elif self.mode=="update":
                self.up_win.destroy()
        return
    def store(self):
        l=""
        c=1
        for x in self.task_entry:
            l=l+str(c)+". "+str(x.get())+'\n'
            c+= 1
        m=self.name_entry.get()
        n=m+'.txt'
        f=open(n,'w+')
        f.write(l)
        f.close()
        self.create_win2.destroy()
        self.create_win.destroy()
        messagebox.showinfo("Created","New list created Successfully.")
    def newwin(self):
        try:
            create_win2=tk.Tk()
            self.create_win2=create_win2
            create_win2.title(self.name_entry.get())
            create_main2=ttk.Frame(create_win2)
            create_main2.grid(row=0,column=0,sticky=(tk.W, tk.E, tk.N, tk.S))
            ttk.Label(create_main2,text="Enter the items of the list",font=("calibri",16)).grid(row=0,column=0,padx=30,pady=5)
            count=self.ntasks_entry.get()
            self.task_entry=[]
            for i in range(int(count)):
                task_entry=ttk.Entry(create_main2,width=35)
                task_entry.grid(row=i+1,column=0,padx=35,pady=5,sticky=tk.W)
                self.task_entry.append(task_entry)
            sub_btn=ttk.Button(create_main2,text="Save",command=self.store)
            sub_btn.grid(row=int(count)+1,column=0,padx=20,pady=5)
        except ValueError:
            self.create_win.destroy()
            self.create_win2.destroy()
            messagebox.showerror("Error","Enter At least one item.")
    def check(self):
        m=self.name_entry.get()
        n=m+'.txt'
        checking=os.path.exists(n)
        if checking ==False:
            self.newwin()
        else:
            messagebox.showerror("Error","List already Exist.")
            self.create_win.destroy()
    def create(self):
        create_win=tk.Tk()
        self.create_win=create_win
        create_win.title("New list")
        create_main=ttk.Frame(create_win)
        create_main.grid(row=0,column=0,sticky=(tk.W, tk.E, tk.N, tk.S))
        label=ttk.Label(create_main,text="Enter the name of the list",anchor="center",font=("calibri",16)).grid(row=0,columnspan=2,column=0,padx=30,pady=5)
        name_entry=ttk.Entry(create_main,width=35)
        name_entry.grid(row=1,columnspan=2,column=0,padx=35,pady=5,sticky=tk.W)
        self.name_entry=name_entry
        ttk.Label(create_main,text="Enter the number of items",font=("calibri",16)).grid(row=3,columnspan=2,column=0,sticky=tk.N)
        ntasks_entry=ttk.Entry(create_main,width=35)
        ntasks_entry.grid(row=4,columnspan=2,column=0,padx=35,pady=5,sticky=tk.W)
        self.ntasks_entry=ntasks_entry
        sub_btn=ttk.Button(create_main,text="Save",command=self.check)
        sub_btn.grid(row=5,column=0,padx=20,pady=5)
        self.window=create_win
        close_btn=ttk.Button(create_main,text="Close",command=self.close).grid(row=5,column=1,pady=10,padx=10)        
    def update(self):
        up_win=tk.Tk()
        self.up_win=up_win
        up_win.title("List")
        up_main=ttk.Frame(up_win)
        up_main.grid(row=0,column=0,sticky=(tk.W, tk.E, tk.N, tk.S))
        ttk.Label(up_main,text="Enter the name of the list",font=("calibri",16)).grid(row=0,columnspan=2,column=0,sticky=tk.N,padx=30,pady=5)
        name_entry=ttk.Entry(up_main,width=25)
        name_entry.grid(row=1,columnspan=2,column=0,padx=35,pady=5)
        self.name_entry=name_entry
        self.mode="update"
        sub_btn=ttk.Button(up_main,text="Enter",command=self.check1)
        sub_btn.grid(row=2,column=0,padx=20,pady=5)
        self.window=up_win
        close_btn=ttk.Button(up_main,text="Close",command=self.close).grid(row=2,column=1,pady=10,padx=10)
    def delete(self):
        del_win=tk.Tk()
        self.del_win=del_win
        del_win.title("List")
        del_main=ttk.Frame(del_win)
        del_main.grid(row=0,column=0,sticky=(tk.W, tk.E, tk.N, tk.S))
        ttk.Label(del_main,text="Enter the name of the list",font=("calibri",16)).grid(row=0,columnspan=2,column=0,sticky=tk.N,padx=30,pady=5)
        name_entry=ttk.Entry(del_main,width=25)
        name_entry.grid(row=1,columnspan=2,column=0,padx=35,pady=5)
        self.name_entry=name_entry
        self.mode="delete"
        sub_btn=ttk.Button(del_main,text="Enter",command=self.check1)
        sub_btn.grid(row=2,column=0,padx=20,pady=5)
        self.window=del_win
        close_btn=ttk.Button(del_main,text="Close",command=self.close).grid(row=2,column=1,pady=10,padx=10)

win=tk.Tk()
win.title("To Do List")
todolist(win)
win.mainloop()
