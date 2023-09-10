"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
# lista_palavras = frase.split() ['olha', 'só', 'que,']
lista_frases_cruas = frase.split(', ') #['Olha só que', 'coisa interessante!']

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #rstrip - corta os espaços da direita; lstrip - esquerda

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)


