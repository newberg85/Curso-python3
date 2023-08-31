primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print('primeiro_valor =', primeiro_valor, 'é maior do que o segundo_valor =', segundo_valor)
elif primeiro_valor == segundo_valor:
    print('Os valores são iguais')
else:
    print('segundo_valor =', segundo_valor, 'é maior do que o primeiro_valor =', primeiro_valor)