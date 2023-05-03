from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from buga_buga import bot_start
    
class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Bot(Screen):

    def criar_bot(self):
        self.sinal = False
    def ligar_bot(self):
        self.sinal = True
        while self.sinal:
            bot_start(self.sinal)

    def desligar_bot(self):
        self.sinal = False



class Config(Screen):
    def fa(self):
        pass

    def fb(self):
        pass


class MyApp(App):
    def build(self):
        
        return Gerenciador()

if __name__ == '__main__':
    MyApp().run()
    