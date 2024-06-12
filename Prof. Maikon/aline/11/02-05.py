import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Funções matemáticas básicas
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

def potenciacao(base, expoente):
    return base ** expoente

def raiz_quadrada(numero):
    if numero < 0:
        messagebox.showerror("Erro", "Raiz quadrada de número negativo!")
        return None
    else:
        return math.sqrt(numero)

def raiz_n_esima(numero, indice):
    if numero < 0 and indice % 2 == 0:
        messagebox.showerror("Erro", "Raiz n-ésima complexa!")
        return None
    else:
        return numero ** (1 / indice)

# Funções de memória
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

# Interface gráfica principal
app = Tk()
app.title("Calculadora Avançada")

# Criando abas para diferentes funcionalidades
abas = ttk.Notebook(app)
aba_basica = ttk.Frame(abas)
aba_avancada = ttk.Frame(abas)
aba_memoria = ttk.Frame(abas)
abas.add(aba_basica, text="Básica")
abas.add(aba_avancada, text="Avançada")
abas.add(aba_memoria, text="Memória")
abas.pack(expand=True, fill="both")

# Funcionalidades básicas (soma, subtração, multiplicação, divisão)
def soma_interface():
    try:
        a = float(entrada_a_soma.get())
        b = float(entrada_b_soma.get())
        resultado = soma(a, b)
        label_resultado_soma.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

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

# ... (implementar interfaces para as outras funções básicas: subtração, multiplicação, divisão)

# Funções avançadas (integração, derivada, transformada de Fourier)
# Implemente conforme necessário

# Funções de memória (adicionar, remover, consultar, limpar)
# Implemente conforme necessário

# Funções de Engenharia Civil (momento fletor, cortante, etc.)
# Implemente conforme necessário

app.mainloop()
