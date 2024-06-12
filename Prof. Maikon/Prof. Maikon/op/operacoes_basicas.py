import tkinter as tk
from tkinter import messagebox

# Funções para operações básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        messagebox.showerror("Erro", "Divisão por zero!")
        return None
    else:
        return a / b

class OperacoesBasicasGUI:
    def __init__(self, parent):
        self.parent = parent
        self.operacoes_frame = tk.Frame(parent)
        self.operacoes_frame.pack(padx=20, pady=20)

        # Cria os campos de entrada
        self.entrada1_label = tk.Label(self.operacoes_frame, text="Entrada 1:")
        self.entrada1_label.grid(row=0, column=0)
        self.entrada1 = tk.Entry(self.operacoes_frame)
        self.entrada1.grid(row=0, column=1)

        self.entrada2_label = tk.Label(self.operacoes_frame, text="Entrada 2:")
        self.entrada2_label.grid(row=1, column=0)
        self.entrada2 = tk.Entry(self.operacoes_frame)
        self.entrada2.grid(row=1, column=1)

        # Cria os botões de operação
        self.soma_button = tk.Button(self.operacoes_frame, text="Soma", command=self.realizar_soma)
        self.soma_button.grid(row=2, column=0, pady=10)

        self.subtracao_button = tk.Button(self.operacoes_frame, text="Subtração", command=self.realizar_subtracao)
        self.subtracao_button.grid(row=2, column=1, pady=10)

        self.multiplicacao_button = tk.Button(self.operacoes_frame, text="Multiplicação", command=self.realizar_multiplicacao)
        self.multiplicacao_button.grid(row=3, column=0, pady=10)

        self.divisao_button = tk.Button(self.operacoes_frame, text="Divisão", command=self.realizar_divisao)
        self.divisao_button.grid(row=3, column=1, pady=10)

        # Cria a área de exibição do resultado
        self.resultado_label = tk.Label(self.operacoes_frame, text="")
        self.resultado_label.grid(row=4, column=0, columnspan=2)

    def realizar_soma(self):
        a = float(self.entrada1.get())
        b = float(self.entrada2.get())
        resultado = soma(a, b)
        self.exibir_resultado(f"Soma: {resultado}")

    def realizar_subtracao(self):
        a = float(self.entrada1.get())
        b = float(self.entrada2.get())
        resultado = subtracao(a, b)
        self.exibir_resultado(f"Subtração: {resultado}")

    def realizar_multiplicacao(self):
        a = float(self.entrada1.get())
        b = float(self.entrada2.get())
        resultado = multiplicacao(a, b)
        self.exibir_resultado(f"Multiplicação: {resultado}")

    def realizar_divisao(self):
        a = float(self.entrada1.get())
        b = float(self.entrada2.get())
        resultado = divisao(a, b)
        if resultado is not None:
            self.exibir_resultado(f"Divisão: {resultado}")

    def exibir_resultado(self, resultado):
        self.resultado_label.config(text=resultado)