#Conversão de tipos, coerção
#Type convertion, typecastasting, coercion
#É o ato de converter um tipo em outro
#Tipos imutáveis e primivos: str, int, float, bool

print(1+1) #Python entendeu que 1 e 1 são números inteiros e fez a soma

print('a'+'b')#Python entendeu que 'a' e 'b' são strings e fez a concatenação

print('1', type('1'))#Python entendeu que '1' é uma string e imprimiu o tipo dela

print(int('1') + 1) #Python converteu a string '1' em um número inteiro e fez a soma

print(float('1') + 1) #Python converteu o número inteiro 1 em um número float e fez a soma

print(bool('1')) #Python converteu a string '1' em um booleano e imprimiu True

print(bool('')) #Python converteu a string vazia em um booleano e imprimiu False

print(str(1 + 1)) #Python converteu o número inteiro 2 em uma string e imprimiu '2'

print(str(1)+'A') #Python converteu o número inteiro 1 em uma string e imprimiu '1A'

Aluno = 'João'

print(str(1)+'-'+Aluno) #Python converteu o número inteiro 1 em uma string e imprimiu '1-João'

import os

os.system('pause')