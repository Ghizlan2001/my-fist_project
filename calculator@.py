from tkinter import *
root = Tk()
root.geometry("360x420")
root.title("Calculator")
# root.configure(bg="#17161b")

current=""
def Click(value):
    global current
    current += value
    label.config(text=current)

def Clear():
    global current
    current=""
    label.config(text=current)

def sum():
    global current
    result=""
    if current !="":
        try:
            result = eval(current)
        except:
            result = "error"
            current = ""
    label.config(text= result)

    


label = Label(root, text="",bd=10, font=("Arial", 24), width=18, height=2,bg="#fff", justify="right")
label.grid(columnspan=6)
btn1 = Button(root, text="1",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("1"))
btn1.grid(row=4, column=0)
btn2 = Button(root, text="2",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("2"))
btn2.grid(row=4, column=1)
btn3 = Button(root, text="3",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("3"))
btn3.grid(row=4, column=2)
btn4 = Button(root, text="4",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("4"))
btn4.grid(row=3, column=0)
btn5 = Button(root, text="5",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("5"))
btn5.grid(row=3, column=1)
btn6 = Button(root, text="6",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("6"))
btn6.grid(row=3, column=2)
btn7 = Button(root, text="7",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command =lambda:Click("7"))
btn7.grid(row=2, column=0)
btn8 = Button(root, text="8",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("8"))
btn8.grid(row=2, column=1)
btn9 = Button(root, text="9",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("9"))
btn9.grid(row=2, column=2)
btn0 = Button(root, text="0",bd=1, width=4,padx=45, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("0"))
btn0.grid(row=5, column=0,columnspan=2)
btn_plus = Button(root, text="+", bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("+"))
btn_plus.grid(row=2, column=3)
btn_minus = Button(root, text="-", bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("-"))
btn_minus.grid(row=3, column=3)
btn_multiple = Button(root, text="*", bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("*"))
btn_multiple.grid(row=1, column=3)
btn_div = Button(root, text="/", bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command = lambda:Click("/"))
btn_div.grid(row=1, column=2)
btn_equal = Button(root, text="=", bd=1,pady=14.5, width=4, height=2,font=("Arial", 25, "bold"),fg="#fff",bg="violet", command =sum)
btn_equal.grid(row=4, column=3, rowspan=2)
btn_point = Button(root, text=".", bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b",command= lambda:Click("."))
btn_point.grid(row=5, column=2)
btn_clear = Button(root, text="C",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="pink",command= Clear)
btn_clear.grid(row=1, column=0)
btn_pour = Button(root,text="%",bd=1, width=4, height=1,font=("Arial", 25, "bold"),fg="#fff",bg="#17161b", command=lambda:Click("%"))
btn_pour.grid(row=1, column=1)

root.mainloop()