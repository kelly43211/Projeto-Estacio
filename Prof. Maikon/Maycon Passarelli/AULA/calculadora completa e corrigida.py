import tkinter as tk
from tkinter import messagebox
import math
from scipy import integrate
import numpy as np
from tkinter import *
from math import sqrt

# Função para exibir uma mensagem de erro
def mostrar_erro(mensagem):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Erro", mensagem)
    root.destroy()

# Função para exibir uma mensagem informativa
def mostrar_informacao(mensagem):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Informação", mensagem)
    root.destroy()

# Função para adicionar um valor à memória
def adicionar_memoria(nome, valor):
    memoria[nome] = valor

# Função para remover um valor da memória
def remover_memoria(nome):
    if nome in memoria:
        del memoria[nome]
    else:
        mostrar_informacao(f"Nome '{nome}' não encontrado na memória.")

# Função para consultar um valor na memória
def consultar_memoria(nome):
    if nome in memoria:
        return memoria[nome]
    else:
        mostrar_informacao(f"Nome '{nome}' não encontrado na memória.")

# Função para limpar a memória
def limpar_memoria():
    memoria.clear()
    mostrar_informacao("Memória limpa.")

# Função para calcular a integral numérica
def integral_numerica(funcao_str, a, b, n):
    try:
        funcao = lambda x: eval(funcao_str)
        resultado = integrate.quad(funcao, a, b, epsabs=1e-5, reltol=1e-9, maxfun=n)[0]
        return resultado
    except Exception as e:
        mostrar_erro(f"Erro ao avaliar a função: {e}")
        return None

# Função para calcular a derivada numérica
def derivada_numerica(funcao_str, x, h):
    try:
        funcao = lambda x: eval(funcao_str)
        derivada = (funcao(x + h) - funcao(x - h)) / (2 * h)
        return derivada
    except Exception as e:
        mostrar_erro(f"Erro ao avaliar a função: {e}")
        return None

# Inicialização da memória como um dicionário vazio
memoria = {}

def transformada_fourier(sinal):
    fourier = np.fft.fft(sinal)
    return fourier
def momento_fletor(forca, distancia, tipo_apoio):
    if tipo_apoio == "engastada":
        return forca * distancia
    elif tipo_apoio == "biapoiada":
        return forca * distancia / 2
    else:
        raise ValueError("Tipo de apoio não reconhecido")

def cortante(forca, distancia, tipo_apoio):
    if tipo_apoio == "engastada":
        return forca
    elif tipo_apoio == "biapoiada":
        return forca / 2
    else:
        raise ValueError("Tipo de apoio não reconhecido")

def normal(area, tensao):
    return area * tensao

def analise_esforcos_composta(materiais, geometrias):
    # Lógica para análise de esforços em vigas compostas
    pass

def dimensionamento_coluna(carga, material, comprimento):
    # Lógica para dimensionamento de colunas utilizando normas como a NBR 6118
    pass

def calculo_laje(carga, vao, material, espessura):
    # Lógica para cálculo de lajes utilizando métodos como o método de vigas biapoiadas
    pass
def capacidade_carga_estacas(metodo, parametros):
    if metodo == "Meyerhof":
        # Lógica para calcular a capacidade de carga de estacas usando o método de Meyerhof
        pass
    elif metodo == "Terzaghi":
        # Lógica para calcular a capacidade de carga de estacas usando o método de Terzaghi
        pass
    else:
        raise ValueError("Método não reconhecido")

def estabilidade_talude(metodo, parametros):
    if metodo == "Mohr-Coulomb":
        # Lógica para análise da estabilidade de taludes usando o método de Mohr-Coulomb
        pass
    elif metodo == "Bishop":
        # Lógica para análise da estabilidade de taludes usando o método de Bishop
        pass
    else:
        raise ValueError("Método não reconhecido")

def permeabilidade_solo(metodo, parametros):
    if metodo == "teste_permeabilidade":
        # Lógica para cálculo da permeabilidade do solo usando métodos como teste de permeabilidade
        pass
    else:
        raise ValueError("Método não reconhecido")

def recalque_solo(metodo, parametros):
    if metodo == "elasticidade":
        # Lógica para cálculo de recalque do solo usando o método de elasticidade
        pass
    elif metodo == "Winkler":
        # Lógica para cálculo de recalque do solo usando o método de Winkler
        pass
    else:
        raise ValueError("Método não reconhecido")
