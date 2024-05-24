
import math
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import messagebox

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

from tkinter import messagebox
from math import sqrt

# Funções para potenciação e radiciação
def potenciacao(a, n):
    return a ** n

def raiz_quadrada(a):
    if a < 0:
        messagebox.showerror("Erro", "Raiz quadrada de número negativo!")
        return None
    else:
        return a ** 0.5

def raiz_n_esima(a, n):
    if a < 0 and n % 2 == 0:
        messagebox.showerror("Erro", "Raiz n-ésima complexa!")
        return None
    else:
        return a ** (1 / n)

import math
from tkinter import messagebox

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

from tkinter import messagebox

memoria = {}

def adicionar_memoria(nome, valor):
    memoria[nome] = valor

def remover_memoria(nome):
    if nome in memoria:
        del memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def consultar_memoria(nome):
    if nome in memoria:
        return memoria[nome]
    else:
        messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

def limpar_memoria():
    memoria.clear()
    messagebox.showinfo("Informação", "Memória limpa.")


import integrate
from tkinter import messagebox

def integral_numerica(funcao_str, a, b, n):
    try:
        # Converter a função string em função Python
        funcao = eval(funcao_str)
        resultado = integrate.quad(funcao, a, b, epsabs=1e-5, reltol=1e-9, maxfun=n)[0]
        return resultado
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None

from tkinter import messagebox

def derivada_numerica(funcao_str, x, h):
    try:
        # Converter a função string em função Python
        funcao = eval(funcao_str)
        derivada = (funcao(x + h) - funcao(x - h)) / (2 * h)
        return derivada
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao avaliar a função: {e}")
        return None

import numpy as np

def transformada_fourier(sinal):
    try:
        fourier = np.fft.fft(sinal)
        return fourier
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular a transformada de Fourier: {e}")
        return None

def momento_fletor(forca, distancia, tipo_apoio):
    # Implementar a lógica para cálculo de momento fletor considerando o tipo de apoio (engastada, bi-apoiada, etc.)
    if tipo_apoio == "engastada":
        return forca * distancia
    elif tipo_apoio == "bi-apoiada":
        return forca * distancia / 2
    else:
        raise ValueError("Tipo de apoio não reconhecido.")

def normal(area, tensao):
    # Implementar a Lei de Hooke para calcular a força normal
    return area * tensao

def analise_esforcos_composta(materiais, geometrias):
    # Inicializar variáveis para os esforços totais
    forca_normal_total = 0
    momento_fletor_total = 0
    cortante_total = 0

    # Iterar sobre cada parte da viga composta
    for material, geometria in zip(materiais, geometrias):
        # Calcular a força normal e o momento fletor para cada parte
        area = geometria['area']
        tensao = material['tensao']
        forca_normal = normal(area, tensao)
        momento_fletor = momento_fletor(forca_normal, geometria['distancia'], tipo_apoio=geometria['tipo_apoio'])
        cortante = cortante(forca_normal, geometria['distancia'], tipo_apoio=geometria['tipo_apoio'])

        # Somar os esforços totais
        forca_normal_total += forca_normal
        momento_fletor_total += momento_fletor
        cortante_total += cortante

    # Retornar os esforços totais
    return forca_normal_total, momento_fletor_total, cortante_total

def dimensionamento_coluna(carga, material, comprimento):
    # Implementação simplificada considerando apenas a carga de compressão e o material da coluna
    area = 0.1  # Área de seção transversal da coluna (m²)
    tensao = material['tensao']  # Tensão máxima admissível do material (N/m²)
    forca_normal = normal(area, tensao)
    if forca_normal >= carga:
        return "Coluna dimensionada corretamente."
    else:
        return "Coluna subdimensionada. Aumente a área da seção transversal."

def calculo_laje(carga, vao, material, espessura):
    # Implementação simplificada considerando uma laje biapoiada com carga uniforme
    largura = 1.0  # Largura da laje (m)
    momento_fletor_maximo = carga * vao ** 2 / 8  # Momento fletor máximo (N.m)
    tensao_maxima = momento_fletor_maximo / (largura * espessura ** 2 / 6)  # Tensão máxima (N/m²)
    if tensao_maxima <= material['tensao']:
        return "Laje dimensionada corretamente."
    else:
        return "Laje subdimensionada. Aumente a espessura da laje."

