from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import requests
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from create_subject import CreateSubject
from news import NewsPage
from quiz import QuizPage
from stats import StatsPage
from kivy.uix.floatlayout import FloatLayout
from db import create_db
import sqlite3

import openai
import os
from api import API_KEY

import numpy
import sklearn
openai.api_key=API_KEY



create_db()
conn = sqlite3.connect('mobile_app_data.db')

class MainScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        root = FloatLayout()
        scroll = ScrollView(size_hint=(1,1),do_scroll_x=False,do_scroll_y=True)
        layout = BoxLayout(orientation = "vertical",size_hint_y = None,size_hint_x = None, spacing = 10, padding = 30, )
        layout.bind(minimum_height=layout.setter("height"))


        createS = Button(text = "Create subject", size_hint=(None,None), size = (500,100),pos_hint={"center_x":10})
        createS.bind(on_press=self.go_to_creation)
        news = Button(text="news",size_hint=(None,None),size=(500,100),pos_hint={"center_x":10})
        news.bind(on_press=self.see_news)
        quizz = Button(text="quiz",size_hint=(None,None),size=(500,100),pos_hint={"center_x":10})
        quizz.bind(on_press=self.see_quiz)
        stats = Button(text="stats",size_hint=(None,None),size=(500,100),pos_hint={"center_x":10})
        stats.bind(on_press=self.see_stats)



        layout.add_widget(createS)
        layout.add_widget(news)
        layout.add_widget(stats)
        layout.add_widget(quizz)
        
        scroll.add_widget(layout)
        root.add_widget(scroll)
        self.add_widget(root)
    
    
    
    def go_to_creation(self,instance):
        self.manager.current = "create_subject"
    def see_stats(self,instance):
        self.manager.current = "stats"
    def see_news(self,instance):
        self.manager.current = "news"
    def see_quiz(self,instance):
        self.manager.current = "quiz"
    
    # def onll(self,instance):
    #     if check_internet():
    #         self.manager.current = "online"
    #     else:
    #         popup = Popup(title="you don't have internet",content = Label(text="this is popup"),size_hint=(None,None),size={1,2})
    #         popup.open()

        
def check_internet():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False
    


class MyApp(App):

    def build(self):

        sm = ScreenManager()
        sm.add_widget(MainScreen(name="MainScreen"))


        sm.add_widget(NewsPage(name="news"))
        sm.add_widget(CreateSubject(name="create_subject"))
        sm.add_widget(QuizPage(name="quiz"))
        sm.add_widget(StatsPage(name="stats"))
        
        sm.current = "MainScreen"
        return sm

if __name__ == "__main__":
    MyApp().run()

