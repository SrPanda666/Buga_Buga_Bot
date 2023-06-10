import tkinter as tk
from tkinter import messagebox
import threading

def iniciar():
    print("Iniciando o processo paralelo...")

def parar():
    print("Parando o processo paralelo...")

def sair():
    if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
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