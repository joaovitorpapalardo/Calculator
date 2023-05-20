import os

while True:

    #Declarando variáveis
    num = (input('Digite um número: '))
    num_2 = (input('Digite outro número: '))
    testando = num.isdigit
    testando_2 = num_2.isdigit

    #Tratando erro de valor
    try:
        num = float(num)
        num_2 = float(num_2)
        print("Proximo passo")
    except ValueError:
        print("Digite apenas números!")
        continue

    operaçao = input('O que deseja fazer? somar"+", subtrair"-", dividir"/", multiplicar"x": ')
    oper = '+-/x'

    #Calculos | Respostas
    if operaçao in oper:
        if operaçao == '+':
            os.system('cls')
            print(f'{num} + {num_2} = {num + num_2}')
        elif operaçao == '-':
            os.system('cls')
            print(f'{num} - {num_2} = {num - num_2}')
        elif operaçao == '/':
            os.system('cls')
            print(f'{num} / {num_2} = {num / num_2}')
        elif operaçao == 'x':
            os.system('cls')
            print(f'{num} x {num_2} = {num * num_2}')
    
    #Continuar ou sair da calculadora
    else:
        print('Operador inválido')
    continuar = (input('Deseja continuar na Calculadora? Digite "s" para sim, "n" para não: '))
    if continuar == 's':
        os.system('cls')
        continue
    else:
        break