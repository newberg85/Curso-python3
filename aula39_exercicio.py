''' Calculadora com while'''

print(11 * '=')
print('Calculadora')
print(11 * '=')

while True:
    print("Opções")
    print("Soma || Subtração || Divisão || Multiplicação")
    opcao = input('Escolha uma operação: ')
    # .lower transforma as letras em minusculas

    try:
        num1 = int(input('Digite um número:'))
        num2 = int(input('Digite outro número:'))

        if opcao == 'Soma' or opcao == 'soma':
            soma = num1 + num2
            print(f'a soma de {num1} + {num2} é {soma}')
        elif opcao == 'Subtração' or opcao == 'subtração':
            subtracao = num1 - num2
            print(f'a subtração de {num1} - {num2} é {subtracao}')
        elif opcao == 'Divisão' or opcao == 'divisão':
            divisao = num1 / num2
            print(f'a Divisão de {num1} / {num2} é {divisao}')
        elif opcao == 'Multiplicação' or opcao == 'multiplicação':
            multiplicacao = num1 * num2  
            print(f'a multiplicação de {num1} * {num2} é {multiplicacao}')
        else:
            print("Operação não reconhecida. Por favor, escolha uma operação válida.")
    except:
        print('números invalidos')
    
    sair = input('Você deseja sair? ')
    if sair == 'Sim' or sair == 'sim':
        break
    elif sair == 'Não'or sair == 'não':
        continue

    