def capacidade_carga_estacas(metodo, parametros):
    if metodo == "Meyerhof":
        # Implementar cálculo da capacidade de carga de estacas pelo método de Meyerhof
        pass
    elif metodo == "Terzaghi":
        # Implementar cálculo da capacidade de carga de estacas pelo método de Terzaghi
        pass
    else:
        raise ValueError("Método não reconhecido.")

def estabilidade_talude(metodo, parametros):
    if metodo == "Mohr-Coulomb":
        # Implementar análise da estabilidade de taludes pelo método de Mohr-Coulomb
        pass
    elif metodo == "Bishop":
        # Implementar análise da estabilidade de taludes pelo método de Bishop
        pass
    else:
        raise ValueError("Método não reconhecido.")

def permeabilidade_solo(metodo, parametros):
    if metodo == "Teste de permeabilidade":
        # Implementar cálculo da permeabilidade do solo pelo teste de permeabilidade
        pass
    else:
        raise ValueError("Método não reconhecido.")

def recalque_solo(metodo, parametros):
    if metodo == "Elasticidade":
        # Implementar cálculo de recalque do solo pelo método de elasticidade
        pass
    elif metodo == "Winkler":
        # Implementar cálculo de recalque do solo pelo método de Winkler
        pass
    else:
        raise ValueError("Método não reconhecido.")

def fluxo_tubulacao(vazao, diametro, rugosidade):
    # Implementação simplificada da equação de Darcy-Weisbach
    from math import pi, sqrt
    g = 9.81  # Aceleração devido à gravidade (m/s²)
    rugosidade_absoluta = rugosidade * diametro
    area = pi * (diametro / 2)**2
    velocidade = vazao / area
    fator_friction = 0.02  # Fator de atrito (valor de exemplo)
    perda_carga = fator_friction * (velocidade**2) * (diametro / (2 * g))
    return perda_carga
def fluxo_canal(area_molhada, declividade, rugosidade):
    # Implementação simplificada da equação de Manning
    n = 0.03  # Rugosidade de Manning (valor de exemplo)
    raio_hidraulico = area_molhada / (2 * (area_molhada)**0.5)
    velocidade = (1 / n) * (raio_hidraulico**(2/3)) * (declividade**0.5)
    return velocidade
def dimensionamento_rede_hidraulica(metodo, parametros):
    if metodo == "NBR10838":
        # Implementação simplificada do dimensionamento conforme norma NBR 10838
        diametro = parametros['vazao'] * 4 / (pi * parametros['velocidade'])
        return diametro
    else:
        raise ValueError("Método não reconhecido.")

def tratamento_agua(metodo, parametros):
    if metodo == "Coagulacao":
        # Implementação simplificada do tratamento por coagulação
        if parametros['ph'] < 7:
            return "Adicionar coagulante para aumentar o pH"
        else:
            return "Água tratada com sucesso"
    else:
        raise ValueError("Método de tratamento de água não reconhecido")

# Exemplo de uso:
parametros_agua = {'ph': 6.5, 'turbidez': 20}  # Parâmetros da água
print(tratamento_agua("Coagulacao", parametros_agua))
def tratamento_esgoto(metodo, parametros):
    if metodo == "Ativacao_lodo":
        # Implementação simplificada do tratamento por ativação de lodo
        if parametros['carga_organica'] > 50:
            return "Ativar lodo biológico para degradação de matéria orgânica"
        else:
            return "Esgoto tratado com sucesso"
    else:
        raise ValueError("Método de tratamento de esgoto não reconhecido")

# Exemplo de uso:
parametros_esgoto = {'carga_organica': 60}  # Parâmetros do esgoto
print(tratamento_esgoto("Ativacao_lodo", parametros_esgoto))

def area_terreno(vertices):
    # Supondo que vertices é uma lista de coordenadas (x, y) dos vértices do terreno
    # Implementação simplificada do método do polígono
    area = 0
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    area = abs(area) / 2
    return area
def volume_terreno(area, profundidade):
    # Implementação simples: volume = área * profundidade
    volume = area * profundidade
    return volume
def nivelamento(pontos):
    # Supondo que pontos é uma lista de alturas
    # Implementação simplificada: calcular a média das alturas
    altura_media = sum(pontos) / len(pontos)
    return altura_media
def locacao_obra(coordenadas):
    # Supondo que coordenadas é uma lista de coordenadas (x, y)
    # Implementação simplificada: calcular a média das coordenadas
    x_media = sum(coord[0] for coord in coordenadas) / len(coordenadas)
    y_media = sum(coord[1] for coord in coordenadas) / len(coordenadas)
    return x_media, y_media
