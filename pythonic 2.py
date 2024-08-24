from tkinter import *
top=Tk()
top.geometry("1400x800")
top.title("VICKY")
top.config(bg="grey")
welcome=Label(top,text="welcome to our page",font=("Timesnewroman",30,"bold"))
welcome.place(x=500,y=120)
def login():
    get=Frame(top,bg="black",height=700,width=400)
    get.pack(fill=X)
    num=Label(top,text="P L E A S E   L O G I N",font=("TimesNew Roman",30,"bold"),bg="grey",fg="white")
    num.place(x=500,y=50)
    user=Label(top,text="user name",font=("TimesNew Roman",30,"italic"),bg="grey",fg="black")
    user.place(x=500,y=400)
    password=Label(top,text="password",font=("TimesNew Roman",30,"italic"),bg="grey",fg="black")
    password.place(x=500,y=500)
    box=Entry(top,text="",font=("TimeNewRoman",30,"italic"),fg="black",)
    box.place(x=700,y=400,width=200,height=50)
    ox=Entry(top,text="",font=("TimeNewRoman",30,"italic"),fg="black",)
    ox.place(x=700,y=500,width=200,height=50)
    button=Button(top,text="login",font=("TimeNewRoman",30,"italic"),bg="black",fg="white",activebackground="yellow",activeforeground="red",command=login)
    button.place(x=600,y=600,width=200,height=100)

button=Button(top,text="Get start",font=("TimeNewRoman",30,"italic"),bg="black",fg="white",activebackground="yellow",activeforeground="red",command=login)
button.place(x=600,y=550,width=200,height=100)








=====
