from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo

import mysql.connector

def file_browse():
    name_file = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("Text files",
    "*.txt"), ("all files", "*.*")))

    showinfo(
        title='Selected File',
        message=name_file
    )



def feed_inputs():
    window = Tk()
    window.title("Feed Inputs")
    window.geometry("500x500")

    heading = Label(window,text="Feeds Input",bg="grey",fg="white",font="40",width="500",height="3")
    heading.pack()

    # global imah_fileSelected 
    # imah_fileSelected = Label(window, text = "demo").place(x="300", y="350")
    # global ctc_fileSelected 
    # ctc_fileSelected = Label(window, text= "demo").place(x="300", y = "400")
    #-----------------------------------------------------------------------------------------------------------
#Lables

    kriType_text = Label(window,text="KRI Type : ")
    cob_text = Label(window,text="COB : ")
    riskIndicator_text = Label(window,text="Risk Indicator : ")
    srcSystem_text = Label(window,text="Source System : ")
    feedLocation_text = Label(window,text="Feed Location : ")
    imah_file = Label(window, text = "IMAH File : " ).place(x="15", y="350")
    ctc_file = Label(window, text = "CTC File : " ).place(x="15", y="400")

    kriType_text.place(x="15",y="100")
    cob_text.place(x="15",y="150")
    riskIndicator_text.place(x="15",y="200")
    srcSystem_text.place(x="15",y="250")
    feedLocation_text.place(x="15",y="300")

#------------------------------------------------------------------------------------------------------------
#FeedInput

    kriType = StringVar()
    cob = StringVar()
    riskIndicator = StringVar()
    srcSystem = StringVar()
    feedLocation = StringVar()

    kriType_entry = Entry(window,textvariable=kriType,width="30")
    cob_entry = Entry(window,textvariable=cob,width="30")
    riskIndicator_entry = Entry(window,textvariable=riskIndicator,width="30")
    srcSystem_entry = Entry(window,textvariable=srcSystem,width="30")
    feedLocation_entry = Entry(window,textvariable=feedLocation,width="30")

    kriType_entry.place(x="115",y="103")
    cob_entry.place(x="115",y="153")
    riskIndicator_entry.place(x="115",y="203")
    srcSystem_entry.place(x="115",y="253")
    feedLocation_entry.place(x="115",y="303")

   

#----------------------------------------------------------------------------------------------------------
#Button
    imah_button = Button(window, text="Browse IMAH .csv file" , width="20",  bg="grey" , fg="black" , command=file_browse)
    ctc_button = Button(window, text="Browse CTC .csv file" , width="20",  bg="grey" , fg="black" , command=file_browse)
    button = Button(window, text="Submit" , width="12",  bg="brown" , fg="white" , command='')
    imah_button.place(x="115", y="350")
    ctc_button.place(x="115", y="400")
    button.place(x="35",y="450")

def sql_login_info():
    userName_info = userName.get()
    password_info = password.get()
    hostName_info = hostName.get()
    port_info = port.get()
    serviceName_info = serviceName.get()
        
    print(userName_info)
    print(password_info)
    print(hostName_info)
    print(port_info)
    print(serviceName_info)
    
    conn = mysql.connector.connect(host= hostName_info , password = password_info , user = userName_info )
    if conn.is_connected():
        print("Connection established...")
  

app = Tk()

app.geometry("500x500")

app.title("SQL Server Login")

heading = Label(text="SQL Server Login",bg="grey",fg="white",font="40",width="500",height="3")
heading.pack()
#-----------------------------------------------------------------------------------------------------------
#Labels

userName_text = Label(text="User Name : ")
password_text = Label(text="Password : ")
hostName_text = Label(text="Host Name : ")
port_text = Label(text="Port : ")
serviceName_text = Label(text="Service Name : ")

userName_text.place(x="15",y="100")
password_text.place(x="15",y="150")
hostName_text.place(x="15",y="200")
port_text.place(x="15",y="250")
serviceName_text.place(x="15",y="300")


#-----------------------------------------------------------------------------------------------------------
#SQLEntry

userName = StringVar()
password = StringVar()
hostName = StringVar()
port = IntVar()
serviceName = StringVar()

userName_entry = Entry(textvariable=userName,width="30")
password_entry = Entry(textvariable=password,width="30")
hostName_entry = Entry(textvariable=hostName,width="30")
port_entry = Entry(textvariable=port,width="30")
serviceName_entry = Entry(textvariable=serviceName,width="30")

userName_entry.place(x="115",y="103")
password_entry.place(x="115",y="153")
hostName_entry.place(x="115",y="203")
port_entry.place(x="115",y="253")
serviceName_entry.place(x="115",y="303")


#-----------------------------------------------------------------------------------------------------------
#Button

button = Button(app , text="Submit" , width="12" , bg="brown" , fg="white" , command=sql_login_info)
button.place(x="35",y="370")

Test = Button(app , text="Navigate" , width="12" , bg="brown" , fg="white" , command=feed_inputs)
Test.place(x="145",y="370")


mainloop()