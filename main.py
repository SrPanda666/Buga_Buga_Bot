import tkinter as tk
from buga_buga_class import BugaBuga
from time import sleep

bot = BugaBuga(personagem_x=684,personagem_y=384,lista_x=1226,Lista_y=321)


sinal = True

def iniciar():
    print("Iniciando...")

    global sinalq
    sinal = True

    while sinal:
    
        bot.batalha()

        sleep(3)

        bot.looting(bot.down_person[0]+50,bot.down_person[1], 1190,517,'q')

def parar():
    print("Parando...")
    bot.aguarda()
    global sinal 
    sinal = False

def sair():
    root.destroy()

root = tk.Tk()

btn_iniciar = tk.Button(root, text="Iniciar", command=iniciar)
btn_iniciar.pack(pady=10)

btn_parar = tk.Button(root, text="Parar", command=parar)
btn_parar.pack(pady=10)

btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.pack(pady=10)

root.mainloop()
