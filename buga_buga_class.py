import pyautogui as gui

class BugaBuga():

    def __init__(self,personagem_x=684,personagem_y=384,lista_x=1226,Lista_y=321) -> None:
        self.lista_batalha =  (lista_x,Lista_y)
        self.posicao_personagem = (personagem_x,personagem_y)
        
        self.right_person = (personagem_x + 50)
        self.left_person = (personagem_x - 50, personagem_y)
        self.up_person = (personagem_x, personagem_y - 50)
        self.down_person = (personagem_x, personagem_y + 50) #(679,431)


    def batalha(self):
        #pescamos o peixe, agora é descer a porrada nele
        gui.moveTo(x=self.lista_batalha[0],y=self.lista_batalha[1])
        gui.leftClick()

        #lançando todos os ataques de uma vez
        gui.press(['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10'])

    def looting(self,poke_x,poke_y,box_x,box_y,botao_boll='q'): #box_x = 1190, box_y = 517

        gui.moveTo(poke_x,poke_y)
        gui.rightClick()
        gui.moveTo(box_x, box_y)
        gui.leftClick()
        gui.leftClick()
        gui.leftClick()
        gui.leftClick()
        gui.leftClick()
        """ Caso queira capturar tbm"""
        gui.moveTo(poke_x, poke_y)
        gui.press(botao_boll)
        gui.leftClick
        
        #fechar a box
        #gui.moveTo(box_x,box_y)
        #gui.leftClick()

    def aguarda(self):
        pass
