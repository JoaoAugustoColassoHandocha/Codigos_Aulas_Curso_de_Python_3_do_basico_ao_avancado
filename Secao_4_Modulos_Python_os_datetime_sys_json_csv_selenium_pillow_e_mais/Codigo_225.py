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
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
    
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes com a base (1000 por padrão), isso deve bater com o nosso índice na abreviação dos tamanhos.
    
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    
    # Por quanto nosso tamanho deve ser dividido para gerar o tamanho correto.
    
    potencia = base ** indice_abreviacao_tamanhos
    
    # Nosso tamanho final
    
    tamanho_final = tamanho_em_bytes / potencia
    
    # A abreviação que queremos
    
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

caminho = os.path.join('C:\\Temp', 'Desktop')
counter = count()

print('\n------------------------------\n')

for root, dirs, files in os.walk(caminho):
    
    the_counter = next(counter)
    
    print()
    print(the_counter, 'Pasta atual:', root)
    
    for dir_ in dirs:
        
        print('     |_____', the_counter, 'Diretório:', dir_)
        
    for file_ in files:
        
        caminho_completo_arquivo = os.path.join(root, file_)
        print('     |_____', the_counter, 'Arquivo:', caminho_completo_arquivo)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')