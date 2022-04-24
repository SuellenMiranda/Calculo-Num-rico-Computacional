print("Atividade avaliativa - Cálculo Numérico Computacional Parte 1")

vetNum = []  # vetor inicial sem posições definidas
cont = 0  # variável contadora já inicializada

while cont <= 3:  #função WHILE utilizada para tratamento de erro
    try:
        vetNum.append(
            float(input("\nDigite um número real: "))
        )  # Valores informados pelo usuário. Conversão dos valores do input para tipo float.
        cont += 1
    except ValueError:
        print("\nValor informado não é um número real. Tente novamente!")

somaNum1 = sum(vetNum)  # somar todos os elementos do vetor
print("\nos valores informados foram: ", vetNum)
print("\na soma dos valores informados é: ", somaNum1)

revNum = list(
    reversed(vetNum))  # reverter a ordens dos elementos do vetor vetNum
somaNum2 = sum(revNum)
print("\nos valores informados reversos foram: ", revNum)
print("\na soma dos valores reversos informados é: ", somaNum2)

if (somaNum1 == somaNum2
    ):  # compara se os valores são iguais e retorna o resultado
    print("\nos valores informados são identicos!")
else:
    print("\nos valores informados são diferentes!")

#ex de numeros para somar: 0.1+0.2+0.3+0.4=0.999999999....