def curva_nivel(pontos):
    # Supondo que pontos é uma lista de alturas em diferentes pontos
    # Implementação simplificada: traçar curvas de nível conectando pontos com a mesma altura
    curvas_nivel = {}
    for altura in set(pontos):
        curvas_nivel[altura] = [(x, y) for x, y in pontos if y == altura]
    return curvas_nivel
# Continuação do código anterior

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
label_titulo_engenharia_civil = tk.Label(aba_engenharia_civil, text="Engenharia Civil")
label_titulo_engenharia_civil.pack()

def calcular_momento_fletor():
    # Implemente a lógica para calcular o momento fletor aqui
    pass

def calcular_cortante():
    # Implemente a lógica para calcular o cortante aqui
    pass

# Botões para calcular momento fletor e cortante
botao_momento_fletor = tk.Button(aba_engenharia_civil, text="Calcular Momento Fletor", command=calcular_momento_fletor)
botao_momento_fletor.pack()

botao_cortante = tk.Button(aba_engenharia_civil, text="Calcular Cortante", command=calcular_cortante)
botao_cortante.pack()

# Chamada da interface gráfica
interface()

def divisao_interface():
    try:
        a = float(entrada_a_divisao.get())
        b = float(entrada_b_divisao.get())
        resultado = divisao(a, b)
        if resultado is not None:
            label_resultado_divisao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero!")

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
from tkinter import *
from tkinter import messagebox

memoria = {}

# Função para adicionar um valor à memória
def adicionar_memoria(nome, valor):
    memoria[nome] = valor

# Função para remover um valor da memória
def remover_memoria(nome):
    if nome in memoria:
        del memoria[nome]
    else:
        raise KeyError(f"Nome '{nome}' não encontrado na memória.")

# Função para consultar um valor na memória
def consultar_memoria(nome):
    return memoria.get(nome)

# Função para limpar a memória
def limpar_memoria():
    memoria.clear()
    messagebox.showinfo("Informação", "Memória limpa.")

# Interface gráfica para as funcionalidades de memória
def interface_memoria():
    janela = Tk()
    janela.title("Memória")

    # Adicionar à memória
    def adicionar_interface():
        nome = entrada_nome.get()
        valor_str = entrada_valor.get()
        try:
            valor = float(valor_str)
            adicionar_memoria(nome, valor)
            messagebox.showinfo("Informação", f"Valor '{valor}' armazenado na memória com nome '{nome}'.")
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido!")

    label_nome = Label(janela, text="Nome:")
    label_nome.pack()
    entrada_nome = Entry(janela)
    entrada_nome.pack()

    label_valor = Label(janela, text="Valor:")
    label_valor.pack()
    entrada_valor = Entry(janela)
    entrada_valor.pack()

    botao_adicionar = Button(janela, text="Adicionar", command=adicionar_interface)
    botao_adicionar.pack()

    # Remover da memória
    def remover_interface():
        nome = entrada_nome_remover.get()
        try:
            remover_memoria(nome)
            messagebox.showinfo("Informação", f"Valor com nome '{nome}' removido da memória.")
        except KeyError:
            messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

    label_nome_remover = Label(janela, text="Nome:")
    label_nome_remover.pack()
    entrada_nome_remover = Entry(janela)
    entrada_nome_remover.pack()

    botao_remover = Button(janela, text="Remover", command=remover_interface)
    botao_remover.pack()

    # Consultar memória
    def consultar_interface():
        nome = entrada_nome_consultar.get()
        valor = consultar_memoria(nome)
        if valor is not None:
            messagebox.showinfo("Informação", f"Valor do nome '{nome}': {valor}")
        else:
            messagebox.showinfo("Informação", f"Nome '{nome}' não encontrado na memória.")

    label_nome_consultar = Label(janela, text="Nome:")
    label_nome_consultar.pack()
    entrada_nome_consultar = Entry(janela)
    entrada_nome_consultar.pack()

    botao_consultar = Button(janela, text="Consultar", command=consultar_interface)
    botao_consultar.pack()

    # Limpar memória
    def limpar_interface():
        limpar_memoria()
        janela.destroy()

    botao_limpar = Button(janela, text="Limpar Memória", command=limpar_interface)
    botao_limpar.pack()

    janela.mainloop()

# Chamar a função para iniciar a interface de memória
interface_memoria()

from tkinter import *
from tkinter import ttk, messagebox

