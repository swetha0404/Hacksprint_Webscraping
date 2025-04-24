# on Button click reading and displaying date selection
from tkinter import *
from tkcalendar import DateEntry 
import pandas as pd
import numpy as np
from datetime import datetime 


my_w = Tk()
my_w.geometry("770x433")
my_w.title("Hacksprint") 

img = PhotoImage(file="G:/HackSprint 3.0/background.png")
label = Label(
    my_w,
    image=img
)
label.place(x=-2, y=0)
Label(my_w,text= "Commodity Price Prediction",font=('Calibri',20)).place(x=235,y=0)
Label(my_w,text= "Crude Oil",font=('Calibri',15)).place(x=340,y=70)

Label(my_w, text= "Choose a Date",font=('Calibri',13), background= 'gray61', foreground="white").place(x=245,y=145)
cal=DateEntry(my_w,selectmode='day',font=('Calibri',13),date_pattern='dd-mm-YYYY',width= 16, background= "magenta3", foreground= "white",bd=2)
cal.place(x=365,y=145)

def my_upd(): # triggered on Button Click
    dt=cal.get_date()
    selected_date=dt.strftime("%d-%m-%Y") #format to change 
    print(selected_date)
    l1.config(text=selected_date) # read and display date
   
    dataframe = pd.read_csv("C:/Users/Chandramouleesvar V/Hacksprint/OutputDataFrame.csv")
    
    for i in range(len(dataframe['Date'])): 
        new_date = datetime.strptime(dataframe['Date'][i], '%d-%m-%Y')
        new_date=str(new_date)[:10]
        new_date=new_date.split('-')
        new_date.reverse()
        new_date='-'.join(new_date)       
        
        
        if selected_date == new_date:
            print(selected_date,new_date)
            l2.config(text=dataframe['Close Price'][i])            
            break

        else: 
            l2.config(text='Data Unavailable')
            
            



b1=Button(my_w,text='Get Price',font=('Calibri',12), command=lambda:my_upd())
b1.place(x=260,y=190)

l1=Label(my_w,text='                   ',font=('Calibri',13))  # Label to display date 
l1.place(x=400,y=190)

Label(my_w,text='Closing Price',font=('Calibri',13),background= 'gray61', foreground="white").place(x=250,y=245)
l2=Label(my_w,text='               ',font=('Calibri',13))
l2.place(x=410,y=245)


Label(my_w,text=' CodePlay ',font=('Calibri',15)).place(x=670,y=395)
my_w.mainloop()

