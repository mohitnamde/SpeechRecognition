# Hello world.

import kivy
import pyttsx3
import speech_recognition as sr

kivy.require('1.0.6')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()