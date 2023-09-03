"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# texto = iter('Berg') # __iter__()

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

texto = 'Berg'  #iterável
# iterador = iter(texto) #iterador 

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)