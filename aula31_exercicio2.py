"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Qual a hora?')

# if hora <= 11:
#     print('Bom dia!!')
# elif 12 >= hora <= 17:
#     print('Boa tarde!!')
# elif 18 >= hora <= 23:
#     print('Boa noite!!')
# else:
#     print('Hora invalida')

try: 
    hora_int = int(hora)

    if hora <= 11:
        print('Bom dia!!')
    elif 12 >= hora <= 17:
        print('Boa tarde!!')
    elif 18 >= hora <= 23:
        print('Boa noite!!')
    else:
        print('Não conheço essa hora')
except:
    print('Digite apenas numeros inteiros :)')