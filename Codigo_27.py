'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
    
* Obs: As variáveis que não mudam, são escritas em maiúsculo

'''

import os
from colorama import init, Fore, Style

init()

def main(vel_carro_passou_radar_1, range_carro_radar_1, velocidade, local_carro, RADAR_1, LOCAL_1, RADAR_RANGE):
    
    RADAR_1 = 60 # Velocidade máxima do radar 1
    LOCAL_1 = 100 # Local onde o radar 1 está
    RADAR_RANGE = 1 # A distância onde o radar pega
    
    print(Style.BRIGHT, Fore.BLUE + f'\n{"=" * 10} Sistema Radar {"=" * 10}\n' + Style.RESET_ALL)
    print('[A] - Abrir sistema radar')
    print('[S] - Sair')
    print(Style.BRIGHT, Fore.BLUE + f'\n{'=' * 35}\n'+ Style.RESET_ALL)
    
    opcao = input('Escolha uma opção: ')
    
    os.system('cls')
    
    if opcao == 'A' or opcao == 'a':

        velocidade = int(input(Style.BRIGHT + f'\nQual a velocidade do automóvel: ')) # Velocidade atual do carro
        local_carro = int(input(Style.BRIGHT + f'\nQual o local do automóvel no momento: ')) # Local em que o carro está na estrada

        vel_carro_passou_radar_1 = velocidade > RADAR_1 # Verifica se o carro está acima da velocidade do radar 1
        range_carro_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) # Verifica se o carro está na área de alcance do radar 1
        
        os.system('cls')
        
        verifica_radar(vel_carro_passou_radar_1, range_carro_radar_1, velocidade, RADAR_1)
    
    elif opcao == 'S' or opcao == 's':
        
        print(Style.BRIGHT, Fore.BLUE + f'\nSaindo do sistema radar...\n' + Style.RESET_ALL)
        os.system('pause')
        os.system('cls')
        
    else:
        
        print(Fore.RED, Style.BRIGHT + f'\nOpção inválida!\n' + Style.RESET_ALL)
        os.system('pause')
        os.system('cls')
        main(0, 0, 0, 0, 0, 0, 0)

# Verifica se o carro está na área de alcance do radar e a velocidade é maior que a permitida
def verifica_radar(vel_carro_passou_radar_1, range_carro_radar_1, velocidade, RADAR_1):

    if vel_carro_passou_radar_1 == True:
        
        if range_carro_radar_1 == True:
            
            print(Style.BRIGHT, Fore.RED + f'\nVocê está acima da velocidade permitida!' + Style.RESET_ALL)
            print(f'\nVelocidade máxima permitida: {RADAR_1} km/h')
            print('\nVelocidade atual do veículo:' + Style.BRIGHT, Fore.RED + f'{velocidade} km/h\n' + Style.RESET_ALL)
            os.system('pause')
            os.system('cls')
            main(0, 0, 0, 0, 0, 0, 0)
            
        elif range_carro_radar_1 == False:
            
            print(Style.BRIGHT, Fore.YELLOW + f'\nVocê não se encontra na área de alcance do radar!' + Style.RESET_ALL)
            print(f'\nVelocidade atual do veículo:' + Style.BRIGHT, Fore.YELLOW + f'{velocidade}km/h\n' + Style.RESET_ALL)
            os.system('pause')
            os.system('cls')
            main(0, 0, 0, 0, 0, 0, 0)
            
        else:
            
            print(Style.BRIGHT, Fore.RED + f'\nErro no processamento dos dados!\n' + Style.RESET_ALL)
            os.system('pause')
            os.system('cls')
            main(0, 0, 0, 0, 0, 0, 0)
        
    elif vel_carro_passou_radar_1 == False:
        
        
        if range_carro_radar_1 == True:
            
            print(Style.BRIGHT, Fore.GREEN + f'\nVocê está dentro da velocidade permitida!' + Style.RESET_ALL)
            print(f'\nVelocidade máxima permitida: {RADAR_1} km/h')
            print(f'\nVelocidade atual do veículo:' +  Style.BRIGHT, Fore.GREEN + f'{velocidade}km/h\n' + Style.RESET_ALL)
            os.system('pause')
            os.system('cls')
            main(0, 0, 0, 0, 0, 0, 0)
            
        elif range_carro_radar_1 == False:
            
            print(Style.BRIGHT, Fore.YELLOW + f'\nVocê não se encontra na área de alcance do radar!' + Style.RESET_ALL)
            print(f'\nVelocidade atual do veículo:' + Style.BRIGHT, Fore.YELLOW + f'{velocidade}km/h\n' + Style.RESET_ALL)
            os.system('pause')
            os.system('cls')
            main(0, 0, 0, 0, 0, 0, 0)
            
        else:
            
            print(Style.BRIGHT, Fore.RED + f'\nErro no processamento dos dados!\n' + Style.RESET_ALL)
            os.system('pause')
            os.system('cls')
            main(0, 0, 0, 0, 0, 0, 0)
        
    else:
        
        print(Style.BRIGHT, Fore.RED + f'\nErro no processamento dos dados!\n' + Style.RESET_ALL)
        os.system('pause')
        os.system('cls')
        main(0, 0, 0, 0, 0, 0, 0)
    
main(0, 0, 0, 0, 0, 0, 0)