numeros = [5, 2, 8, 1, 9]
print(max(numeros))
print(max(10, 20, 30))

numeros = [32, 25, 1000, 58, 963]
print(max(numeros))

numeros = [96, 35, 259 ,256]
print(min(numeros))

lista = [False, True, False]
print(any(lista))

lista_vazia = []
print(any(lista_vazia))

lista = [True, True, True]
print(all(lista))

lista = [True, False, True]
print(all(lista))

texto = "meu cachorro fez coco no patio"
print(len(texto))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(lista))

dicionario = dict(nome="João", idade=30)
print(dicionario)

dicionario = dict(nome="Tatilaine", idade=20)
print(dicionario)

print(abs(-9))
print(abs(9.15))

print(bin(99459729))
print(bin(10))

def quadrado(número):
    return número ** 2

numeros = [2, 4, 6, 8, 10]
quadrados = map(quadrado, numeros)
print(list(quadrados))

