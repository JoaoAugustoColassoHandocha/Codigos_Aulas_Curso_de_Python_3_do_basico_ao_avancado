lazy import os

def soma(x: float, y: float) ->float:
    
    return x + y

def main() -> None:
    
    print(soma(10, 20))
    print(soma(20,20))  

if __name__ == '__main__':
    
    print('\n------------------------------\n')

    main()
    
    print('\n------------------------------\n')

    input('Clique em qualquer tecla para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')