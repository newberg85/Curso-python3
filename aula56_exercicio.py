"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

print('Lista de compras')

lista_de_compras = []

while True:
    print('O que dejesa fazer?')
    opcao = input('[i]Inserir, [a]Apagar, [l]Listar: ')

    if opcao == 'i':
        os.system('cls')
        item = input('Item:')
        quantidade = input('Quantidade: ')
        lista_de_compras.append(item)
    elif opcao == 'a':
        indice_str = input('Escolha qual item quer apagar: ')
        
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista_de_compras) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista_de_compras, start=1):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')

