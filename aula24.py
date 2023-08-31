"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Berg'
preco = 1000.95896473
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %06x' % (15, 15))