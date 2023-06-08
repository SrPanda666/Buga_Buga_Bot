import tkinter as tk
from buga_buga_class import BugaBuga
from time import sleep

class EstadoInicial:
    def __init__(self):
        print("Entrando no estado inicial.")

    def proximo_estado(self):
        print("Transicionando para o próximo estado.")
        return EstadoExecucao()


class EstadoExecucao:
    def __init__(self):
        print("Entrando no estado de execução.")

    def proximo_estado(self):
        print("Transicionando para o próximo estado.")
        return EstadoFinal()


class EstadoFinal:
    def __init__(self):
        print("Entrando no estado final.")

    def proximo_estado(self):
        print("Não há próximo estado. A máquina chegou ao estado final.")


class App:
    def __init__(self):
        self.bot = BugaBuga(684, 384, 1226, 321)
        self.estado_atual = EstadoInicial()

    def iniciar(self):
        print("Iniciando...")
        self.sinal = True
        self.executar_maquina()

    def parar(self):
        print("Parando...")
        self.sinal = False
        self.bot.aguarda()

    def sair(self):
        root.destroy()

    def executar_maquina(self):
        while not (isinstance(self.estado_atual, EstadoFinal)):
            self.bot.batalha()
            sleep(3)
            self.bot.looting(self.bot.down_person[0] + 50, self.bot.down_person[1], 1190, 517, 'q')
            self.estado_atual = self.estado_atual.proximo_estado()

            if isinstance(self.estado_atual, EstadoFinal):
                self.parar()
                break

root = tk.Tk()
app = App()

btn_iniciar = tk.Button(root, text="Iniciar", command=app.iniciar)
btn_iniciar.pack(pady=10)

btn_parar = tk.Button(root, text="Parar", command=app.parar)
btn_parar.pack(pady=10)

btn_sair = tk.Button(root, text="Sair", command=app.sair)
btn_sair.pack(pady=10)

root.mainloop()
