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

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # Para unir dois sets
s4 = s1 & s2 # Para retornar os itens presentes nos dois sets
s5 = s1 - s2 # Para retornar os itens que estão apenas na esquerda
s6 = s1 ^ s2 # Para retornar os itens que não estão em ambos os sets

os.system('pause')
os.system('cls')