#GUI RELATED PKAGES AND MODULES
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder 
import threading as th
from threading import Thread
#FOR ftp related libraries
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

import os
#for getting ip address
import socket

#First Page
class WelcomePage(Screen):
    pass

#Second Page
class LoginPage(Screen):
    def Login(self):
        try:
        #getting username and password
            username=self.user.text
            password=self.pswd.text
            
        #This will decide which user to allow access
            authorizer=DummyAuthorizer()
            authorizer.add_user(username,password,LoginPage.p)
        #update authorization settings in the FTP handler  
            handler=FTPHandler
            handler.authorizer=authorizer

        # getting ip address 
            hostname = socket.gethostname()
            ip=socket.gethostbyname(hostname)

        #creating server
            LoginPage.server=FTPServer((ip,1238),handler)
            LoginPage.server.serve_forever()  
        except Exception as e:
            print("something went wrong",e)
        else:
            print("Successful!")

    def Temp(self):
        #creating a thread to target login function
        t1 = th.Thread(name="d",target=self.Login) 

        #if user does not select any path from file chooser
        if self.demo.path=='/' and self.demo1.path=='/':
            os.chdir("..")
            LoginPage.p=os.getcwd()
        #if user chooses any file from any of the view list or icon
        else:
            ls=[self.demo.path,self.demo1.path]
            while '/' in ls:
                ls.remove('/')
            LoginPage.p=str(ls[0])
        #to start the thread that we created
        t1.start()

# Third Page
class Engine(Screen):
    #to get the ip address of the network and disply it on last screen
    def ip(self):
        hostname = socket.gethostname()
        ip=socket.gethostbyname(hostname)
        self.result.text = f"ftp://{str(ip)}:1238"

    def kill(self):
        #to close the server 
        LoginPage.server.close()        

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__=="__main__":
    MyMainApp().run()

