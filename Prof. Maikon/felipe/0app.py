import matc
from re import A
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Interface gráfica (utilizando tkinter como exemplo)def interface():
    # Criar a janela principal
janela = Tk()
janela.title("Calculadora Científica Avançada - Engenharia Civil e Básica")

    # Abas para separação das funcionalidades
abas = ttk.Notebook(janela)
aba_basica = ttk.Frame(abas)
aba_avancada = ttk.Frame(abas)
aba_engenharia_civil = ttk.Frame(abas)
abas.add(aba_basica, text="Básica")
abas.add(aba_avancada, text="Avançada")
abas.add(aba_engenharia_civil, text="Eng. Civil")
abas.pack(expand=True, fill="both")

    # Funcionalidades básicas (utilizar widgets do tkinter)
    # ... (implementar campos de entrada, botões, labels para as operações básicas)

    # Funcionalidades avançadas (integração, derivada, transformada de Fourier)
def integracao_numerica():
        funcao_str = entrada_funcao.get()
        a = float(entrada_limite_a.get())
        b = float(entrada_limite_b.get())
        n = int(entrada_pontos.get())
        resultado = integral_numerica(funcao_str, a, b, n)
        if resultado is not None:
            label_resultado_integracao.config(text=f"Resultado: {resultado:.4f}")

label_funcao_integracao = Label(aba_avancada, text="Função:")
label_funcao_integracao.pack()
entrada_funcao = Entry(aba_avancada)
entrada_funcao.pack()

label_limite_a = Label(aba_avancada, text="Limite inferior (a):")
label_limite_a.pack()
entrada_limite_a = Entry(aba_avancada)
entrada_limite_a.pack()

label_limite_b = Label(aba_avancada, text="Limite superior (b):")
label_limite_b.pack()
entrada_limite_b = Entry(aba_avancada)
entrada_limite_b.pack()

label_pontos = Label(aba_avancada, text="Número de pontos (n):")
label_pontos.pack()
entrada_pontos = Entry(aba_avancada)
entrada_pontos.pack()

botao_integrar = Button(aba_avancada, text="Integrar", command=integracao_numerica)
botao_integrar.pack()

label_resultado_integracao = Label(aba_avancada, text="Resultado:")
label_resultado_integracao.pack()

def derivada_numerica():
        funcao_str = entrada_funcao_derivada.get()
        x = float(entrada_valor_x.get())
        h = float(entrada_passo.get())
        resultado = derivada_numerica(funcao_str, x, h)
        if resultado is not None:
            label_resultado_derivada.config(text=f"Derivada: {resultado:.4f}")

label_funcao_derivada = Label(aba_avancada, text="Função:")
label_funcao_derivada.pack()
entrada_funcao_derivada = Entry(aba_avancada)
entrada_funcao_derivada.pack()

label_valor_x = Label(aba_avancada, text="Valor de x:")
label_valor_x.pack()
entrada_valor_x = Entry(aba_avancada)
entrada_valor_x.pack()

label_passo = Label(aba_avancada, text="Passo (h):")
label_passo.pack()
entrada_passo = Entry(aba_avancada)
entrada_passo.pack()

botao_derivar = Button(aba_avancada, text="Derivar", command=derivada_numerica)
botao_derivar.pack()

label_resultado_derivada = Label(aba_avancada, text="Resultado:")
label_resultado_derivada.pack()

def transformada_fourier_plot():
        sinal_str = entrada_sinal.get()
        try:
            sinal = eval(sinal_str)
            fourier = transformada_fourier(sinal)
            plt.plot(np.abs(fourier))
            plt.title("Transformada de Fourier")
            plt.xlabel("Frequência")
            plt.ylabel("Magnitude")
            plt.show()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar o sinal: {e}")

label_sinal = Label(aba_avancada, text="Sinal:")
label_sinal.pack()
entrada_sinal = Entry(aba_avancada)
entrada_sinal.pack()

botao_fourier = Button(aba_avancada, text="Calcular Fourier", command=transformada_fourier_plot)
botao_fourier.pack()

    # Funções de Engenharia Civil (implementar botões para acionar funções específicas)
    # ... (implementar botões para momento fletor, cortante
	# ... (código anterior para integração, derivada e transformada de Fourier)

# Funcionalidades básicas (utilizar widgets do tkinter)
def soma_interface():
    try:
        a = float(entrada_a_soma.get())
        b = float(entrada_b_soma.get())
        resultado = soma(a, b)
        label_resultado_soma.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

label_a_soma = Label(Aaba_basica, text="Valor de a:")
label_a_soma.pack()
entrada_a_soma = Entry(aba_basica)
entrada_a_soma.pack()

