                                #Task - 2 (#CODESOFT - PYTHON PROGRAMMING INTERNSHIP)

import tkinter as tk

#functions numbers
def num0():
    entry.insert(tk.END,"0")
def num1():
    entry.insert(tk.END,"1")
def num2():
    entry.insert(tk.END,"2")
def num3():
    entry.insert(tk.END,"3")
def num4():
    entry.insert(tk.END,"4")
def num5():
    entry.insert(tk.END,"5")
def num6():
    entry.insert(tk.END,"6")
def num7():
    entry.insert(tk.END,"7")
def num8():
    entry.insert(tk.END,"8")
def num9():
    entry.insert(tk.END,"9")

#function caluclations
def Add():
    entry.insert(tk.END,"+")
def Sub():
    entry.insert(tk.END,"-")
def Mul():
    entry.insert(tk.END,"*")
def Div():
    entry.insert(tk.END,"/")
def Mod():
    entry.insert(tk.END,"%")
def Pow():
    entry.insert(tk.END,"^")
def clear():
    entry.delete(0,tk.END)
def dele():
    value = entry.get()
    entry.delete(len(value)-1,tk.END)

#caluclation part function
def caluclate():
    value = entry.get()
    if '+' in value:
        text = value.split('+') 
        num1 = int(text[0])
        num2 = int(text[1])
        result = num1+num2
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    elif '*' in value:
        text = value.split('*')
        num1 = int(text[0])
        num2 = int(text[1])
        result = num1*num2
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    elif '/' in value:
        text = value.split('/')
        num1 = int(text[0])
        num2 = int(text[1])
        result = num1/num2
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    elif '-' in value:
        text = value.split('-')
        num1 = int(text[0])
        num2 = int(text[1])
        result = num1-num2
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    elif '%' in value:
        text = value.split('%')
        num1 = int(text[0])
        num2 = int(text[1])
        result = num1%num2
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    elif '^' in value:
        text = value.split('^')
        num1 = int(text[0])
        num2 = int(text[1])
        result = num1^num2
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    else:
        Res.config(tk.DISABLED)
          
root = tk.Tk()
root.geometry("400x400")
root.title("CALUCLATOR")
root.resizable(False,False)
entry = tk.Entry(root,width=45,highlightbackground="white",bd=5,highlightcolor="black")
entry.place(x=50,y=50)


#number buttons
delete = tk.Button(root,text="X",command=dele,width=2,height=1,bg="red",fg="black",borderwidth=2,border=1,bd=2)
delete.place(x=350,y=48)
button7 = tk.Button(root,text="7",command=num7,width=6,bd=3)
button7.place(x=50,y=100)
button8 = tk.Button(root,text="8",command=num8,width=6,bd=3)
button8.place(x=110,y=100)
button9 = tk.Button(root,text="9",command=num9,width=6,bd=3)
button9.place(x=170,y=100)
button4 = tk.Button(root,text="4",command=num4,width=6,bd=3)
button4.place(x=50,y=140)
button5 = tk.Button(root,text="5",command=num5,width=6,bd=3)
button5.place(x=110,y=140)
button6 = tk.Button(root,text="6",command=num6,width=6,bd=3)
button6.place(x=170,y=140)
button3 = tk.Button(root,text="3",command=num3,width=6,bd=3)
button3.place(x=50,y=180)
button2 = tk.Button(root,text="2",command=num2,width=6,bd=3)
button2.place(x=110,y=180)
button1 = tk.Button(root,text="1",command=num1,width=6,bd=3)
button1.place(x=170,y=180)
button0 = tk.Button(root,text="0",command=num0,width=18,bd=3)
button0.place(x=70,y=220)

# Arithmetic buttons 
Add = tk.Button(root,text="+",command=Add,width="8",bd=3)
Add.place(x=235,y=100)
Sub = tk.Button(root,text="-",command=Sub,width="8",bd=3)
Sub.place(x=310,y=100)
Mul = tk.Button(root,text="*",command=Mul,width="8",bd=3)
Mul.place(x=235,y=140)
Div = tk.Button(root,text="/",command=Div,width="8",bd=3)
Div.place(x=310,y=140)
Mod = tk.Button(root,text="%",command=Mod,width="8",bd=3)
Mod.place(x=235,y=180)
Pow = tk.Button(root,text="^",command=Pow,width="8",bd=3)
Pow.place(x=310,y=180)
clear = tk.Button(root,text="C",command=clear,width="12",bd=3)
clear.place(x=250,y=220)
Res = tk.Button(root,text="=",command=caluclate,width="30",bg="green",borderwidth=5,bd=3)
Res.place(x=85,y=260)
root.mainloop()