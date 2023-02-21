from kivy.app import App
from kivy.core.window import Window

from login_page import Login_page
from home_page import Home_page

from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (1200, 700)

class Main(App):
    def build(self):
        sm = ScreenManager()
        #sm.add_widget(Login_page(name="login"))
        sm.add_widget(Home_page(name="home"))

        return sm
Main().run()
