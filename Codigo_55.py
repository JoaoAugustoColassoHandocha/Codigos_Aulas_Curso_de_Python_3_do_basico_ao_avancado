'''
EXERCÍCIO

Faça uma lista de compras com listas

O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista

Não permita que o programa quebre com erros de índices inexistentes na lista.

'''

import os, getpass

os.system('color 1f')

try:
    
    def main():

        print('\n' + '-' * 5 + 'LISTA DE COMPRA' + '-' * 5 + '\n')
        print('[A] - Acessar o sistema')
        print('[S] - Sair')
        print('\n' + '-' * 25 + '\n')
            
        op = input('Escolha uma opção: ')
            
        os.system('cls')
            
        if op == '' or op == ' ':
            
            print('\nFavor repassar a opção desejada!!!\n')
            os.system('pause')
            os.system('cls')
            main()
        
        elif op.upper() == 'A':
            
            senha = getpass.getpass('\nFavor repassar a senha de acesso: ')
            
            os.system('cls')
            
            while True:
            
                if senha == 'AcessoLista':
                    
                    lista_compra()
                    break
                
                elif senha == '' or senha == ' ':
                    
                    print('\nFavor repassar a senha solicitada!!!\n')
                    os.system('pause')
                    os.system('cls')
                    main()
                    break
                
                elif senha != 'AcessoLista':
                    
                    print('\nSENHA ERRADA!!!')
                    print('\nFavor inserir senha correta!\n')
                    os.system('pause')
                    os.system('cls')
                    main()
                    break
                
                else: 
                    
                    print('\nERRO!!!')
                    print('\nFavor entrar em contato com o suporte do sistema.')
                    os.system('pause')
                    os.system('cls')
                    main()
                    break   
                                        
        elif op.upper() == 'S':
            
            print('\nSaindo...\n')
            os.system('pause')
            os.system('cls')
            
        elif op.upper() != 'A' or op.upper() != 'S':
            
            print('\nOPÇÃO ERRADA!!!')
            print('\nFavor inserir opção certa.\n')
            os.system('pause')
            os.system('cls')
            main()
            
        else:
            
            print('\nERRO!!!')
            print('\nFavor entrar em contato com o suporte do sistema.')
            os.system('pause')
            os.system('cls')
            
    def lista_compra():
        
        lista = []
        
        while True:
            
            print('\n' + '-' * 25 + '\n')
            print('[1] - Adicionar produto')
            print('[2] - Mostrar lista')
            print('[3] - Apagar produto')
            print('[4] - Retornar ao menu')
            print('\n' + '-' * 25 + '\n')
            
            opcao = input('Escolha uma opção: ')
            
            os.system('cls')

            if opcao == '' or opcao == ' ':
            
                print('\nFavor repassar a opção desejada!!!\n')
                
                os.system('pause')
                os.system('cls')
            
            elif opcao == '1':
                
                ad_prod = input('\nProduto: ')
                lista.append(ad_prod)
                
                os.system('cls')
            
            elif opcao == '2':
                
                print('\nÍndice | Produto')
                print('----------------')
                
                for indice, prod in enumerate(lista):

                    print(f'   {indice}   | {prod}')
                
                print('----------------\n')
                
                os.system('pause')
                os.system('cls')
                
            elif opcao == '3':
                
                ap_prod = input('\nÍndice do produto: ')
                
                os.system('cls')
                                  
                try:
                    
                    ap_prod_int = int(ap_prod)
                    del lista[ap_prod_int]
                    os.system('cls')
            
                except IndexError:
                            
                    print('\nÍNDICE ERRADO!!!')
                    print('\nFavor inserir índice certo.\n')
                    os.system('pause')
                    os.system('cls')
                    
                except ValueError:
                    
                    print('\nÍNDICE ERRADO!!!')
                    print('\nFavor inserir número para índice.\n')
                    os.system('pause')
                    os.system('cls')
                    
                
                except Exception:
                    
                    print('\nErro Desconhecido.')
                    print('\nFavor entrar em contato com o suporte do sistema.\n')
                    os.system('pause')
                    os.system('cls')
                                  
                except:
                            
                    print('\nERRO!!!')
                    print('\nNão foi possível repassar os dados para o sistema.\n')
                    os.system('pause')
                    os.system('cls')
                                                                
            elif opcao == '4':
                
                main()
                break
            
            elif opcao != '1' or opcao != '2' or opcao != '3' or opcao != '4':
            
                print('\nOPÇÃO ERRADA!!!')
                print('\nFavor inserir opção certa.\n')
                os.system('pause')
                os.system('cls')
            
            else:
                
                print('\nERRO!!!')
                print('\nFavor entrar em contato com o suporte do sistema.\n')
                os.system('pause')
                os.system('cls')
                os.system('exit')
                break
        
except:
    
    print('\nERRO!!!')
    print('\nFavor entrar em contato com o suporte do sistema.\n')
    os.system('pause')
    os.system('cls')
        
main()