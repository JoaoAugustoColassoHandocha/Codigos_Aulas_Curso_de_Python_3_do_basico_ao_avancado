'''
Update Codigo_223.py

os.listdir para navegar em caminhos

/Users/luizotavio/Desktop/EXEMPLO

C:'\'Users'\'luizotavio'\'Desktop'\'EXEMPLO

caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

'''

lazy import os, locale

locale.setlocale(locale.LC_ALL, '') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

caminho = os.path.join('C:\\Users\\sd.joao.handocha', 'OneDrive - Ministério Público do Trabalho', 'Documentos', 'Codigos_Aulas_Curso_de_Python_3_do_basico_ao_avancado')

print('\n------------------------------')

for pasta in os.listdir(caminho):
    
    print(f'\n{pasta}\n')
    
    caminho_completo_pasta = os.path.join(caminho, pasta)
    
    if not os.path.isdir(caminho_completo_pasta):
        
        continue
    
    for item in os.listdir(caminho_completo_pasta):
    
        print('     ', item)

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')