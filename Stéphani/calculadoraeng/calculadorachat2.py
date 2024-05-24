import tkinter as tk
from tkinter import ttk, messagebox
import math

# Funções para operações básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero!")
        resultado = None
    return resultado

# Funções para potenciação e radiciação
def potenciacao(a, n):
    return a ** n

def raiz_quadrada(a):
    if a < 0:
        messagebox.showerror("Erro", "Raiz quadrada de número negativo!")
        return None
    else:
        return math.sqrt(a)

def raiz_n_esima(a, n):
    if a < 0 and n % 2 == 0:
        messagebox.showerror("Erro", "Raiz n-ésima complexa!")
        return None
    else:
        return a ** (1 / n)

# Funções para funções matemáticas
def seno(x):
    return math.sin(x)

def cosseno(x):
    return math.cos(x)

def tangente(x):
    if math.cos(x) == 0:
        messagebox.showerror("Erro", "Tangente indefinida!")
        return None
    else:
        return math.tan(x)

def logaritmo_natural(x):
    if x <= 0:
        messagebox.showerror("Erro", "Logaritmo natural de número não positivo!")
        return None
    else:
        return math.log(x)

def logaritmo_decimal(x):
    if x <= 0:
        messagebox.showerror("Erro", "Logaritmo decimal de número não positivo!")
        return None
    else:
        return math.log10(x)

# Funções de Engenharia Civil
def momento_fletor(forca, distancia):
    return forca * distancia

def calculo_laje(altura, largura, comprimento):
    # Exemplo de cálculo de volume de concreto necessário para uma laje
    volume = altura * largura * comprimento
    return volume

