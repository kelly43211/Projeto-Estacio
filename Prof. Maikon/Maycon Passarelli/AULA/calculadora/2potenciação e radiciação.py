import tkinter as tk
from tkinter import messagebox

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal do Tkinter
        messagebox.showerror("Erro", "Divisão por zero!")
        root.destroy()  # Fecha a janela do Tkinter
        return None
    else:
        return a / b
import tkinter as tk
from tkinter import messagebox

def potenciacao(a, n):
    return a ** n

def raiz_quadrada(a):
    if a < 0:
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal do Tkinter
        messagebox.showerror("Erro", "Raiz quadrada de número negativo!")
        root.destroy()  # Fecha a janela do Tkinter
        return None
    else:
        return a ** 0.5

def raiz_n_esima(a, n):
    if a < 0 and n % 2 == 0:
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal do Tkinter
        messagebox.showerror("Erro", "Raiz n-ésima complexa!")
        root.destroy()  # Fecha a janela do Tkinter
        return None
    else:
        return a ** (1 / n)
