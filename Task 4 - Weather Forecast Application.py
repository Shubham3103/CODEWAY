import tkinter as tk
from tkinter import ttk, messagebox
import requests
import datetime as dt

class weather_forecast:
    def __init__(self,main):
        self.main=main
        self.window=self.main
        self.frame_main=ttk.Frame(main)
        self.frame_main.grid(row=0,column=0,sticky=(tk.W, tk.E, tk.N, tk.S))
        ttk.Label(self.frame_main,text="Weather Forecast Application",font=("calibri",18)).grid(row=0,columnspan=2,column=0,pady=5,padx=30)
        ttk.Label(self.frame_main,text="Enter the name or zip code of the city",font=("calibri",16)).grid(row=1,columnspan=2,column=0,sticky=tk.N,padx=30,pady=5)
        name_entry=ttk.Entry(self.frame_main,width=25)
        name_entry.grid(row=2,columnspan=2,column=0,padx=35,pady=5)
        self.name_entry=name_entry
        sub_btn=ttk.Button(self.frame_main,text="Enter",command=self.enter)
        sub_btn.grid(row=3,column=0,padx=10,pady=5)
        close_btn=ttk.Button(self.frame_main,text="Close",command=self.close).grid(row=3,column=1,pady=10,padx=10)
    def enter(self):
        city=self.name_entry.get()
        try:
            api='6ad90e1ce8dd3601e2534b8eb9a1754e' 
            try:
                zip_code=int(city)
                zip_code=str(zip_code)
                self.url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&appid={api}&units=metric"
            except:
                self.url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
                city=city.upper()
                pass
            response=requests.get(self.url).json()
            description=str(response['weather'][0]['description'])
            temperature=str(response['main']['temp'])+"°C"
            humidity=str(response['main']['humidity'])+"%"
            time=dt.date.today()
            time=str(time)
            date=time
            self.win2=tk.Tk()
            self.win2.title("Weather Forecast Application")
            self.frame_main2=ttk.Frame(self.win2)
            self.frame_main2.grid(row=0,column=0,sticky=(tk.W, tk.E, tk.N, tk.S))
            ttk.Label(self.frame_main2,text=city,font=("calibri",18)).grid(row=0,columnspan=3,column=0,pady=5,padx=30)
            ttk.Label(self.frame_main2,text="Weather Report",font=("calibri",16)).grid(row=1,columnspan=3,column=0,sticky=tk.N,padx=30,pady=5)
            ttk.Label(self.frame_main2,text="Date",font=("calibri",16)).grid(row=2,column=0,sticky=tk.W,padx=30,pady=5)
            ttk.Label(self.frame_main2,text=": ",font=("calibri",16)).grid(row=2,column=1,sticky=tk.W,padx=5,pady=5)
            ttk.Label(self.frame_main2,text=date,font=("calibri",16)).grid(row=2,column=2,sticky=tk.W,padx=30,pady=5)
            ttk.Label(self.frame_main2,text="Temperature",font=("calibri",16)).grid(row=3,column=0,sticky=tk.W,padx=30,pady=5)
            ttk.Label(self.frame_main2,text=": ",font=("calibri",16)).grid(row=3,column=1,sticky=tk.W,padx=5,pady=5)
            ttk.Label(self.frame_main2,text=temperature,font=("calibri",16)).grid(row=3,column=2,sticky=tk.W,padx=30,pady=5)
            ttk.Label(self.frame_main2,text="Humidity",font=("calibri",16)).grid(row=4,column=0,sticky=tk.W,padx=30,pady=5)
            ttk.Label(self.frame_main2,text=": ",font=("calibri",16)).grid(row=4,column=1,sticky=tk.W,padx=5,pady=5)
            ttk.Label(self.frame_main2,text=humidity,font=("calibri",16)).grid(row=4,column=2,sticky=tk.W,padx=30,pady=5)
            ttk.Label(self.frame_main2,text="Description",font=("calibri",16)).grid(row=5,column=0,sticky=tk.W,padx=30,pady=5)
            ttk.Label(self.frame_main2,text=": ",font=("calibri",16)).grid(row=5,column=1,sticky=tk.W,padx=5,pady=5)
            ttk.Label(self.frame_main2,text=description,font=("calibri",16)).grid(row=5,column=2,sticky=tk.W,padx=30,pady=5)
            close_btn=ttk.Button(self.frame_main2,text="Close",command=self.close).grid(row=6,columnspan=3,column=0,pady=10,padx=10)
            self.window=self.win2
        except requests.ConnectionError:
            messagebox.showerror("Error","You are offline. Please check your internet connection.")
        except Exception as e:
            messagebox.showerror("Error",f"An unexpected error occured {str(e)}")
    def close(self):
        try:
            if self.window==self.win2:
                self.window.destroy()
                self.window=self.main
            else:
                self.window.destroy()
        except:
            self.window.destroy()
win=tk.Tk()
win.title("Weather Forecast Application")
weather_forecast(win)
win.mainloop()