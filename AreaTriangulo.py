

valorA = input("Digite o valor de A: ")
valorB = input("Digite o valor de B: ")
valorC = input("Digite o valor de C: ")

if valorA > (valorB + valorC):
    print("Nao e possivel montar um triangulo com esses valores: {}, {}, {}.".format(valorA, valorB, valorC))
else:
    s = (valorA + valorB + valorC) / 2
    area = (s * (s - valorA) * (s - valorB) * (s - valorC)) ** 0.5
    print("a area do triangulo e {:.2f}".format(area))