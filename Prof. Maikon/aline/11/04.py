numeros = [5, 2, 8, 1, 9]
print(max(numeros))
print(max(10, 20, 30))
numeros = [10, 16, 18, 21, 25]
print(max(numeros ))
numeros = [98, 35, 10, 1, 65, 5]


lista = [False, True, False]
print(any(lista))

lista_vazia = []
print(any(lista_vazia))

lista = [True, True,True]
print(all(lista))

lista = [True, False, True]
print(all(lista))

texto = "meu cachorro fez coco no patio"
print(len(texto))

lista = [1, 2, 3, 4, 5]
print(len(lista))

dicionario = dict(nome="João", idade=30)
print(dicionario)

dicionario = dict(nome="Aline", idade=22) 
print(dicionario)

print(abs(-3))
print(abs(1.23))

print(bin(2563))
print(bin(20))

def quadrado(numero):
    return numero ** 2

numeros = [1, 3, 5, 7, 9]
quadrados = map(quadrado, numeros)
print(list(quadrados))