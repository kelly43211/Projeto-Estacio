# Funções de Engenharia Civil (implementar botões para acionar funções específicas)
def momento_fletor_interface():
    try:
        forca = float(entrada_forca_mf.get())
        distancia = float(entrada_distancia_mf.get())
        tipo_apoio = entrada_tipo_apoio_mf.get()
        resultado = momento_fletor(forca, distancia, tipo_apoio)
        if resultado is not None:
            label_resultado_mf.config(text=f"Resultado: {resultado:.4f} N.m")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida!")

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
entrada_tipo_apoio_mf.pack

# ... (código anterior para funções de soma, subtração, multiplicação)

# Funções de Engenharia Civil (implementar botões para acionar funções específicas)
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

# ... (código para implementar interfaces gráficas de outras funções de engenharia civil)

# ... (código restante da interface gráfica)

# ... (código anterior para funções básicas, memória e outras funções de engenharia civil)

# Funções de Engenharia Civil
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

# Funções de Engenharia Civil (implementar de acordo com suas necessidades)
def momento_fletor(forca, distancia, tipo_apoio):
    # ... (implementar a lógica para calcular o momento fletor)

def cortante(forca, distancia, tipo_apoio):
    # ... (implementar a lógica para calcular o cortante)

# ... (implementar outras funções de engenharia civil que você desejar)        