"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Berg'
# # nome[1] = 'D' #erro
# outra_variavel = nome
# nome =  'João'
# print(nome)
# print(outra_variavel)

lista_a = ['Berg', 'Karla']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'

print(lista_b)

