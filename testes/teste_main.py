import tkinter as tk
from tkinter import messagebox
from time import sleep

sinal = True
root = None

def iniciar():
    global sinal
    sinal = True
    while sinal:
        print("Batalha")
        sleep(1)
        
def parar():
    global sinal
    sinal = False
    messagebox.showinfo("Aviso", "Bot teve sua execução parada")

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

    # Aumentando o tamanho da interface gráfica
    root.geometry(f"{200}x100")

    # Execução da interface gráfica
    root.mainloop()

interface()
