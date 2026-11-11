'''
Update Codigo_225.py

os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)

'''

lazy import os, locale, math
lazy from itertools import count

locale.setlocale(locale.LC_ALL, '') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    
    # Formata um tamanho de bytes para o tamanho apropriado
    
    # Original: https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python
    
    # Se o tamanho for menor ou igual a 0, retorna 0 B.
    if tamanho_em_bytes <= 0:
        
        return '0 B'
    
    # Tupla com os tamanhos
    
    

print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')