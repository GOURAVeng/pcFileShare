#GUI RELATED PACKAGES AND MODULES
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
#from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.label import Label
#from kivy.uix.button import Button
from kivy.lang import Builder 
import threading as th

#FOR ftp related libraries
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

#for getting ip address
import socket
import os

#First Page
class WelcomePage(Screen):pass

#Second Page
class LoginPage(Screen):
    # username=ObjectProperty(None)
    # password=ObjectProperty(None)
    def Login(self):
        try:
            # username=self.username.text
            # password=self.password.text

            # if self.ids.username.text == "" and self.ids.password.text == "":
            #     popup = Popup(title='Wrong',
            #     content='Input field cannot be empty')
            #     popup.open()
            # else:
            username=self.user.text
            password=self.pswd.text
            print(username,password)
            authorizer=DummyAuthorizer()
            authorizer.add_user(username,password,LoginPage.p)
            print(LoginPage.p)
            handler=FTPHandler
            handler.authorizer=authorizer

        # getting ip address 
            hostname = socket.gethostname()
            #ip=socket.gethostbyname(hostname)

            LoginPage.server=FTPServer(("192.168.43.15",1238),handler)
            LoginPage.server.serve_forever()  
        except Exception as e:
            print("something went wrong",e)
        else:
            print("Successful!")
    def Temp(self):
        t1 = th.Thread(name="d",target=self.Login) 
        print("path"+self.demo.path) 
        ls=[self.demo.path,self.demo1.path]
        print(ls)
        if ls==['/','/']:
            LoginPage.p=os.getcwd()
            print("inside if")
            print(ls)
        else:
            while '/' in ls:
                ls.remove('/')
                print(ls)
            LoginPage.p=str(ls[0])
        print("outside")
        print(ls) 
        t1.start()
    
    # def temp2(self):
    #     t2=Thread(target=self.stop)
    #     t2.start()

    # def stop(self):
    #     Login.server.close()

# Third Page
class Engine(Screen):
    def ip(self):
        hostname = socket.gethostname()
        #ip=socket.gethostbyname(hostname)
        self.result.text = "192.168.43.15:1238"

    def kill(self):
        # threads = th.enumerate()
        # temp = None
        # for x in threads:
        #     if x.name == 'd':
        #         temp = x
        # temp.__stop_event.set()
        LoginPage.server.close()        
    # def Server(self):
    # def stop(self):
    #     server.close()
        # authorizer=DummyAuthorizer()
        # authorizer.add_user(LoginPage.username,LoginPage.password,os.getcwd())
        # handler=FTPHandler
        # handler.authorizer=authorizer

        # # getting ip address

        # hostname = socket.gethostname()
        # ip=socket.gethostbyname(hostname)

        # server=FTPServer((ip,1238),handler)
        # server.serve_forever()
    


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv


if __name__=="__main__":
    MyMainApp().run()

