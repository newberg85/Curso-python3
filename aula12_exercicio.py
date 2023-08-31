nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 17.3:
    print(f'{nome} está abaixo do peso e seu imc é {imc:.2f}')
elif 17.3 <= imc < 25.5:
    print(f'{nome} está com o peso normal e seu imc é {imc:.2f}')
elif 25.5 <= imc < 29.7:
    print(f'{nome} está com excesso de peso e seu imc é {imc:.2f}')
else:
    print(f'{nome} está obeso e seu imc é {imc:.2f}')

#obs:f-strings são strings com a letra f no início e chaves {} para realizar a interpolação de expressões.