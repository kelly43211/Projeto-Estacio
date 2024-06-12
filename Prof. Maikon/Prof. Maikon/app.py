import os
import tkinter as tk

from op import operacoes_basicas, potenciacao_radiciacao, funcoes_matematicas, memoria, integracao_derivacao
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Função para exibir a tela de splash
def show_splash():
    splash_root = tk.Toplevel(root)
    splash_root.overrideredirect(True)  # Remove a barra de título da janela

    # Obtém o caminho absoluto do diretório atual
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Carrega o ícone a partir do arquivo de imagem
    icon_path = os.path.join(current_dir, "engineering_icon.png")
    icon = ImageTk.PhotoImage(Image.open(icon_path))
    icon_label = tk.Label(splash_root, image=icon)
    icon_label.image = icon
    icon_label.pack(pady=100)

    # Define um atraso antes de fechar a tela de splash
    splash_root.after(5000, splash_root.destroy)

root = tk.Tk()
root.title("Calculadora de Engenharia")

# Obtém o caminho absoluto do diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Carrega o ícone a partir do arquivo de imagem
icon_path = os.path.join(current_dir, "engineering_icon.png")
icon = ImageTk.PhotoImage(Image.open(icon_path))
root.iconphoto(False, icon)

# Configura o estilo dos botões
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=10)

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Cria a tela inicial com botões para selecionar a função
inicio_frame = ttk.Frame(notebook)
notebook.add(inicio_frame, text='Início')

btn_operacoes_basicas = ttk.Button(inicio_frame, text="Operações Básicas", command=lambda: operacoes_basicas.OperacoesBasicasGUI(root))
btn_operacoes_basicas.pack(pady=10)

btn_potenciacao_radiciacao = ttk.Button(inicio_frame, text="Potenciação e Radiciação", command=lambda: potenciacao_radiciacao.PotenciacaoRadiciacaoGUI(root))
btn_potenciacao_radiciacao.pack(pady=10)

btn_funcoes_matematicas = ttk.Button(inicio_frame, text="Funções Matemáticas", command=lambda: funcoes_matematicas.FuncoesMatematicasGUI(root))
btn_funcoes_matematicas.pack(pady=10)

btn_memoria = ttk.Button(inicio_frame, text="Operações com Memória", command=lambda: memoria.MemoriaGUI(root))
btn_memoria.pack(pady=10)

btn_integracao_derivacao = ttk.Button(inicio_frame, text="Integração e Derivação", command=lambda: integracao_derivacao.IntegracaoDerivacaoGUI(root))
btn_integracao_derivacao.pack(pady=10)

# Exibe a tela de splash antes da janela principal
show_splash()

root.mainloop()