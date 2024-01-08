from tkinter import *
pro=Tk()
px = 10
py=30
txt0=StringVar
style="{arial} 12 bold "
pro.geometry('450x510')
c=Canvas(pro, bg="green").place(x=0, y=0 , width=450 , height=510)
btn_ac=Button(pro,text="AC", font=style , width=8, height=2, bg="red").grid(row=1,column=0, padx= px, pady= py)
b_ad=Button(pro,text="+", font=style , width=8, height=2, bg="yellow").grid(row=1,column=1, padx= px, pady= py)
b_sub=Button(pro,text="-", font=style , width=8, height=2, bg="yellow").grid(row=1,column=2, padx= px, pady= py)
b_mul=Button(pro,text="*", font=style , width=8, height=2, bg="yellow").grid(row=1,column=3, padx= px, pady= py)
b_1=Button(pro,text="1", font=style , width=8, height=2, bg="yellow").grid(row=2,column=0, padx= px, pady= py)
b_2=Button(pro,text="2", font=style , width=8, height=2, bg="yellow").grid(row=2,column=1, padx= px, pady= py)
b_3=Button(pro,text="3", font=style , width=8, height=2, bg="yellow").grid(row=2,column=2, padx= px, pady= py)
b_4=Button(pro,text="4", font=style , width=8, height=2, bg="yellow").grid(row=2,column=3, padx= px, pady= py)
b_5=Button(pro,text="5", font=style , width=8, height=2, bg="yellow").grid(row=3,column=0, padx= px, pady= py)
b_6=Button(pro,text="6", font=style , width=8, height=2, bg="yellow").grid(row=3,column=1, padx= px, pady= py)
b_7=Button(pro,text="7", font=style , width=8, height=2, bg="yellow").grid(row=3,column=2, padx= px, pady= py)
b_8=Button(pro,text="8", font=style , width=8, height=2, bg="yellow").grid(row=3,column=3, padx= px, pady= py)
b_9=Button(pro,text="9", font=style , width=8, height=2, bg="yellow").grid(row=4,column=0, padx= px, pady= py)
b_0=Button(pro,text="0", font=style , width=8, height=2, bg="yellow").grid(row=4,column=1, padx= px, pady= py)
b_div=Button(pro,text="/", font=style , width=8, height=2, bg="yellow").grid(row=4,column=2, padx= px, pady= py)
b_equal=Button(pro,text="=", font=style , width=8, height=2, bg="yellow").grid(row=4,column=3, padx= px, pady= py)
etr=Entry(pro,font="{arial} 18 bold" ,textvariable=txt0,width=31).grid(row=0,columnspan=4,pady=12)

pdx=20
pro.mainloop()
