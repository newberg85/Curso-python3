"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
# numero = lista[2]
# print(lista)
# print(lista[2])
# print(numero)

# del lista[1]
# print(lista)

#clear() limpa a lista

# append adiciona um item a uma lista 
lista.append(50)
# pop remove o ultimo elemento de uma lista.
lista.pop()
lista.append(60)
lista.append(70)
lista.insert(0, 5)
lista.insert(0, 5)
ultimo_valor = lista.pop()
print(lista, 'Removido', ultimo_valor)