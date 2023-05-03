import pyautogui as gui
#from pos_img import localiza_img_tela
from time import sleep

def lotear_capturar(x,y):
    gui.moveTo(x,y)
    sleep(0.25)
    gui.rightClick()
    gui.moveTo(x=1189, y=514)
    gui.leftClick()
    gui.leftClick()
    gui.leftClick()
    gui.leftClick()
    sleep(0.25)
    #gui.moveTo(x=1349, y=490)
    gui.press('q')
    gui.moveTo(x,y)
    gui.leftClick()


def pescar(agua=(0,0),vara=(0,0),lista_batalha=(0,0),regiao_peixe=(0,0,0,0)):
    #clicando na vara de pesca
    gui.moveTo(x=vara[0],y=vara[1])
    gui.leftClick

    #jogando a isca na agua
    gui.moveTo(x=agua[0],y=agua[1])
    gui.leftClick

    #quando o peixe fica verde, coloca o mouse no meio do peixe e clica
    peixe_x,peixe_y = peixe_verde(regiao_peixe)
    gui.moveTo(x=peixe_x,y=peixe_y)
    gui.leftClick()

    #pescamos o peixe, agora é descer a porrada nele
    gui.moveTo(x=lista_batalha[0],y=lista_batalha[1])
    gui.leftClick()

    #lançando todos os ataques de uma vez
    gui.press(['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10'])



def peixe_verde(regiao_peixe=(0,0,0,0)):
   box = gui.locateOnScreen('img/1.PNG',limit=12,region=regiao_peixe)
   x = box[0]
   y = box[1]
   largura = box[2]
   altura = box[3]

   pos_x = x + (largura/2)
   pos_y = y + (altura/2)

   return pos_x,pos_y

    