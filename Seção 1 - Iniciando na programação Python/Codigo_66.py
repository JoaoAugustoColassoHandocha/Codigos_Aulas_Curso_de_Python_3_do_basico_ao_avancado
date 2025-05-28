'''
Gerador de CPFs

'''

import os, re, random

os.system('color 1f')

qtd_cpf = int(input('\nQuantidade de CPFs que deseja gerar: '))

os.system('cls')

print('\n')

for a in range(qtd_cpf):

    while True:
        
        num_nove_cpf = ''
        
        cpf_form = ''
        
        for i in range(9):
            
            num_nove_cpf += str(random.randint(0, 9))

        corrigir_cpf = re.sub(r'[^0-9]', '', num_nove_cpf)
        
        prim_char_ent_cpf_rep = corrigir_cpf == corrigir_cpf[0] * len(cpf_form)
            
        try:
                
            nove_digitos = corrigir_cpf[:9]
            contador_regressivo_1 = 10
            resultado_1 = 0
                
            for digito in nove_digitos:
                    
                resultado_1 += int(digito) * contador_regressivo_1
                contador_regressivo_1 -= 1
                
            digito_1 = (resultado_1 * 10) % 11
                
            digito_1 = digito_1 if digito_1 <= 9 else 0
                
            dez_digitos = corrigir_cpf[:10]
            contador_regressivo_2 = 11
            resultado_2 = 0
                
            for digito in dez_digitos:
                    
                resultado_2 += int(digito) * contador_regressivo_2
                contador_regressivo_2 -= 1
                    
            digito_2 = (resultado_2 * 10) % 11
                
            digito_2 = digito_2 if digito_2 <= 9 else 0
                
            cpf_form = num_nove_cpf + str(digito_1) + str(digito_2)          
                
            if str(digito_1) == cpf_form[9] and str(digito_2) == cpf_form[10]:
                    
                print(f'O CPF {cpf_form} é verdadeiro!')
                break
                
            elif str(digito_1) != cpf_form[9] or str(digito_2)!= cpf_form[10]:
                    
                print(f'O CPF {cpf_form} é falso!')
                break
                
            else:
                    
                print('Erro!!! Favor entrar em contato com o suporte!')
                break
                
        except ValueError:
                
            print('CPF inválido!')
            os.system('pause')
            os.system('cls')
            
print('\n')
os.system('pause')
os.system('cls')