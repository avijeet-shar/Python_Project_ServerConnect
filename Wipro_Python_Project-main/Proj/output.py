from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo


def close():
    output.window.destroy()
    
    
def output():
    output.window = Tk()
    output.window.title("Output window")
    output.window.geometry("500x500")

    heading = Label(output.window,text="Output window",bg="grey",fg="white",font="40",width="500",height="3")
    heading.pack()

    comment = Label(output.window,text="Here the compared output will be shown!!", bg="green", fg="black", font="20")
    comment.place(x="90", y="250")
    

    button = Button(output.window, text="Close" , width="12",  bg="brown" , fg="white" , command=close)
    button.place(x="170",y="450")