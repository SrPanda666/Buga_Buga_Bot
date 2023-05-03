from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from buga_buga import bot_start
import threading
    
class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Bot(Screen):

    def criar_bot(self):
        self.sinal = False

    def ligar_bot(self):
        try:
            print('liguei')
            self.sinal = True
            print('thread feita')
            self.bot_thread = threading.Thread(target=self.bot_loop)
            print('thread iniciada')
            self.bot_thread.start()
        
        except:
            print('thread falhou')

    def bot_loop(self):
        while self.sinal:
            bot_start()

    def desligar_bot(self):
        print('tentei desligar')
        self.sinal = False
        self.bot_thread.join()
        print('desliguei')


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
    """
    Fazer sistema de sobreposição
    """
