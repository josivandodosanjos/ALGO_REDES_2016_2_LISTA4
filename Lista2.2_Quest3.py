

maior = 0

salarios = [

    [float(input("Digite seu salário: ")), float(input("Digite seu salário: ")), float(input("Digite seu salário: "))],
    [float(input("Digite seu salário: ")), float(input("Digite seu salário: ")), float(input("Digite seu salário: "))],
    [float(input("Digite seu salário: ")), float(input("Digite seu salário: ")), float(input("Digite seu salário: "))]

        ]

menor = salarios[0][0]

for linhas in salarios:
    for num in linhas:

        if num > maior:
            maior = num

        elif num < menor:
            menor = num

print("Maior salário: ", maior)
print("Menor salário: ", menor)