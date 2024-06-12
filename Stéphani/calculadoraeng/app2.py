import tkinter as tk
from tkinter import Tk
import os

# Interface gráfica principal
app = Tk()
app.title("Calculadora Avançada")

# Criando abas para diferentes funcionalidades
aba_operacoes = tk.Frame(app)
aba_operacoes.pack(side="top", fill="both", expand=True)

# Funções para abrir os arquivos correspondentes
def abrir_arquivo_1():
    os.system("start 1operacoes_basica.py")

def abrir_arquivo_2():
    os.system("start 2potenciacao_radificiacao.py")

def abrir_arquivo_3():
    os.system("start 3funcao_matematica.py")

def abrir_arquivo_4():
    os.system("start 4operacoes_memoria.py")

def abrir_arquivo_5():
    os.system("start 5integracao_numerica.py")

def abrir_arquivo_6():
    os.system("start 6operacoes_fourier.py")

def abrir_arquivo_7():
    os.system("start 7operacoes_estrututais.py")

# Você precisa definir as funções para os outros arquivos de maneira semelhante

# Criando botões para cada arquivo de operações
botao_1 = tk.Button(aba_operacoes, text="1operacoes_basica.py", command=abrir_arquivo_1)
botao_1.pack()

botao_2 = tk.Button(aba_operacoes, text="2potenciacao_radificiacao.py", command=abrir_arquivo_2)
botao_2.pack()

botao_3 = tk.Button(aba_operacoes, text="3funcao_matematica.py", command=abrir_arquivo_3)
botao_3.pack()

botao_4 = tk.Button(aba_operacoes, text="4operacoes_memoria.py", command=abrir_arquivo_4)
botao_4.pack()

botao_5 = tk.Button(aba_operacoes, text="5integracao_numerica.py", command=abrir_arquivo_5)
botao_5.pack()

botao_6 = tk.Button(aba_operacoes, text="6operacoes_fourier.py", command=abrir_arquivo_6)
botao_6.pack()

botao_7 = tk.Button(aba_operacoes, text="7operacoes_estruturais.py", command=abrir_arquivo_7)
botao_7.pack()

# Você precisa criar botões para os outros arquivos de maneira semelhante

# Iniciando a interface gráfica
app.mainloop()