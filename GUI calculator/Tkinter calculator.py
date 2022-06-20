from  tkinter import *
top =Tk()
top.iconbitmap('calculator.ico')
top.title("calculator")
operation=Entry(top,width=35,borderwidth=5,bg="black",fg="white")
operation.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
# buttons label
def buttonadd(number):
    current=operation.get()
    operation.delete(0,END)
    operation.insert(0,str(current)+str(number))
   
def clear_button():
    operation.delete(0,END)



def button_equal():
    num2=float(operation.get())
    if math=="addition":
        addi=str(first_num+num2)
        operation.delete(0,END)
        operation.insert(0,addi)
    if math=="subtraction":
        sub=str(first_num-num2)
        operation.delete(0,END)
        operation.insert(0,sub)
    if math=="multiplication":
        mul=str(first_num*num2)
        operation.delete(0,END)
        operation.insert(0,mul)
    if math=="division":
        div=str(first_num  /  num2)
        operation.delete(0,END)
        operation.insert(0,div)

def button_add():
    global  first_num
    global math
    math="addition"
    first_num=float(operation.get())
    operation.delete(0,END)


def button_subtract():
    global  first_num
    global math
    math="subtraction"
    first_num=float(operation.get())
    operation.delete(0,END)

def button_multiply():
    global  first_num
    global math
    math="multiplication"
    first_num=float(operation.get())
    operation.delete(0,END)

def button_divide():
    global  first_num
    global math
    math="division"
    first_num=float(operation.get())
    operation.delete(0,END)

def button_point():
    
     current=operation.get()
     operation.delete(0,END)
     point=str(current)+"."
     operation.insert(0,point)

    

# make buttons

one=Button(top,text="1",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(1))
two=Button(top,text="2",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(2))
three=Button(top,text="3",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(3))
four=Button(top,text="4",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(4))
five=Button(top,text="5",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(5))
six=Button(top,text="6",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(6))
seven=Button(top,text="7",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(7))
eight=Button(top,text="8",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(8))
nine=Button(top,text="9",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(9))
zero=Button(top,text="0",padx=40,pady=20,bg="black",fg="white",command=lambda:buttonadd(0))
add=Button(top,text="+",padx=42,pady=41,bg="blue",fg="white",command=button_add)
equal=Button(top,text="=",padx=93,pady=41,bg="blue",fg="white",command=button_equal)
clear=Button(top,text="Clear",padx=79,pady=20,bg="red",fg="white",command=clear_button)
subtract=Button(top,text="-",padx=44,pady=25,bg="blue",fg="white",command=button_subtract)
multiply=Button(top,text="*",padx=44,pady=25,bg="blue",fg="white",command=button_multiply)
divide=Button(top,text="/",padx=44,pady=25,bg="blue",fg="white",command=button_divide)
point=Button(top,text=".",padx=40,pady=20,bg="blue",fg="white",command=button_point)

# show buttons
one.grid(row=3, column=0)
two.grid(row=3, column=1)
three.grid(row=3, column=2)

four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)

seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)

zero.grid(row=4, column=0)
clear.grid(row=4, column=1, columnspan=2)
add.grid(row=5, column=0)
equal.grid(row=5, column=1, columnspan=2)

subtract.grid(row=6, column=0)
multiply.grid(row=6, column=1)
divide.grid(row=6, column=2)

# point.grid(row=4,column=0)



top.mainloop()