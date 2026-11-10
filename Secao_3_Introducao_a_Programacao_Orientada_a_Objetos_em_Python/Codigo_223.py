'''
Update Codigo_223.py

os.listdir para navegar em caminhos

/Users/luizotavio/Desktop/EXEMPLO

C:'\'Users'\'luizotavio'\'Desktop'\'EXEMPLO

caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'

'''

lazy import os, locale

locale.setlocale(locale.LC_ALL, '') # locale.setlocale(locale.LC_ALL, 'pt_BR.utf8') 

caminho = os.path.join('C:\\Users\\sd.joao.handocha', 'OneDrive - Ministério Público do Trabalho\Documentos\Codigos_Aulas_Curso_de_Python_3_do_basico_ao_avancado\Secao_3_Introducao_a_Programacao_Orientada_a_Objetos_em_Python')

print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')