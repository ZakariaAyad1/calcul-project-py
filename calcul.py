from tkinter import *
from tkinter import Tk, StringVar, Button
pro=Tk()
px = 10
py=30
txt0 = StringVar()
a=0
b=0

def ad():
    global op
    global b
    b=a
    op="+"

def sub():
    global op
    global b
    b=a
    op="-"
def mul():
    global op
    global b
    b=a
    op="*"
def div():
    global op
    global b
    b=a
    op="/"

def equal():
    if (op=="+"):
        rslt=a+b
        txt0.set(rslt)    
    if (op=="-"):
        rslt=b-a
        txt0.set(rslt)
    if (op=="*"):
        rslt=a*b
        txt0.set(rslt)
    if (op=="/"):
        rslt=a/b
        txt0.set(rslt)
 










def dlt():
    txt0.set(" ")

def tap0():
    global a
    a=0
    txt0.set(str(a))

def tap1():
    global a
    a=1
    txt0.set(str(a))

def tap2():
    global a
    a=2
    txt0.set(str(a))

def tap3():
    global a
    a=3
    txt0.set(str(a))

def tap4():
    global a
    a=4
    txt0.set(str(a))

def tap5():
    global a
    a=5
    txt0.set(str(a))

def tap6():
    global a
    a=6
    txt0.set(str(a))

def tap7():
    global a
    a=7
    txt0.set(str(a))

def tap8():
    global a
    a=8
    txt0.set(str(a))

def tap9():
    global a
    a=9
    txt0.set(str(a))



style="{arial} 12 bold "

pro.geometry('450x510')
c=Canvas(pro, bg="green").place(x=0, y=0 , width=450 , height=510)
btn_ac=Button(pro, command=dlt,text="AC", font=style , width=8, height=2, bg="red").grid(row=1,column=0, padx= px, pady= py)
b_ad=Button(pro, command=ad , text="+", font=style , width=8, height=2, bg="yellow").grid(row=1,column=1, padx= px, pady= py)
b_sub=Button(pro, command=sub , text="-", font=style , width=8, height=2, bg="yellow").grid(row=1,column=2, padx= px, pady= py)
b_mul=Button(pro, command=mul , text="*", font=style , width=8, height=2, bg="yellow").grid(row=1,column=3, padx= px, pady= py)
b_1=Button(pro,  command=tap1 , text="1", font=style , width=8, height=2, bg="yellow").grid(row=2,column=0, padx= px, pady= py)
b_2=Button(pro, command=tap2 ,text="2", font=style , width=8, height=2, bg="yellow").grid(row=2,column=1, padx= px, pady= py)
b_3=Button(pro, command=tap3 ,text="3", font=style , width=8, height=2, bg="yellow").grid(row=2,column=2, padx= px, pady= py)
b_4=Button(pro, command=tap4 ,text="4", font=style , width=8, height=2, bg="yellow").grid(row=2,column=3, padx= px, pady= py)
b_5=Button(pro, command=tap5 ,text="5", font=style , width=8, height=2, bg="yellow").grid(row=3,column=0, padx= px, pady= py)
b_6=Button(pro, command=tap6 ,text="6", font=style , width=8, height=2, bg="yellow").grid(row=3,column=1, padx= px, pady= py)
b_7=Button(pro, command=tap7 ,text="7", font=style , width=8, height=2, bg="yellow").grid(row=3,column=2, padx= px, pady= py)
b_8=Button(pro, command=tap8 ,text="8", font=style , width=8, height=2, bg="yellow").grid(row=3,column=3, padx= px, pady= py)
b_9=Button(pro, command=tap9 ,text="9", font=style , width=8, height=2, bg="yellow").grid(row=4,column=0, padx= px, pady= py)
b_0=Button(pro, command=tap0 ,text="0", font=style , width=8, height=2, bg="yellow").grid(row=4,column=1, padx= px, pady= py)
b_div=Button(pro, command=div ,  text="/", font=style , width=8, height=2, bg="yellow").grid(row=4,column=2, padx= px, pady= py)
b_equal=Button(pro, command=equal ,  text="=", font=style , width=8, height=2, bg="yellow").grid(row=4,column=3, padx= px, pady= py)
etr=Entry(pro,font="{arial} 18 bold" ,textvariable=txt0,width=31).grid(row=0,columnspan=4,pady=12)

pdx=20
pro.mainloop()
