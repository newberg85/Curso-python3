# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

'''

entrada = input('[E]Entrar [S]Sair: ')
senha_digitada = input('Digite sua senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou')
elif entrada == 'S':
    print('saiu')

'''

#avaliação de curto circuito
print(True and False and True)