label_b_soma = Label(aba_basica, text="Valor de b:")
label_b_soma.pack()
entrada_b_soma = Entry(aba_basica)
entrada_b_soma.pack()

botao_somar = Button(aba_basica, text="Somar", command=soma_interface)
botao_somar.pack()

label_resultado_soma = Label(aba_basica, text="Resultado:")
label_resultado_soma.pack()

def subtracao_interface():
    try:
        a = float(entrada_a_subtracao.get())
        b = float(entrada_b_subtracao.get())
        resultado = subtracao(a, b)
        label_resultado_subtracao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

label_a_subtracao = Label(aba_basica, text="Valor de a:")
label_a_subtracao.pack()
entrada_a_subtracao = Entry(aba_basica)
entrada_a_subtracao.pack()

label_b_subtracao = Label(aba_basica, text="Valor de b:")
label_b_subtracao.pack()
entrada_b_subtracao = Entry(aba_basica)
entrada_b_subtracao.pack()

botao_subtrair = Button(aba_basica, text="Subtrair", command=subtracao_interface)
botao_subtrair.pack()

label_resultado_subtracao = Label(aba_basica, text="Resultado:")
label_resultado_subtracao.pack()

def multiplicacao_interface():
    try:
        a = float(entrada_a_multiplicacao.get())
        b = float(entrada_b_multiplicacao.get())
        resultado = multiplicacao(a, b)
        label_resultado_multiplicacao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

label_a_multiplicacao = Label(aba_basica, text="Valor de a:")
label_a_multiplicacao.pack()
entrada_a_multiplicacao = Entry(aba_basica)
entrada_a_multiplicacao.pack()

label_b_multiplicacao = Label(aba_basica, text="Valor de b:")
label_b_multiplicacao.pack()
entrada_b_multiplicacao = Entry(aba_basica)
entrada_b_multiplicacao.pack()

botao_multiplicar = Button(aba_basica, text="Multiplicar", command=multiplicacao_interface)
botao_multiplicar.pack()

label_resultado_multiplicacao = Label(aba_basica, text="Resultado:")
label_resultado_multiplicacao.pack()

def divisao_interface():
    try:
        a = float(entrada_a_divisao.get())
        b = float(entrada_b_divisao.get())
        resultado = divisao(a, b)
        label_resultado_divisao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero!")

label_a_divisao = Label(aba_basica, text="Valor de a:")
label_a_

# ... (código anterior para soma, subtração, multiplicação e divisão)

# Funcionalidades de memória (utilizar widgets do tkinter)
def adicionar_memoria_interface():
    nome = entrada_nome_memoria.get()
    valor_str = entrada_valor_memoria.get()
    try:
        valor = float(valor_str)
        adicionar_memoria(nome, valor)
        messagebox.showinfo("Informação", f"Valor '{valor}' armazenado na memória com nome '{nome}'.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido!")

label_nome_memoria = Label(aba_basica, text="Nome:")
label_nome_memoria.pack()
entrada_nome_memoria = Entry(aba_basica)
entrada_nome_memoria.pack()

label_valor_memoria = Label(aba_basica, text="Valor:")
label_valor_memoria.pack()
entrada_valor_memoria = Entry(aba_basica)
entrada_valor_memoria.pack()

botao_adicionar_memoria = Button(aba_basica, text="Adicionar", command=adicionar_memoria_interface)
botao_adicionar_memoria.pack()

def remover_memoria_interface():
    nome = entrada_nome_memoria_remover.get()
    remover_memoria(nome)
    messagebox.showinfo("Informação", f"Valor com nome '{nome}' removido da memória.")

label_nome_memoria_remover = Label(aba_basica, text="Nome:")
label_nome_memoria_remover.pack()
entrada_nome_memoria_remover = Entry(aba_basica)
entrada_nome_memoria_remover.pack()

botao_remover_memoria = Button(aba_basica, text="Remover", command=remover_memoria_interface)
botao_remover_memoria.pack()

def consultar_memoria_interface():
    nome = entrada_nome_memoria_consultar.get()
    valor = consultar_memoria(nome)
    if valor is not None:
        messagebox.showinfo("Informação", f"Valor do nome '{nome}': {valor}")
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

label_nome_memoria_consultar = Label(aba_basica, text="Nome:")
label_nome_memoria_consultar.pack()
entrada_nome_memoria_consultar = Entry(aba_basica)
entrada_nome_memoria_consultar.pack()

botao_consultar_memoria = Button(aba_basica, text="Consultar", command=consultar_memoria_interface)
botao_consultar_memoria.pack()

def limpar_memoria_interface():
    limpar_memoria()
    messagebox.showinfo("Informação", "Memória limpa.")

botao_limpar_memoria = Button(aba_basica, text="Limpar Memória", command=limpar_memoria_interface)
botao_limpar_memoria.pack()