def fluxo_tubulacao(vazao, diametro, rugosidade):
    # Lógica para cálculo do fluxo em tubulações utilizando equações como Darcy-Weisbach
    pass

def fluxo_canal(area_molhada, declividade, rugosidade):
    # Lógica para cálculo do fluxo em canais abertos utilizando equações como Manning
    pass

def dimensionamento_rede_hidraulica(metodo, parametros):
    # Lógica para dimensionamento de redes hidráulicas utilizando normas como NBR 10838
    pass

def tratamento_agua(metodo, parametros):
    # Lógica para cálculo de estações de tratamento de água utilizando métodos como coagulação
    pass

def tratamento_esgoto(metodo, parametros):
    # Lógica para cálculo de estações de tratamento de esgoto utilizando métodos como ativação por lodo
    pass
def area_terreno(vertices):
    # Lógica para cálculo da área de um terreno utilizando métodos como planímetro
    pass

def volume_terreno(area, profundidade):
    # Lógica para cálculo do volume de um terreno
    pass

def nivelamento(pontos):
    # Lógica para nivelamento utilizando instrumentos como o nível
    pass

def locacao_obra(coordenadas):
    # Lógica para locação de obras utilizando instrumentos como o teodolito
    pass

def curva_nivel(pontos):
    # Lógica para traçado de curvas de nível utilizando métodos de interpolação
    pass


def momento_fletor_interface():
    try:
        forca = float(entrada_forca_mf.get())
        distancia = float(entrada_distancia_mf.get())
        tipo_apoio = entrada_tipo_apoio_mf.get()
        
        resultado = momento_fletor(forca, distancia, tipo_apoio)  # Supondo que você já implementou a função momento_fletor
        
        label_resultado_mf.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da interface gráfica
app = tk.Tk()
app.title("Calculadora Avançada")

# Criando abas para diferentes funcionalidades
aba_basica = tk.Frame(app)
aba_avancada = tk.Frame(app)
aba_memoria = tk.Frame(app)
aba_engenharia_civil = tk.Frame(app)

aba_basica.pack(side="top", fill="both", expand=True)
aba_avancada.pack(side="top", fill="both", expand=True)
aba_memoria.pack(side="top", fill="both", expand=True)
aba_engenharia_civil.pack(side="top", fill="both", expand=True)

# Criação dos widgets na aba de engenharia civil
label_forca_mf = tk.Label(aba_engenharia_civil, text="Força (N):")
label_forca_mf.pack()
entrada_forca_mf = tk.Entry(aba_engenharia_civil)
entrada_forca_mf.pack()

label_distancia_mf = tk.Label(aba_engenharia_civil, text="Distância (m):")
label_distancia_mf.pack()
entrada_distancia_mf = tk.Entry(aba_engenharia_civil)
entrada_distancia_mf.pack()

label_tipo_apoio_mf = tk.Label(aba_engenharia_civil, text="Tipo de Apoio:")
label_tipo_apoio_mf.pack()
entrada_tipo_apoio_mf = tk.Entry(aba_engenharia_civil)
entrada_tipo_apoio_mf.pack()

botao_calcular_mf = tk.Button(aba_engenharia_civil, text="Calcular", command=momento_fletor_interface)
botao_calcular_mf.pack()

label_resultado_mf = tk.Label(aba_engenharia_civil, text="Resultado:")
label_resultado_mf.pack()

app.mainloop()



def soma_interface():
    try:
        a = float(entrada_a_soma.get())
        b = float(entrada_b_soma.get())
        resultado = soma(a, b)
        label_resultado_soma.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def subtracao_interface():
    try:
        a = float(entrada_a_subtracao.get())
        b = float(entrada_b_subtracao.get())
        resultado = subtracao(a, b)
        label_resultado_subtracao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

def multiplicacao_interface():
    try:
        a = float(entrada_a_multiplicacao.get())
        b = float(entrada_b_multiplicacao.get())
        resultado = multiplicacao(a, b)
        label_resultado_multiplicacao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

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

app = Tk()
app.title("Calculadora Básica")

aba_basica = Frame(app)
aba_basica.pack()

# Soma
label_a_soma = Label(aba_basica, text="Valor de a:")
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

# Subtração
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

# Multiplicação
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

# Divisão
label_a_divisao = Label(aba_basica, text="Valor de a:")
label_a_divisao.pack()
entrada_a_divisao = Entry(aba_basica)
entrada_a_divisao.pack()

