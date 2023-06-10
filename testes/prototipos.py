import threading
import tkinter as tk
from time import sleep

sinal = True
thread = None
root = None

def iniciar():
    global sinal, thread
    if not thread or not thread.is_alive():
        sinal = True
        thread = threading.Thread(target=batalha)
        thread.start()

def batalha():
    while sinal: 
            print("Batalha")
            sleep(1)

def parar():
    global sinal
    sinal = False

def interface():
    global root
    root = tk.Tk()

    # Botão "Iniciar"
    btn_iniciar = tk.Button(root, text="Iniciar", command=iniciar)
    btn_iniciar.pack(fill='x', expand=True)

    # Botão "Parar"
    btn_parar = tk.Button(root, text="Parar", command=parar)
    btn_parar.pack(fill='x', expand=True)

    #aumentando o tamanho da interface grafica
    root.geometry(f"{200}x{100}")

    # Execução da interface gráfica
    root.mainloop()

thread_interface = threading.Thread(target=interface)
thread_interface.start()
