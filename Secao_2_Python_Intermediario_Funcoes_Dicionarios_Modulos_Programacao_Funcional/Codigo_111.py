'''
Modularização - Entendendo os seus próprios módulos Python

* O primeiro módulo executado chama-se __main__

* Você pode importar outro módulo inteiro ou parte do módulo

* O python conhece a pasta onde o __main__ está e as pastas abaixo dele.

* Ele não reconhece pastas e módulos acima do __main__ por padrão

* O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

'''
try:
    
    import os, sys
    
    sys.path.append('')
    
except ModuleNotFoundError:
    
    print('Erro!')
    
import Codigo_111_Modulo

os.system('color 1f')

print('\n******************************\n')

print(f'Esse módulo se chama {__name__}')

print('\n******************************\n')

print(*sys.path, sep = '\n')

print('\n******************************\n')

os.system('pause')
os.system('cls')