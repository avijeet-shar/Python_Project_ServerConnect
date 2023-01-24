from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import os
import shutil
from output import output

def resultWindow():
    output()
    feed_inputs.window.destroy()


#----------------------------------------------------------------------------------------------------------
#Submit Function
def save_info():
    create_new_dir()
    copyFiles()
    

#----------------------------------------------------------------------------------------------------------
#Copy File from destination and paste it in Server Files Folder

def copyFiles():
    path = '/home/User/Documents'
 
# Source path
    source = file_browse.name_file
    filename = os.path.basename(source)
    print(filename)
    print(source)
 
# Destination path
    destination = os.getcwd() + "\serverFiles" + "/" + filename
    print(destination)
 
# Copy the content of
# source to destination
    dest = shutil.copyfile(source, destination)
 
# Print path of newly
# created file
    print("Destination path:", dest)    


#------------------------------------------------------------------------------------------------------
#Creating a folder

def create_new_dir():
    dirName = os.getcwd() + "\serverFiles"
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok=True)

#------------------------------------------------------------------------------------------------------
#Browse File Popup    

def file_browse():
    file_browse.name_file = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("Text files",
    "*.txt"), ("all files", "*.*")))

    showinfo(
        title='Selected File',
        message=file_browse.name_file
    )
    save_info()
#-------------------------------------------------------------------------------------------------------
#Feed Input Function
    
def feed_inputs():
    feed_inputs.window = Tk()
    feed_inputs.window.title("Feed Inputs")
    feed_inputs.window.geometry("500x500")

    heading = Label(feed_inputs.window,text="Feeds Input",bg="grey",fg="white",font="40",width="500",height="3")
    heading.pack()

    # global imah_fileSelected 
    # imah_fileSelected = Label(window, text = "demo").place(x="300", y="350")
    # global ctc_fileSelected 
    # ctc_fileSelected = Label(window, text= "demo").place(x="300", y = "400")
#-----------------------------------------------------------------------------------------------------------
#Lables

    kriType_text = Label(feed_inputs.window,text="KRI Type : ")
    cob_text = Label(feed_inputs.window,text="COB : ")
    riskIndicator_text = Label(feed_inputs.window,text="Risk Indicator : ")
    srcSystem_text = Label(feed_inputs.window,text="Source System : ")
    feedLocation_text = Label(feed_inputs.window,text="Feed Location : ")
    imah_file = Label(feed_inputs.window, text = "IMAH File : " ).place(x="15", y="350")
    ctc_file = Label(feed_inputs.window, text = "CTC File : " ).place(x="15", y="400")

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

    kriType_entry = Entry(feed_inputs.window,textvariable=kriType,width="30")
    cob_entry = Entry(feed_inputs.window,textvariable=cob,width="30")
    riskIndicator_entry = Entry(feed_inputs.window,textvariable=riskIndicator,width="30")
    srcSystem_entry = Entry(feed_inputs.window,textvariable=srcSystem,width="30")
    feedLocation_entry = Entry(feed_inputs.window,textvariable=feedLocation,width="30")

    kriType_entry.place(x="115",y="103")
    cob_entry.place(x="115",y="153")
    riskIndicator_entry.place(x="115",y="203")
    srcSystem_entry.place(x="115",y="253")
    feedLocation_entry.place(x="115",y="303")
#--------------------------------------------------------------------------------------------------------------
#Button
    imah_button = Button(feed_inputs.window, text="Browse IMAH .csv file" , width="20",  bg="grey" , fg="black" , command=file_browse)
    ctc_button = Button(feed_inputs.window, text="Browse CTC .csv file" , width="20",  bg="grey" , fg="black" , command=file_browse)
    button = Button(feed_inputs.window, text="Submit" , width="12",  bg="brown" , fg="white" , command=resultWindow)
    imah_button.place(x="115", y="350")
    ctc_button.place(x="115", y="400")
    button.place(x="170",y="450")

   