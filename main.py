import threading
import tkinter as tk
from tkinter import messagebox
from time import sleep
from buga_buga_class import BugaBuga

"""
Sina = Condição de controle para iniciar e parar o bot
thread: thread que executa o bot em paralelo com a interface gráfica
root: Raiz de controle da interface gráfica
bot: Instancia do buga buga bot que foi criada e preparada para ser executada
como_lootear: recebe se a região de loot sera apenas um lado ou tres opções
Na pratica:
    sendo:
            1 - Esquerda do personagem
            2 - cima do personagem
            3 - Direita do personagem
            4 - Em baixo do perconagem
            5 - 3 blocos em baixo do personagem
"""
sinal = False 
thread = None
root = None
bot = BugaBuga(684,384,1226,321)
como_lootear = 5

"""
Abaixo deste comentario estão as funções desenvolvidas para fazer o sistema funcionar
Aviso: muito coidado para NÃO MEXER nelas
"""

def iniciar():
    """
    Funcão acionada pelo botão iniciar da interface gráfica, responsavel para executar a thread de inicio do bot
    Esta função acessa as variaveis globais sinal e thread:
        se sinal for True e não existir uma thread viva no momento:
            então cria uma thread que executa o bot
        se nao, avisa ao usuário que o bot já foi iniciado
    """
    global sinal, thread
    if not thread or not thread.is_alive():
        sinal = True
        thread = threading.Thread(target=ligar_bot)
        thread.start()
    else:
        messagebox.showinfo("Aviso", 'Bot ja está sendo executado')

def ligar_bot():
    """
    Cria um laço de repetição "Inifinito" até que o sinal seja "FALSE"
    a cada 3 segundos o bot inicia o processo de batalha
    apos a batalha o bot aguarda 3 segundos
    apos a aguardar, o bot inicia o processo de looting
    e o ciclo é reiniciado
    """
    while sinal: 
            sleep(3)
            bot.batalha()
            sleep(3)
            bot.como_lootear(1)

def parar():
    """
    Altera o valor da variavel global 'sinal' para para 'False' visando parar o bot, além de mostrar uma mensagem para o usuário
    """
    global sinal
    sinal = False
    messagebox.showinfo("Aviso", 'Bot teve sua execuração parada')

def sair():
    """
    Pergunta para o usuário realmente quer sair
        caso sim: Fecha o app
        caso não: Nada acontece
    """
    if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
        root.destroy()

def interface():
    """
    função que cria uma interface gráfica usando tkinter e atrela a mesma a variavel global root
    """
    global root
    root = tk.Tk()

    # Botão "Iniciar"
    btn_iniciar = tk.Button(root, text="Iniciar", command=iniciar)
    btn_iniciar.pack(fill='x', expand=True)

    # Botão "Parar"
    btn_parar = tk.Button(root, text="Parar", command=parar)
    btn_parar.pack(fill='x', expand=True)

    # Botão "Sair"
    btn_sair = tk.Button(root, text="Sair", command=sair)
    btn_sair.pack(fill='x', expand=True)
    #aumentando o tamanho da interface grafica
    root.geometry(f"{200}x{100}")

    # Execução da interface gráfica
    root.mainloop()


################################## Condigo em execução a baixo, resto é função e controle#######
"""
Thread responsavel pela interface gráfica
"""
thread_interface = threading.Thread(target=interface)
thread_interface.start()
