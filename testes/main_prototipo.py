import threading
import tkinter as tk
from tkinter import messagebox
from time import sleep

"""
Sina = Condição de controle para iniciar e parar o bot
thread: thread que executa o bot em paralelo com a interface gráfica
root: Raiz de controle da interface gráfica
"""
sinal = True
thread = None
root = None

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
        thread = threading.Thread(target=batalha)
        thread.start()
    else:
        messagebox.showinfo("Aviso", 'Bot ja está sendo executado')

def batalha():
    while sinal: 
            print("Batalha")
            sleep(1)

def parar():
    global sinal
    sinal = False
    messagebox.showinfo("Aviso", 'Bot teve sua execuração parada')

def sair():
    if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
        root.destroy()

def interface():
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

thread_interface = threading.Thread(target=interface)
thread_interface.start()