def calculo_estrutural():
    # Função para cálculo estrutural específico
    pass

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Criar uma aba para as operações básicas
        tab_control = ttk.Notebook(self)
        tab_basic = ttk.Frame(tab_control)
        tab_control.add(tab_basic, text='Operações Básicas')
        tab_control.pack(expand=1, fill='both')

        # Adicionar campos de entrada e botões para as operações básicas
        label_a = tk.Label(tab_basic, text="Valor de a:")
        label_a.grid(row=0, column=0)
        self.entry_a = tk.Entry(tab_basic)
        self.entry_a.grid(row=0, column=1)

        label_b = tk.Label(tab_basic, text="Valor de b:")
        label_b.grid(row=1, column=0)
        self.entry_b = tk.Entry(tab_basic)
        self.entry_b.grid(row=1, column=1)

        self.result_label = tk.Label(tab_basic, text="Resultado:")
        self.result_label.grid(row=2, column=1)

        button_sum = tk.Button(tab_basic, text="Soma", command=self.sum_operation)
        button_sum.grid(row=3, column=0)
        
        button_subtract = tk.Button(tab_basic, text="Subtração", command=self.subtract_operation)
        button_subtract.grid(row=3, column=1)

        button_multiply = tk.Button(tab_basic, text="Multiplicação", command=self.multiply_operation)
        button_multiply.grid(row=4, column=0)

        button_divide = tk.Button(tab_basic, text="Divisão", command=self.divide_operation)
        button_divide.grid(row=4, column=1)

        # Criar uma aba para funções matemáticas
        tab_math = ttk.Frame(tab_control)
        tab_control.add(tab_math, text='Funções Matemáticas')
        tab_control.pack(expand=1, fill='both')

        # Adicionar campos de entrada e botões para funções matemáticas
        label_x = tk.Label(tab_math, text="Valor de x:")
        label_x.grid(row=0, column=0)
        self.entry_x = tk.Entry(tab_math)
        self.entry_x.grid(row=0, column=1)

        self.math_result_label = tk.Label(tab_math, text="Resultado:")
        self.math_result_label.grid(row=1, column=1)

        button_sine = tk.Button(tab_math, text="Seno", command=self.sine_operation)
        button_sine.grid(row=2, column=0)
        
        button_cosine = tk.Button(tab_math, text="Cosseno", command=self.cosine_operation)
        button_cosine.grid(row=2, column=1)

        button_tangent = tk.Button(tab_math, text="Tangente", command=self.tangent_operation)
        button_tangent.grid(row=3, column=0)

        button_natural_log = tk.Button(tab_math, text="Logaritmo Natural", command=self.natural_log_operation)
        button_natural_log.grid(row=3, column=1)

        button_decimal_log = tk.Button(tab_math, text="Logaritmo Decimal", command=self.decimal_log_operation)
        button_decimal_log.grid(row=4, column=0)

        # Criar uma aba para operações de engenharia civil
        tab_civil_eng = ttk.Frame(tab_control)
        tab_control.add(tab_civil_eng, text='Engenharia Civil')
        tab_control.pack(expand=1, fill='both')

        # Adicionar campos de entrada e botões para operações de engenharia civil
        label_forca = tk.Label(tab_civil_eng, text="Força:")
        label_forca.grid(row=0, column=0)
        self.entry_forca = tk.Entry(tab_civil_eng)
        self.entry_forca.grid(row=0, column=1)

        label_distancia = tk.Label(tab_civil_eng, text="Distância:")
        label_distancia.grid(row=1, column=0)
        self.entry_distancia = tk.Entry(tab_civil_eng)
        self.entry_distancia.grid(row=1, column=1)

        button_momento_fletor = tk.Button(tab_civil_eng, text="Momento Fletor", command=self.momento_fletor_operation)
        button_momento_fletor.grid(row=2, column=0)

        label_altura = tk.Label(tab_civil_eng, text="Altura:")
        label_altura.grid(row=3, column=0)
        self.entry_altura = tk.Entry(tab_civil_eng)
        self.entry_altura.grid(row=3, column=1)

        label_largura = tk.Label(tab_civil_eng, text="Largura:")
        label_largura.grid(row=4, column=0)
        self.entry_largura = tk.Entry(tab_civil_eng)
        self.entry_largura.grid(row=4, column=1)

        label_comprimento = tk.Label(tab_civil_eng, text="Comprimento:")
        label_comprimento.grid(row=5, column=0)
        self.entry_comprimento = tk.Entry(tab_civil_eng)
        self.entry_comprimento.grid(row=5, column=1)

        button_calculo_laje = tk.Button(tab_civil_eng, text="Cálculo de Laje", command=self.calculo_laje_operation)
        button_calculo_laje.grid(row=6, column=0)

    def sum_operation(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            result = soma(a, b)
            self.result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def subtract_operation(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            result = subtracao(a, b)
            self.result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def multiply_operation(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            result = multiplicacao(a, b)
            self.result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def divide_operation(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            result = divisao(a, b)
            if result is not None:
                self.result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def sine_operation(self):
        try:
            x = float(self.entry_x.get())
            result = seno(x)
            self.math_result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def cosine_operation(self):
        try:
            x = float(self.entry_x.get())
            result = cosseno(x)
            self.math_result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def tangent_operation(self):
        try:
            x = float(self.entry_x.get())
            result = tangente(x)
            if result is not None:
                self.math_result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def natural_log_operation(self):
        try:
            x = float(self.entry_x.get())
            result = logaritmo_natural(x)
            if result is not None:
                self.math_result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def decimal_log_operation(self):
        try:
            x = float(self.entry_x.get())
            result = logaritmo_decimal(x)
            if result is not None:
                self.math_result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def momento_fletor_operation(self):
        try:
            forca = float(self.entry_forca.get())
            distancia = float(self.entry_distancia.get())
            result = momento_fletor(forca, distancia)
            self.result_label.config(text=f"Momento Fletor: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

    def calculo_laje_operation(self):
        try:
            altura = float(self.entry_altura.get())
            largura = float(self.entry_largura.get())
            comprimento = float(self.entry_comprimento.get())
            result = calculo_laje(altura, largura, comprimento)
            self.result_label.config(text=f"Volume de Concreto: {result}")
        except ValueError:
            messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
