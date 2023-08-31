# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

# nome_completo = "Wandemberg de Meneses viana"
# print(nome_completo)
# idade = 18;
# print(nome_completo, idade, "anos")

# nome = 'Berg'
# idade = 18
# maior_de_idade = idade >= 18
# print('Nome:', nome, 'Idade:', idade, )
# print('É maior?', maior_de_idade)

nome = input('Digite seu nome?')
idade = int(input('Qual a sua idade?'))

if idade < 18:
    print(nome,'tem', idade, 'anos', 'e ele é menor de idade.')
else:
    print(nome,'tem', idade, 'anos', 'e ele é maior de idade.')