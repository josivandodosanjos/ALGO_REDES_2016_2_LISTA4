matriz = [[-7,-3],[4,8],[-1,-6]]

contator_negativos = 0
soma_positivos = 0
contador_impares = 0
contador_pares = 0

for linhas in matriz:
    for numero in linhas:
        if numero < 0:
            contator_negativos = contator_negativos + 1

        else:
            soma_positivos = soma_positivos + numero

        if numero % 2 == 0:
            contador_pares = contador_pares + 1

        else:
            contador_impares = contador_impares + 1

print("Quantidade de Números negativos: ", contator_negativos)
print("Soma dos positivos: ", soma_positivos)
print("Quantidade de Números pares: ", contador_pares)
print("Quantidade de Números impares: ", contador_impares)