# coding=utf-8
# Implementar uma função que retorne verdadeiro se o número for primo
# (falso caso contrário). Testar de 1 a 100.
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

def primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

lista_Impares = []

for x in range(2, 100):
    if (primo(x)):
        lista_Impares.append(x)

print (lista_Impares)
