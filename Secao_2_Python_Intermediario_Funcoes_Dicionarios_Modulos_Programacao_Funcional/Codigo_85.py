'''
Sets - Conjuntos em Python (tipo set)

Conjuntos são ensinados na matemática

https://brasilescola.uol.com.br/matematica/conjunto.htm

Representados graficamente pelo diagrama de Venn

Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

Criando um set
set(interável) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados de iteráveis.

- Não aceitam valores mutáveis;
- Seus valores serão sempre únicos;
- Não tem índexes;
- Não garantem ordem;
- São iteráveis (for, in, not in)

Métodos úteis: add, update, clear, discard

Operadores úteis: 
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos

'''

import os

os.system('color 1f')

s1 = set() # set vazio
s2 = set('Teste') # com dados
s3 = {'João', 1, 2, 3} # com dados em outro formato

print(f'\n{s1}')
print(f'{s2}')
print(f'{s3}\n')

os.system('pause')
os.system('cls')