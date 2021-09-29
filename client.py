#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea = None
labelchat = None
text_message = None

def connectToServer():
    global SERVER
    global name

    cname = name.get()
    SERVER.send(cname.encode('utf8'))


def musicWindow():

    global song_counter
    global listbox
    global filePathLabel
    global infoLabel

    window=Tk()
    window.title('Music Window')
    window.geometry("300x350")
    window.configure(bg = 'LightSkyBlue')
    
    selectLabel = Label(window, text= "Select Song", bg = 'LightSkyBlue', font = ("Calibri",8))
    selectLabel.place(x=2, y=1)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=20)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="Play",bd=1, font = ("Calibri",10))
    playButton.place(x=30,y=200)

    Stop=Button(window,text="Stop",bd=1, font = ("Calibri",10))
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Refresh",bd=1, font = ("Calibri",10))
    Upload.place(x=30,y=250)

    Download=Button(window,text="Download",bd=1, font = ("Calibri",10))
    Download.place(x=200,y=250)

    InfoLabel = Label(window, text = "Info Label", font = ("Calibri",10))
    InfoLabel.place(x=30, y = 280)
    
    #filePathLabel = Label(window, text="", fg = "blue", font = ("Calibri",8))
    #filePathLabel.place(x=10, y = 330)

    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()
