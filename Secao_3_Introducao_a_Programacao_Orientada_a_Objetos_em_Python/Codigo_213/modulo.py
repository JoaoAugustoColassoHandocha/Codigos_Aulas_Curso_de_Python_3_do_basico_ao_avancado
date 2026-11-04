lazy import os

def soma(x: float, y: float) ->float:
    
    return x + y

if __name__ == '__main__':
    
    print('\n------------------------------\n')

    print(soma(10, 20))
    print(soma(20,20))    

    print('\n------------------------------\n')

    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')