# Função para calcular o momento fletor
def momento_fletor(forca, distancia, tipo_apoio):
    try:
        if tipo_apoio == "engasta":
            return forca * distancia
        elif tipo_apoio == "bi-apoiada":
            return forca * distancia / 2
        elif tipo_apoio == "encastre-livre":
            return forca * distancia / 3
        else:
            raise ValueError("Tipo de apoio não reconhecido.")
    except ZeroDivisionError:
        return None

# Interface gráfica para a funcionalidade de momento fletor
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

# Criar a janela principal
janela = Tk()
janela.title("Calculadora de Engenharia Civil")

# Criar aba para as funcionalidades de Engenharia Civil
aba_engenharia_civil = ttk.Frame(janela)
aba_engenharia_civil.pack(expand=True, fill="both")

# Adicionar campos de entrada e botão para o momento fletor
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

botao_mf = Button(aba_engenharia_civil, text="Calcular Momento Fletor", command=momento_fletor_interface)
botao_mf.pack()

label_resultado_mf = Label(aba_engenharia_civil, text="Resultado:")
label_resultado_mf.pack()

# ... (adicionar interfaces para outras funcionalidades de Engenharia Civil, como o cálculo de cortante)

# Iniciar a interface gráfica
janela.mainloop()

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

def potenciacao_interface():
    try:
        base = float(entrada_base_potenciacao.get())
        expoente = float(entrada_expoente_potenciacao.get())
        resultado = potenciacao(base, expoente)
        label_resultado_potenciacao.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

def raiz_quadrada_interface():
    try:
        numero = float(entrada_raiz_quadrada.get())
        resultado = raiz_quadrada(numero)
        if resultado is not None:
            label_resultado_raiz_quadrada.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Erro", "Não é possível calcular a raiz quadrada de um número negativo.")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar um número.")

def raiz_n_esima_interface():
    try:
        numero = float(entrada_raiz_n_esima_numero.get())
        indice = float(entrada_raiz_n_esima_indice.get())
        resultado = raiz_n_esima(numero, indice)
        if resultado is not None:
            label_resultado_raiz_n_esima.config(text=f"Resultado: {resultado}")
        else:
            messagebox.showerror("Erro", "Não é possível calcular a raiz n-ésima de um número negativo com índice par.")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Certifique-se de digitar números.")

# Interfaces gráficas para potenciação, raiz quadrada e raiz n-ésima
label_base_potenciacao = Label(aba_basica, text="Base:")
label_base_potenciacao.pack()
entrada_base_potenciacao = Entry(aba_basica)
entrada_base_potenciacao.pack()

label_expoente_potenciacao = Label(aba_basica, text="Expoente:")
label_expoente_potenciacao.pack()
entrada_expoente_potenciacao = Entry(aba_basica)
entrada_expoente_potenciacao.pack()

botao_potenciar = Button(aba_basica, text="Potenciar", command=potenciacao_interface)
botao_potenciar.pack()

label_resultado_potenciacao = Label(aba_basica, text="Resultado:")
label_resultado_potenciacao.pack()

label_numero_raiz_quadrada = Label(aba_basica, text="Número:")
label_numero_raiz_quadrada.pack()
entrada_raiz_quadrada = Entry(aba_basica)
entrada_raiz_quadrada.pack()

botao_raiz_quadrada = Button(aba_basica, text="Raiz Quadrada", command=raiz_quadrada_interface)
botao_raiz_quadrada.pack()

label_resultado_raiz_quadrada = Label(aba_basica, text="Resultado:")
label_resultado_raiz_quadrada.pack()

label_numero_raiz_n_esima = Label(aba_basica, text="Número:")
label_numero_raiz_n_esima.pack()
entrada_raiz_n_esima_numero = Entry(aba_basica)
entrada_raiz_n_esima_numero.pack()

label_indice_raiz_n_esima = Label(aba_basica, text="Índice:")
label_indice_raiz_n_esima.pack()
entrada_raiz_n_esima_indice = Entry(aba_basica)
entrada_raiz_n_esima_indice.pack()

botao_raiz_n_esima = Button(aba_basica, text="Raiz N-ésima", command=raiz_n_esima_interface)
botao_raiz_n_esima.pack()

label_resultado_raiz_n_esima = Label(aba_basica, text="Resultado:")
label_resultado_raiz_n_esima.pack()

# Interface Gráfica para Cálculo de Momento Fletor (aba_engenharia_civil)
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

botao_calcular_mf = Button(aba_engenharia_civil, text="Calcular", command=momento_fletor_interface)
botao_calcular_mf.pack()

label_resultado_mf = Label(aba_engenharia_civil, text="Resultado:")
label_resultado_mf.pack()




