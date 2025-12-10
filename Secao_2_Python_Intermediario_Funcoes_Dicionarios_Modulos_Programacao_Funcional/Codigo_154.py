'''
Positional-Only Parameters (/) e Keyword-Only Arguments (*)

*args (ilimitado de argumentos posicionais)
**kwargs (ilimitado de argumentos nomeados)

🟢 Positional-only Parameters (/) - Tudo antes da barra deve ser ❗️APENAS❗️ posicional.

PEP 570 – Python Positional-Only Parameters: https://peps.python.org/pep-0570/

🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.

PEP 3102 – Keyword-Only Arguments: https://peps.python.org/pep-3102/

'''

import os

def soma(x, y, /, *, z):
    
    print(x + y + z)
    
print('\n******************************\n')

soma(1, 2, z = 3)

print('\n******************************\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')