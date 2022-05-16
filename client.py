from tkinter import *
from tkinter import ttk
import socket
import threading
import pyaudio

global port

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
        while 1:
            try:
                self.target_ip = e1
                self.target_port = int(e2)
                self.s.connect((self.target_ip, self.target_port))
                break
            except:
                print("Couldn't connect to server")

        chunk_size = 1024 # 512
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 20000

        # initialise microphone recording
        self.p = pyaudio.PyAudio()
        self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size)
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)
        
        print("Connected to Server")

        # start threads
        receive_thread = threading.Thread(target=self.receive_server_data).start()
        self.send_data_to_server()

    def receive_server_data(self):
        while True:
            try:
                data = self.s.recv(1024)
                self.playing_stream.write(data)
            except:
                pass

    def send_data_to_server(self):
        while True:
            try:
                data = self.recording_stream.read(1024)
                self.s.sendall(data)
            except:
                pass


class xyz:
    def __init__(self,root):
        self.root = root
        self.root.title('LOGIN SCREEN')
        Label(text = ' Address ',font='Times 15').grid(row=1,column=1,pady=20)
        self.username = Entry()
        self.username.grid(row=1,column=2,columnspan=10)
        Label(text = ' Port ',font='Times 15').grid(row=2,column=1,pady=10)
        self.password = Entry()
        self.password.grid(row=2,column=2,columnspan=10)
        ttk.Button(text='Connect',command=self.login_user).grid(row=3,column=2)
        
    def login_user(self):
        global e1 
        e1 = self.username.get()
        global e2
        e2 = self.password.get()      
        #Destroy the current window
        root.destroy()
    
    # The main layout of the chat
    def layout(self,name):
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width = False,
                            height = False)
        self.Window.configure(width = 470,
                            height = 550,
                            bg = "#17202A")
        self.labelHead = Label(self.Window,
                            bg = "#17202A",
                            fg = "#EAECEE",
                            text = self.name ,
                            font = "Helvetica 13 bold",
                            pady = 5)
        
        self.labelHead.place(relwidth = 1)
        self.line = Label(self.Window,
                        width = 450,
                        bg = "#ABB2B9")
        
        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)
        
        self.textCons = Text(self.Window,
                            width = 20,
                            height = 2,
                            bg = "#17202A",
                            fg = "#EAECEE",
                            font = "Helvetica 14",
                            padx = 5,
                            pady = 5)
        
        self.textCons.place(relheight = 0.745,
                            relwidth = 1,
                            rely = 0.08)
        
        self.labelBottom = Label(self.Window,
                                bg = "#ABB2B9",
                                height = 80)
        
        self.labelBottom.place(relwidth = 1,
                            rely = 0.825)
        
        self.entryMsg = Entry(self.labelBottom,
                            bg = "#2C3E50",
                            fg = "#EAECEE",
                            font = "Helvetica 13")
        
        # place the given widget
        # into the gui window
        self.entryMsg.place(relwidth = 0.74,
                            relheight = 0.06,
                            rely = 0.008,
                            relx = 0.011)
        
        self.entryMsg.focus()
        
        # create a Send Button
        self.buttonMsg = Button(self.labelBottom,
                                text = "Send",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryMsg.get()))
        
        self.buttonMsg.place(relx = 0.77,
                            rely = 0.008,
                            relheight = 0.06,
                            relwidth = 0.22)
        
        self.textCons.config(cursor = "arrow")
        
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
        
        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight = 1,
                        relx = 0.974)
        
        scrollbar.config(command = self.textCons.yview)
        
        self.textCons.config(state = DISABLED)


if __name__ == '__main__':

    root = Tk()
    root.geometry('425x225')
    application = xyz(root)
    root.mainloop()

    
    # server = application.username
    # port = application.password
    
    c = Client()
    
