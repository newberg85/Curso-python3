"""
Iterando strings com while
"""

nome = input('Digite seu nome:')

# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)