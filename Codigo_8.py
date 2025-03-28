#Variáveis são usadas para salvar algho na memória do computador
#PEP8: incie variáveis com letras minúsculas, pode usar números e underline _.
#O sinal de = é o operador de atribuição. Ele é usado para atribuir um valor a um nome(variável).
#Uso: nome_variavel=experssão

import os

os.system('color 4')

nome_completo = 'João Augusto'
soma_dois = 2 + 2
int_1 = int('1')

print('\n')
print(nome_completo,'-', soma_dois)#Imprime o valor da variável nome_completo e soma_dois
print('\n')
print(int_1,type(int_1))#Imprime o valor da variável int_1 e o tipo dela
print('\n')

os.system('pause')
os.system('cls')

#Exemplo

nome = 'João'
idade = 26
maior_de_idade = idade >= 18

print('Nome:', nome)
print('Idade:', idade)

if maior_de_idade == True:
    
    print('\n')
    print(nome, 'tem', idade, 'anos e é maior de idade!')
    print('\n')
    
else:
    
    print('\n')
    print(nome, 'tem', idade, 'anos e não é maior de idade!')
    print('\n')
    
os.system('pause')
os.system('cls')