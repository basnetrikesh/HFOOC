from tkinter import*
from PIL import Image,ImageTk
import os
def start_button_click():
    win.destroy()
    os.system("python main.py")
win=Tk()
win.title("HFOOC")
win.geometry("1020x720")
win.configure(bg="black")
l1=Label(win,text="HANDS-FREE OPERATION OF COMPUTER",bg="black",fg="white",font=("Courier", 20))
l1.pack() 
photo=ImageTk.PhotoImage(Image.open("PRETRAINED_MODELS\\1.jpg"))
frame1 = Frame(win, width=100, height=100)
frame1.pack()
l2=Label(frame1,image=photo)
l2.pack()
l3=Label(text="Project By:",bg="black",fg="white",font=("Courier", 15))
l3.pack()
l4=Label(text="Rajan Ghimire[54-BCT-074]",bg="black",fg="white",font=("Courier", 12))
l4.pack()
l5=Label(text="Raul Shahi[57-BCT-074]",bg="black",fg="white",font=("Courier", 12))
l5.pack()
l6=Label(text="Rikesh Basnet[61-BCT-074]",bg="black",fg="white",font=("Courier", 12))
l6.pack()
l7=Label(text="Sarina Joshi[75-BCT-074]",bg="black",fg="white",font=("Courier", 12))
l7.pack()
start_button=Button(text="START",bg="white",fg="black",command=start_button_click)
start_button.pack(pady=30)

win.mainloop()

