import math
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox
import math

# Funções para operações básicas
def somar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def subtrair():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 - num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 * num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Erro", "Divisão por zero não é permitida!")
            return
        resultado = num1 / num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções para operações de potenciação e radiciação
def potencia():
    try:
        base = float(entry_base.get())
        expoente = float(entry_expoente.get())
        resultado = base ** expoente
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def radiciacao():
    try:
        valor = float(entry_valor.get())
        if valor < 0:
            messagebox.showerror("Erro", "Não é possível calcular a raiz quadrada de um número negativo!")
            return
        resultado = valor ** 0.5
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Funções matemáticas adicionais
def calcular_cosseno():
    try:
        angulo = float(entry_angulo.get())
        resultado = math.cos(math.radians(angulo))
        label_resultado.config(text=f"Cosseno: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_seno():
    try:
        angulo = float(entry_angulo.get())
        resultado = math.sin(math.radians(angulo))
        label_resultado.config(text=f"Seno: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_tangente():
    try:
        angulo = float(entry_angulo.get())
        resultado = math.tan(math.radians(angulo))
        label_resultado.config(text=f"Tangente: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_logaritmo_natural():
    try:
        numero = float(entry_numero.get())
        if numero <= 0:
            messagebox.showerror("Erro", "O logaritmo natural só pode ser calculado para números positivos!")
            return
        resultado = math.log(numero)
        label_resultado.config(text=f"Logaritmo Natural: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def calcular_logaritmo_decimal():
    try:
        numero = float(entry_numero.get())
        if numero <= 0:
            messagebox.showerror("Erro", "O logaritmo decimal só pode ser calculado para números positivos!")
            return
        resultado = math.log10(numero)
        label_resultado.config(text=f"Logaritmo Decimal: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

# Função para exibir a interface de operações básicas
def mostrar_operacoes_basicas():
    esconder_todos_widgets()
    label_num1.pack()
    entry_num1.pack()
    label_num2.pack()
    entry_num2.pack()
    btn_somar.pack()
    btn_subtrair.pack()
    btn_multiplicar.pack()
    btn_dividir.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de radiciação e potenciação
def mostrar_radiciacao_potenciacao():
    esconder_todos_widgets()
    label_base.pack()
    entry_base.pack()
    label_expoente.pack()
    entry_expoente.pack()
    btn_potencia.pack()
    label_valor.pack()
    entry_valor.pack()
    btn_radiciacao.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para exibir a interface de funções matemáticas
def mostrar_funcoes_matematicas():
    esconder_todos_widgets()
    label_angulo.pack()
    entry_angulo.pack()
    btn_calcular_cosseno.pack()
    btn_calcular_seno.pack()
    btn_calcular_tangente.pack()
    label_numero.pack()
    entry_numero.pack()
    btn_calcular_log_natural.pack()
    btn_calcular_log_decimal.pack()
    label_resultado.pack()
    btn_voltar.pack()

# Função para voltar à interface inicial
def voltar():
    esconder_todos_widgets()
    btn_op_basicas.pack()
    btn_rad_pot.pack()
    btn_funcoes_matematicas.pack()

# Função para esconder todos os widgets
def esconder_todos_widgets():
    for widget in root.pack_slaves():
        widget.pack_forget()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x300")  # Definindo a largura e altura da janela
root.minsize(300, 300)    # Definindo o tamanho mínimo da janela

# Botões iniciais
btn_op_basicas = tk.Button(root, text="Operações Básicas", command=mostrar_operacoes_basicas)
btn_rad_pot = tk.Button(root, text="Radiciação e Potenciação", command=mostrar_radiciacao_potenciacao)
btn_funcoes_matematicas = tk.Button(root, text="Funções Matemáticas", command=mostrar_funcoes_matematicas)
btn_op_basicas.pack()
btn_rad_pot.pack()
btn_funcoes_matematicas.pack()

# Labels e entradas para operações básicas
label_num1 = tk.Label(root, text="Número 1:")
entry_num1 = tk.Entry(root)
label_num2 = tk.Label(root, text="Número 2:")
entry_num2 = tk.Entry(root)

# Botões de operações básicas
btn_somar = tk.Button(root, text="Somar", command=somar)
btn_subtrair = tk.Button(root, text="Subtrair", command=subtrair)
btn_multiplicar = tk.Button(root, text="Multiplicar", command=multiplicar)
btn_dividir = tk.Button(root, text="Dividir", command=dividir)

# Labels e entradas para potenciação
label_base = tk.Label(root, text="Base:")
entry_base = tk.Entry(root)
label_expoente = tk.Label(root, text="Expoente:")
entry_expoente = tk.Entry(root)

# Botão de potenciação
btn_potencia = tk.Button(root, text="Potência", command=potencia)

# Labels e entradas para radiciação
label_valor = tk.Label(root, text="Valor para raiz quadrada:")
entry_valor = tk.Entry(root)

# Labels e entradas para funções matemáticas
label_angulo = tk.Label(root, text="Ângulo (em graus):")
entry_angulo = tk.Entry(root)
label_numero = tk.Label(root, text="Número:")
entry_numero = tk.Entry(root)

# Botões de funções matemáticas
btn_calcular_cosseno = tk.Button(root, text="Cosseno", command=calcular_cosseno)
btn_calcular_seno = tk.Button(root, text="Seno", command=calcular_seno)
btn_calcular_tangente = tk.Button(root, text="Tangente", command=calcular_tangente)
btn_calcular_log_natural = tk.Button(root, text="Log Natural", command=calcular_logaritmo_natural)
btn_calcular_log_decimal = tk.Button(root, text="Log Decimal", command=calcular_logaritmo_decimal)

# Botão de voltar
btn_voltar = tk.Button(root, text="Voltar", command=voltar)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="Resultado:")

# Iniciar a interface gráfica
root.mainloop()

