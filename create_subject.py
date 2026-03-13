from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import sqlite3



class CreateSubject(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        get_home = Button(text = 'H',size_hint=(None,None),size=(45,45),pos_hint={"center_x":0.04})
        get_home.bind(on_press=self.Get_home_page)
        
        
        scroll = ScrollView(size_hint=(1,1),do_scroll_x=False,do_scroll_y=True)
        main_layout = BoxLayout(orientation = "vertical",size_hint_y=None)
        main_layout.bind(minimum_height=main_layout.setter("height"))
        
        layout = BoxLayout(orientation="horizontal",size_hint_y = None, spacing = 10, padding = 10)
        layout2 = BoxLayout(orientation = "horizontal",size_hint_y=None,spacing=10,padding=10)

        btn = Button(text="click here",size_hint=(None,None),size=(30,30))
        btnx = Button(text="second click",size_hint=(None,None),size=(30,30))
        btn2 = Button(text="don't click me!",size_hint=(None,None),size=(30,30))
        btn2x = Button(text="second don't click me!",size_hint=(None,None),size=(30,30))


        layout.add_widget(btn)
        layout.add_widget(btnx)
        layout2.add_widget(btn2)
        layout2.add_widget(btn2x)
        
        main_layout.add_widget(get_home)
        main_layout.add_widget(Widget())
        main_layout.add_widget(layout)
        main_layout.add_widget(Widget())
        main_layout.add_widget(layout2)

        scroll.add_widget(main_layout)

        self.add_widget(scroll)
    def Get_home_page(self,instance):
        self.manager.current = "MainScreen"
