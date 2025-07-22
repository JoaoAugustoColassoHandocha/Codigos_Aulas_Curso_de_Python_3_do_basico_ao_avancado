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

s1 = set()
s1.add('João') # Adiciona um valor no set (Não aceita mais de um valor para adicionar)
s1.update('Olá mundo') # Muito parecido com o add, mas deforma valores interados
s1.update(('Augusto', 1, 2, 3)) # Para não deformar e inserir mais informações, pode ser utilizado uma tupla
print(f'\n{s1}\n')

s1.discard()
print(f'{s1}\n')

s1.clear() # Realiza a limpa do set
print(f'{s1}\n')

os.system('pause')
os.system('cls')