# coding=utf-8

# Faça um programa que leia a idade de uma pessoa expressa em dias e
# mostre-a expressa em anos, meses e dias.

numDias = int(input("Digite o numero de dias: "))

anos = numDias // 365

meses = (numDias - anos *365) // 30

dias = (numDias - anos *365 - meses *30)

print ("{} Dias convertido é: \n {} Anos, {} Meses e {} Dias".format(numDias, anos, meses, dias))