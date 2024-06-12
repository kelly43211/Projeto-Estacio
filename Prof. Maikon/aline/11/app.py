import tkinter as tk
from tkinter import ttk, messagebox
import os

# Interface gráfica principal
app = tk.Tk()
app.title("Calculadora Avançada")

# Funções para abrir os arquivos correspondentes
def open_calculos_estruturais():
    os.system("caminho_para_o_arquivo_calculos_estruturais.py")

def open_derivadas_numericas():
    os.system("caminho_para_o_arquivo_derivadas_numericas.py")

def open_divisao_interface():
    os.system("caminho_para_o_arquivo_divisao_interface.py")

def open_funcionalidades_basicas():
    os.system("caminho_para_o_arquivo_funcionalidades_basicas.py")

def open_funcionalidades_memoria():
    os.system("caminho_para_o_arquivo_funcionalidades_memoria.py")

def open_funcoes_avancadas():
    os.system("caminho_para_o_arquivo_funcoes_avancadas.py")

def open_funcoes_engenharia_civil():
    os.system("caminho_para_o_arquivo_funcoes_engenharia_civil.py")

def open_funcoes_matematicas():
    os.system("caminho_para_o_arquivo_funcoes_matematicas.py")

def open_hidraulica_e_saneamento():
    os.system("caminho_para_o_arquivo_hidraulica_e_saneamento.py")

def open_integral_numerica():
    os.system("caminho_para_o_arquivo_integral_numerica.py")

def open_mecanica_dos_solos():
    os.system("caminho_para_o_arquivo_mecanica_dos_solos.py")

def open_operacoes_memoria():
    os.system("caminho_para_o_arquivo_operacoes_memoria.py")

def open_potenciais_raizes():
    os.system("caminho_para_o_arquivo_potenciais_raizes.py")

def open_topografia():
    os.system("caminho_para_o_arquivo_topografia.py")

def open_transformada_fourier():
    os.system("caminho_para_o_arquivo_transformada_fourier.py")

# Botões para cada funcionalidade
btn_calculos_estruturais = ttk.Button(app, text="Cálculos Estruturais", command=open_calculos_estruturais)
btn_calculos_estruturais.pack()

btn_derivadas_numericas = ttk.Button(app, text="Derivadas Numéricas", command=open_derivadas_numericas)
btn_derivadas_numericas.pack()

btn_divisao_interface = ttk.Button(app, text="Divisão Interface", command=open_divisao_interface)
btn_divisao_interface.pack()

btn_funcionalidades_basicas = ttk.Button(app, text="Funcionalidades Básicas", command=open_funcionalidades_basicas)
btn_funcionalidades_basicas.pack()

btn_funcionalidades_memoria = ttk.Button(app, text="Funcionalidades de Memória", command=open_funcionalidades_memoria)
btn_funcionalidades_memoria.pack()

btn_funcoes_avancadas = ttk.Button(app, text="Funções Avançadas", command=open_funcoes_avancadas)
btn_funcoes_avancadas.pack()

btn_funcoes_engenharia_civil = ttk.Button(app, text="Funções de Engenharia Civil", command=open_funcoes_engenharia_civil)
btn_funcoes_engenharia_civil.pack()

btn_funcoes_matematicas = ttk.Button(app, text="Funções Matemáticas", command=open_funcoes_matematicas)
btn_funcoes_matematicas.pack()

btn_hidraulica_e_saneamento = ttk.Button(app, text="Hidráulica e Saneamento", command=open_hidraulica_e_saneamento)
btn_hidraulica_e_saneamento.pack()

btn_integral_numerica = ttk.Button(app, text="Integração Numérica", command=open_integral_numerica)
btn_integral_numerica.pack()

btn_mecanica_dos_solos = ttk.Button(app, text="Mecânica dos Solos", command=open_mecanica_dos_solos)
btn_mecanica_dos_solos.pack()

btn_operacoes_memoria = ttk.Button(app, text="Operações de Memória", command=open_operacoes_memoria)
btn_operacoes_memoria.pack()

btn_potenciais_raizes = ttk.Button(app, text="Potenciais e Raízes", command=open_potenciais_raizes)
btn_potenciais_raizes.pack()

btn_topografia = ttk.Button(app, text="Topografia", command=open_topografia)
btn_topografia.pack()

btn_transformada_fourier = ttk.Button(app, text="Transformada de Fourier", command=open_transformada_fourier)
btn_transformada_fourier.pack()

app.mainloop()
