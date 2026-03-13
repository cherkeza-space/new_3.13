from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class NewsPage(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        get_home = Button(text = 'home')
        get_home.bind(on_press=self.Get_home_page)
        scroll = ScrollView(size_hint=(1,1),do_scroll_x=False,do_scroll_y=True)
        
        main_layout = BoxLayout(orientation = "vertical",size_hint_y=None)
        main_layout.bind(minimum_height=main_layout.setter("height"))
        txt = Label(text="news!")


        main_layout.add_widget(get_home)
        main_layout.add_widget(txt)
        main_layout.add_widget(Widget())
      

        scroll.add_widget(main_layout)

        self.add_widget(scroll)
    def Get_home_page(self,instance):
        self.manager.current = "MainScreen"
