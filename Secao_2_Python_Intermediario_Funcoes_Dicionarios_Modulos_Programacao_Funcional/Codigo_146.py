'''
Criando arquivos com Python + Context Manager with

* Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)

* Modos: 

> r (leitura)
> w (escrita)
> x (para criação)
> a (escreve ao final)
> b (binário)
> t (modo texto)
> + (leitura e escrita)
> Context manager - with (abre e fecha)

* Métodos úteis:

> write, read (escrever e ler)
> writelines (escrever várias linhas)
> seek (move o cursor)
> readline (ler linha)
> readlines (ler linhas)

* Vamos falar mais sobre o módulo os, mas:

> os.remove ou unlink - apaga o arquivo
> os.rename - troca o nome ou move o arquivo

* Vamos falar mais sobre o módulo json, mas:

> json.dump = Gera um arquivo json
> json.load

'''

# os.remove(caminho_do_arquivo) ou os.unlink(caminho_do_arquivo) - Exclui o arquivo criado

import os

os.system('color 1f')

caminho = 'C:\\Users\\jac0625\\Downloads\\Codigos_Aulas_Curso_de_Python_3_do_basico_ao_avancado\\Secao_2_Python_Intermediario_Funcoes_Dicionarios_Modulos_Programacao_Funcional\\'

caminho += 'arquivo.txt'

print('\nCriado arquivo:')

print('\n******************************\n')

with open(caminho, 'w+') as arquivo:
    
    arquivo.write('Linha 1')
    arquivo.write('\n')
    arquivo.write('Linha 2')
    
    arquivo.writelines(
        
        ('\n','Linha 3', '\n', 'Linha 4' )
        
    )
    
    arquivo.seek(0,0)
    
    print(arquivo.read())

print('\n******************************\n')

os.system('pause')
os.system('cls')

print('\nApagando o arquivo...\n')

os.system('pause')
os.system('cls')

os.remove(caminho)

print('\narquivo.txt apagado\n')

os.system('pause')
os.system('cls')
os.system('exit')