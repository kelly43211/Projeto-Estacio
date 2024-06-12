import tkinter as tk
from tkinter import messagebox
import math

def append_to_expression(symbol):
    expression_field.insert(tk.END, symbol)

def calculate():
    try:
        result = eval(expression_field.get())
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida")

def clear():
    expression_field.delete(0, tk.END)

def sqrt():
    try:
        result = math.sqrt(float(expression_field.get()))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def log():
    try:
        result = math.log10(float(expression_field.get()))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def sin():
    try:
        result = math.sin(math.radians(float(expression_field.get())))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def cos():
    try:
        result = math.cos(math.radians(float(expression_field.get())))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

def tan():
    try:
        result = math.tan(math.radians(float(expression_field.get())))
        expression_field.delete(0, tk.END)
        expression_field.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Criação da janela principal
root = tk.Tk()
root.title("Calculadora")

# Campo de expressão
expression_field = tk.Entry(root, font=('arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4)
expression_field.grid(row=0, column=0, columnspan=4)

# Criação dos botões
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, command=calculate)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: append_to_expression(t))
    button.grid(row=row, column=col, sticky="nsew")

# Criação dos botões de funções avançadas
advanced_buttons = [
    ('√', sqrt), ('log', log), ('sin', sin), ('cos', cos), ('tan', tan), ('C', clear)
]

for i, (text, func) in enumerate(advanced_buttons):
    button = tk.Button(root, text=text, padx=20, pady=20, command=func)
    button.grid(row=i//2+1, column=4+i%2, sticky="nsew")

# Tornar os botões responsivos
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(6):
    root.grid_columnconfigure(i, weight=1)

# Execução do loop principal da interface
root.mainloop()
