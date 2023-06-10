import tkinter as tk
from tkinter import messagebox
import threading
from buga_buga_class import BugaBuga
from time import sleep

def start_bot():
    bot = BugaBuga(684,384,1226,321)
    while True:
        print("Pacifista")
        bot.batalha()
        print("Matei")
        sleep(3) #deve ser trocar no futuro
        #bot.looting(bot.down_person[0],bot.down_person[1])
        print("Lotiei")

thread = threading.Thread(target=start_bot)


def iniciar():
    print("Iniciando o processo paralelo...")
    global thread
    thread.start()


def parar():
    print("Parando o processo paralelo...")
    global thread
    thread.join()

def sair():
    #if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
    root.destroy()

# Criação da janela principal
root = tk.Tk()

# Botão "Iniciar"
btn_iniciar = tk.Button(root, text="Iniciar", command=iniciar)
btn_iniciar.pack()

# Botão "Parar"
btn_parar = tk.Button(root, text="Parar", command=parar)
btn_parar.pack()

# Botão "Sair"
btn_sair = tk.Button(root, text="Sair", command=sair)
btn_sair.pack()

# Execução da interface gráfica
root.mainloop()