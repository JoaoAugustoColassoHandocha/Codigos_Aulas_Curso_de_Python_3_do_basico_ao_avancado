'''
Métodos úteis dos dicionários em Python

len - quantas chaves
keys - iterável com as chaves
values - iteráveç com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro

'''

import os, copy

os.system('color 1f')

pessoa = {
    
    'nome': 'João Augusto',
    'idade': 27,
    
}

print('\n')

# Quantidade de chaves
print(len(pessoa))

# Lista os nomes das chaves (Pode ser transformada como list ou tuple) (Pode utilizar também o for de duas formas para conseguiur o nome das chaves)
print(pessoa.keys())
print(tuple(pessoa.keys()))
print(list(pessoa.keys()))

print('\n')
for chave in pessoa.keys():
    print(chave)    
print('\n')


for chave in pessoa:
    print(chave)    
print('\n')

# Lista os valores(resultados) das chaves (Pode ser transformada como list ou tuple) (Pode utilizar também o for para conseguiur os dados das chaves)
print(pessoa.values())
print(list(pessoa.values()))
print(tuple(pessoa.values()))
 
print('\n')
for valor in pessoa.values():
    print(valor)
print('\n')

# Lista as chaves e os valores (Pode ser transformada como list ou tuple) (Pode utilizar também o for para conseguiur as chaves com os valores)
print(pessoa.items())
print(list(pessoa.items()))
print(tuple(pessoa.items()))

print('\n')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')    
print('\n')

# Repassa a informação de uma chave não criada onde utilizará outro valor a partir do momento que é criada
pessoa.setdefault('peso', 'Erro na informação peso')
print(pessoa['peso'])

# Realiza uma cópia rasa do dicionário, onde qualquer mudança nessa cópia (caso não seja feito o .copy()), afeta também o dicionários original (Como no exemplo, o d2 está apontando que é o mesmo dicionário do d1) (Para valores mutáveis, como exemplo uma lista, ele não realiza a cópia, e sim fiquem sinconizados entre eles)
# Para realizar uma cópia mais profunda, visando os valores mutáveis não serem sincronizados, insira import copy, e posteriormente insira o comando como copy.deepcopy()
d1 = {
    
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],    
    
}

d2 = d1

d2['c1'] = 1000
print(d1)

d2 = d1.copy()
d2['c1'] = 100
d2['l1'][1] = 999
print(d1)
print(d2)
d2['l1'][1] = 1

print('-------------')

d2 = copy.deepcopy(d1)
d2['c1'] = 100
d2['l1'][1] = 999
print(d1)
print(d2)

# Retorna um valor None ou o valor da chave, sendo possível repassar um valor padrão
p1 = {
    
    'nome': 'João',
    'sobrenome': 'Augusto',
    
}

print(p1.get('nome', 'Nome não foi encontrado'))
print(p1.get('sobrenome', 'Sobrenome não encontrado'))

# Apaga um item de uma chave específica no dicionário
nome = p1.pop('nome')
print(nome)
print(p1)
p1['nome'] = 'João'

# Apaga a última chave adcionada
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)
p1['sobrenome'] = 'Augusto'

# Modifica e atualiza o dicionário (Pode ser programado de 4 formas)
p1.update({
    
    'nome': 'JOAO',
    'sobrenome': 'AUGUSTO',  
    
})

################

p1.update(idade = 27)

################

tupla = (('peso', 97), ('altura', 1.80))
p1.update(tupla)

################

lista = [['cep', 11111111], ['genero', 'MASCULINO']]
p1.update(lista)

################

print(p1)

print('\n')

os.system('pause')
os.system('cls')