label_b_divisao = Label(aba_basica, text="Valor de b:")
label_b_divisao.pack()
entrada_b_divisao = Entry(aba_basica)
entrada_b_divisao.pack()

botao_dividir = Button(aba_basica, text="Dividir", command=divisao_interface)
botao_dividir.pack()

label_resultado_divisao = Label(aba_basica, text="Resultado:")
label_resultado_divisao.pack()

app.mainloop()

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
from tkinter import *
from tkinter import messagebox

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
from tkinter import *
from tkinter import messagebox

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

# Definições das funções de cálculo
def momento_fletor(forca, distancia, tipo_apoio):
    if tipo_apoio == "engasta":
        return forca * distancia
    elif tipo_apoio == "bi-apoiada":
        return forca * distancia / 2
    elif tipo_apoio == "encastre-livre":
        return forca * distancia / 3
    else:
        raise ValueError("Tipo de apoio inválido.")

def cortante(forca, distancia, tipo_apoio):
    if tipo_apoio == "engasta":
        return forca
    elif tipo_apoio == "bi-apoiada":
        return forca / 2
    elif tipo_apoio == "encastre-livre":
        return forca / 3
    else:
        raise ValueError("Tipo de apoio inválido.")

# Definições das funções de interface
def momento_fletor_interface():
    try:
        forca = float(entrada_forca_mf.get())
        distancia = float(entrada_distancia_mf.get())
        tipo_apoio = entrada_tipo_apoio_mf.get().lower()

        if tipo_apoio not in ["engasta", "bi-apoiada", "encastre-livre"]:
            raise ValueError("Tipo de apoio inválido.")

        resultado = momento_fletor(forca, distancia, tipo_apoio)
        if resultado is not None:
            label_resultado_mf.config(text=f"Momento Fletor: {resultado:.4f} N.m")
        else:
            messagebox.showerror("Erro", "Falha ao calcular o momento fletor.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

def cortante_interface():
    try:
        forca = float(entrada_forca_cortante.get())
        distancia = float(entrada_distancia_cortante.get())
        tipo_apoio = entrada_tipo_apoio_cortante.get().lower()

        if tipo_apoio not in ["engasta", "bi-apoiada", "encastre-livre"]:
            raise ValueError("Tipo de apoio inválido.")

        resultado = cortante(forca, distancia, tipo_apoio)
        if resultado is not None:
            label_resultado_cortante.config(text=f"Cortante: {resultado:.4f} N")
        else:
            messagebox.showerror("Erro", "Falha ao calcular o cortante.")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

# Interface gráfica
app = Tk()
app.title("Calculadora Engenharia Civil")

aba_engenharia_civil = Frame(app)
aba_engenharia_civil.pack(side="top", fill="both", expand=True)

# Entradas e botões para o cálculo do momento fletor
label_forca_mf = Label(aba_engenharia_civil, text="Força (N):")
label_forca_mf.pack()
entrada_forca_mf = Entry(aba_engenharia_civil)
entrada_forca_mf.pack()

label_distancia_mf = Label(aba_engenharia_civil, text="Distância (m):")
label_distancia_mf.pack()
entrada_distancia_mf = Entry(aba_engenharia_civil)
entrada_distancia_mf.pack()

label_tipo_apoio_mf = Label(aba_engenharia_civil, text="Tipo de Apoio:")
label_tipo_apoio_mf.pack()
entrada_tipo_apoio_mf = Entry(aba_engenharia_civil)
entrada_tipo_apoio_mf.pack()

botao_calcular_mf = Button(aba_engenharia_civil, text="Calcular Momento Fletor", command=momento_fletor_interface)
botao_calcular_mf.pack()

label_resultado_mf = Label(aba_engenharia_civil, text="Resultado:")
label_resultado_mf.pack()

# Entradas e botões para o cálculo do cortante
label_forca_cortante = Label(aba_engenharia_civil, text="Força (N):")
label_forca_cortante.pack()
entrada_forca_cortante = Entry(aba_engenharia_civil)
entrada_forca_cortante.pack()

label_distancia_cortante = Label(aba_engenharia_civil, text="Distância (m):")
label_distancia_cortante.pack()
entrada_distancia_cortante = Entry(aba_engenharia_civil)
entrada_distancia_cortante.pack()

label_tipo_apoio_cortante = Label(aba_engenharia_civil, text="Tipo de Apoio:")
label_tipo_apoio_cortante.pack()
entrada_tipo_apoio_cortante = Entry(aba_engenharia_civil)
entrada_tipo_apoio_cortante.pack()

botao_calcular_cortante = Button(aba_engenharia_civil, text="Calcular Cortante", command=cortante_interface)
botao_calcular_cortante.pack()

label_resultado_cortante = Label(aba_engenharia_civil, text="Resultado:")
label_resultado_cortante.pack()

app.mainloop()

def divisao_interface():
    try:
        a = float(entrada_a_divisao.get())
        b = float(entrada_b_divisao.get())
        resultado = divisao(a, b)
        if resultado is not None:
            label_resultado_divisao.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Erro", "Divisão por zero!")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

label_a_divisao = Label(aba_basica, text="Valor de a:")
label_a_divisao.pack()
entrada_a_divisao = Entry(aba_basica)
entrada_a_divisao.pack()

label_b_divisao = Label(aba_basica, text="Valor de b:")
label_b_divisao.pack()
entrada_b_divisao = Entry(aba_basica)
entrada_b_divisao.pack()

botao_dividir = Button(aba_basica, text="Dividir", command=divisao_interface)
botao_dividir.pack()

label_resultado_divisao = Label(aba_basica, text="Resultado:")
label_resultado_divisao.pack()

# Agora você pode prosseguir com o restante do código para outras funções básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return None  # Divisão por zero, retorne None ou outra indicação de erro
    else:
        return a / b

# Agora você pode prosseguir com a definição da interface gráfica para a função de divisão e outras funções básicas
def divisao_interface():
    try:
        a = float(entrada_a_divisao.get())
        b = float(entrada_b_divisao.get())
        resultado = divisao(a, b)
        if resultado is not None:
            label_resultado_divisao.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Erro", "Divisão por zero!")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

label_a_divisao = Label(aba_basica, text="Valor de a:")
label_a_divisao.pack()
entrada_a_divisao = Entry(aba_basica)
entrada_a_divisao.pack()

label_b_divisao = Label(aba_basica, text="Valor de b:")
label_b_divisao.pack()
entrada_b_divisao = Entry(aba_basica)
entrada_b_divisao.pack()

botao_dividir = Button(aba_basica, text="Dividir", command=divisao_interface)
botao_dividir.pack()

label_resultado_divisao = Label(aba_basica, text="Resultado:")
label_resultado_divisao.pack()

# Agora você pode prosseguir com o restante do código para outras funções básicas
def adicionar_memoria_interface():
    nome = entrada_nome_memoria.get()
    valor_str = entrada_valor_memoria.get()
    try:
        valor = float(valor_str)
        adicionar_memoria(nome, valor)
        messagebox.showinfo("Informação", f"Valor '{valor}' armazenado na memória com nome '{nome}'.")
    except ValueError:
        messagebox.showerror("Erro", "Valor inválido!")

label_nome_memoria = Label(aba_memoria, text="Nome:")
label_nome_memoria.pack()
entrada_nome_memoria = Entry(aba_memoria)
entrada_nome_memoria.pack()

label_valor_memoria = Label(aba_memoria, text="Valor:")
label_valor_memoria.pack()
entrada_valor_memoria = Entry(aba_memoria)
entrada_valor_memoria.pack()

botao_adicionar_memoria = Button(aba_memoria, text="Adicionar", command=adicionar_memoria_interface)
botao_adicionar_memoria.pack()

label_titulo_basica = tk.Label(aba_basica, text="Funções Básicas")
label_titulo_basica.pack()

label_a_soma = tk.Label(aba_basica, text="Valor de a:")
label_a_soma.pack()
entrada_a_soma = tk.Entry(aba_basica)
entrada_a_soma.pack()

label_b_soma = tk.Label(aba_basica, text="Valor de b:")
label_b_soma.pack()
entrada_b_soma = tk.Entry(aba_basica)
entrada_b_soma.pack()

botao_somar = tk.Button(aba_basica, text="Somar", command=lambda: soma_interface(entrada_a_soma, entrada_b_soma))
botao_somar.pack()

label_resultado_soma = tk.Label(aba_basica, text="Resultado:")
label_resultado_soma.pack()

# Interface para a subtração
label_a_subtracao = tk.Label(aba_basica, text="Valor de a:")
label_a_subtracao.pack()
entrada_a_subtracao = tk.Entry(aba_basica)
entrada_a_subtracao.pack()

label_b_subtracao = tk.Label(aba_basica, text="Valor de b:")
label_b_subtracao.pack()
entrada_b_subtracao = tk.Entry(aba_basica)
entrada_b_subtracao.pack()

botao_subtrair = tk.Button(aba_basica, text="Subtrair", command=lambda: subtracao_interface(entrada_a_subtracao, entrada_b_subtracao))
botao_subtrair.pack()

label_resultado_subtracao = tk.Label(aba_basica, text="Resultado:")
label_resultado_subtracao.pack()

# Interface para a multiplicação
label_a_multiplicacao = tk.Label(aba_basica, text="Valor de a:")
label_a_multiplicacao.pack()
entrada_a_multiplicacao = tk.Entry(aba_basica)
entrada_a_multiplicacao.pack()

label_b_multiplicacao = tk.Label(aba_basica, text="Valor de b:")
label_b_multiplicacao.pack()
entrada_b_multiplicacao = tk.Entry(aba_basica)
entrada_b_multiplicacao.pack()

botao_multiplicar = tk.Button(aba_basica, text="Multiplicar", command=lambda: multiplicacao_interface(entrada_a_multiplicacao, entrada_b_multiplicacao))
botao_multiplicar.pack()

label_resultado_multiplicacao = tk.Label(aba_basica, text="Resultado:")
label_resultado_multiplicacao.pack()

# Interface para a divisão
label_a_divisao = tk.Label(aba_basica, text="Valor de a:")
label_a_divisao.pack()
entrada_a_divisao = tk.Entry(aba_basica)
entrada_a_divisao.pack()

label_b_divisao = tk.Label(aba_basica, text="Valor de b:")
label_b_divisao.pack()
entrada_b_divisao = tk.Entry(aba_basica)
entrada_b_divisao.pack()

botao_dividir = tk.Button(aba_basica, text="Dividir", command=lambda: divisao_interface(entrada_a_divisao, entrada_b_divisao))
botao_dividir.pack()

label_resultado_divisao = tk.Label(aba_basica, text="Resultado:")
label_resultado_divisao.pack()



# Funções básicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return None
    return a / b

def potenciacao(base, expoente):
    return base ** expoente

def raiz_quadrada(numero):
    if numero < 0:
        return None
    return sqrt(numero)

def raiz_n_esima(numero, indice):
    if numero < 0 and indice % 2 == 0:
        return None
    return numero ** (1 / indice)

# Funções para integração, derivada e transformada de Fourier
def integral_numerica(funcao_str, a, b, n):
    try:
        funcao = eval(funcao_str)
        resultado = integrate.quad(funcao, a, b, epsabs=1e-5, reltol=1e-9, maxfun=n)[0]
        return resultado
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None

def derivada_numerica(funcao_str, x, h):
    try:
        funcao = eval(funcao_str)
        derivada = (funcao(x + h) - funcao(x - h)) / (2 * h)
        return derivada
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None

def transformada_fourier(sinal):
    fourier = np.fft.fft(sinal)
    return fourier

# Interface gráfica
app = tk.Tk()
app.title("Calculadora Avançada")

# Funções básicas - Interface
label_titulo_basica = tk.Label(app, text="Funções Básicas")
label_titulo_basica.pack()

# Labels e Entradas para soma
label_a_soma = tk.Label(app, text="Valor de a:")
label_a_soma.pack()
entrada_a_soma = tk.Entry(app)
entrada_a_soma.pack()

label_b_soma = tk.Label(app, text="Valor de b:")
label_b_soma.pack()
entrada_b_soma = tk.Entry(app)
entrada_b_soma.pack()

# Botão para soma
def soma_interface():
    try:
        a = float(entrada_a_soma.get())
        b = float(entrada_b_soma.get())
        resultado = soma(a, b)
        label_resultado_soma.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números válidos.")

botao_somar = tk.Button(app, text="Somar", command=soma_interface)
botao_somar.pack()

# Label para resultado da soma
label_resultado_soma = tk.Label(app, text="Resultado:")
label_resultado_soma.pack()

# Mais labels, entradas e botões para outras funções básicas (subtração, multiplicação, divisão, etc.)

# Funções avançadas - Interface
label_titulo_avancada = tk.Label(app, text="Funções Avançadas")
label_titulo_avancada.pack()

# Implementar interfaces para integração, derivada e transformada de Fourier

app.mainloop()
label_titulo_memoria = tk.Label(aba_memoria, text="Memória")  # Correção: aba_memoria ao invés de "aba_memoria"
label_titulo_memoria.pack()

# Implemente as interfaces para as funções de memória aqui





