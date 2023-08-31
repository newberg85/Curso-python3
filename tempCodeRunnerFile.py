num = input('Digite um número:')

try:
    numero_inteiro = float(num)

    impar_par = numero_inteiro % 2 == 0
    par_impar_texto = 'ímpar'

    if impar_par:
        par_impar_texto = 'par'

    print(f'O número {numero_inteiro} é {par_impar_texto}')
except:
    print('Isso não é um número inteiro')