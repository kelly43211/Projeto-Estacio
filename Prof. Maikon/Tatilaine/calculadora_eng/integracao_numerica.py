# Funções para integração numérica
def integral_numerica(funcao_str, a, b, n):
    try:
        # Converter a função string em função Python
        funcao = eval(funcao_str)
        resultado = "integrate".quad(funcao, a, b, epsabs=1e-5, reltol=1e-9, maxfun=n)[0]
        return resultado
    except Exception as e:
        "messagebox.showerror"("Erro", f"Erro ao avaliar a função: {e}")
        return None
    


     # Funcionalidades avançadas (integração, derivada, transformada de Fourier)
    def integracao_numerica(funcao, a, b, n):

        """
    Calcula a integral numérica de uma função utilizando o método do trapézio.

    Parâmetros:
        - funcao: uma função que aceita um único argumento.
        - a, b: os limites inferior e superior da integração.
        - n: o número de subintervalos para dividir o intervalo [a, b].

    Retorna:
        - O valor aproximado da integral numérica.
    """
    h = (b - a) / n
    soma = (funcao(a) + funcao(b)) / 2
    for i in range(1, n):
        soma += funcao(a + i * h)
    return h * soma
    try:
            # Obtendo os valores dos campos de entrada
            funcao_str = entrada_funcao.get()
            a = float(entrada_limite_a.get())
            b = float(entrada_limite_b.get())
            n = int(entrada_pontos.get())
            
            # Verificando se a função de entrada é válida
            def funcao(x):
                return eval(funcao_str, {'x': x, 'math': math})
            
            # Calculando a integral numérica
            resultado = integral_numerica(funcao, a, b, n)
            
            # Atualizando o rótulo com o resultado da integração
            label_resultado_integracao.config(text=f"Resultado: {resultado:.4f}")
    except Exception as e:
            messagebox.showerror("Erro", f"Erro ao integrar: {e}")
            

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
        try:
            # Obtendo os valores dos campos de entrada
            funcao_str = entrada_funcao_derivada.get()
            x = float(entrada_valor_x.get())
            h = float(entrada_passo.get())
            
            # Verificando se a função de entrada é válida
            def funcao(x):
                return eval(funcao_str, {'x': x, 'math': math})
            
            # Calculando a derivada numérica
            resultado = derivada_numerica(funcao, x, h)
            
            # Atualizando o rótulo com o resultado da derivada numérica
            label_resultado_derivada.config(text=f"Derivada: {resultado:.4f}")
        except ValueError:
            messagebox.showerror("Erro", "Certifique-se de que todos os campos foram preenchidos corretamente com valores numéricos.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular a derivada: {e}")

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
        try:
            # Obtendo o sinal a partir do campo de entrada
            sinal_str = entrada_sinal.get()
            
            # Avaliando o sinal para obter a lista de valores
            sinal = eval(sinal_str)
            
            # Calculando a transformada de Fourier do sinal
            fourier = np.fft.fft(sinal)
            
            # Plotando o gráfico da magnitude da transformada de Fourier
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