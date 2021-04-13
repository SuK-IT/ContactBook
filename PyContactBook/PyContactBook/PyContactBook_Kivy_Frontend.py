import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Color, Rectangle
import PyContactBook


class MyGrid(Widget):
    m_Firstname = ObjectProperty(None)
    m_Surname = ObjectProperty(None)
    m_Mail = ObjectProperty(None)
    m_Telephone = ObjectProperty(None)
    m_Street = ObjectProperty(None)
    m_Required = ObjectProperty(None)
    m_First_Req = ObjectProperty(None)
    m_Sur_Req = ObjectProperty(None)
    m_Tel_Req = ObjectProperty(None)

    
    def btn(self):
        if self.m_Firstname.text == "" or self.m_Surname.text == "" or self.m_Telephone.text == "":
            
            red = (60,0,0,1)
            self.m_Required.color = red
            self.m_First_Req.color = red
            self.m_Sur_Req.color = red
            self.m_Tel_Req.color = red
           

        else:
            PyContactBook.CreateContact({ 
        
                'firstname': self.m_Firstname.text,
                'surname': self.m_Surname.text,
                'address': self.m_Street.text,
                'tel': self.m_Telephone.text,
                'mail': self.m_Mail.text
                })
            #print("Vorname: ", self.m_Firstname.text, "Name: ", self.m_Surname.text, "Telefon: ", self.m_Telephone.text, "E-Mail: ", self.m_Mail.text, "Straße: ", self.m_Street.text)
            #Aufräumen, Clear + Auf weiß wechseln
            white = (1,1,1,1)
            black = (0,0,0,0)
            self.m_Required.color = black
            self.m_First_Req.color = white
            self.m_Sur_Req.color = white
            self.m_Tel_Req.color = white
            self.m_Firstname.text = ""
            self.m_Surname.text = ""
            self.m_Telephone.text = ""
            self.m_Mail.text = ""
            self.m_Street.text = ""



 


class MyApp(App):
    def build(self):
        self.title ="Kontakt-Manager"
        return MyGrid()
        
    

if __name__ == "__main__":
    MyApp().run()