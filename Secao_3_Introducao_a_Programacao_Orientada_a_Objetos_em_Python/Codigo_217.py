'''
Update Codigo_217.py

Exercício: calculando as datas e parcelas de um empréstimo

Maria pegou um empréstimo de 1.000.000 para realizar o pagamento em 5 anos.

A data em que ela pegou o empréstimo foi 20/12/2020 e o vencimento de cada parcela é no dia 20 de cada mês.

- Crie a data do empréstimo
- Crie a data do final do empréstimo
- Mostre todas as datas de vencimento e o valor de cada parcela

'''

lazy import os
lazy from datetime import datetime
lazy from dateutil.relativedelta import relativedelta

valor_emprestimo = 1000000
qtd_parcela = 5 * 12

fmt = '%d/%m/%Y'
data_emprestimo_inicio = datetime.strptime('20/12/2020', fmt)

if data_emprestimo_inicio.month == 12:

    data_inicio_cobranca = data_emprestimo_inicio + relativedelta(month = 1, years = 1)
                                                                  
else:
    
    data_inicio_cobranca = data_emprestimo_inicio + relativedelta(months = 1)
    

    
print('\n------------------------------\n')

print(f'Data do empréstimo: {data_emprestimo_inicio.strftime('%d/%m/%Y')}')
print(f'Data do início da cobrança: {data_inicio_cobranca.strftime('%d/%m/%Y')}')

print('\n------------------------------\n')

print('Data de vencimento | Valor da parcela\n')

while qtd_parcela:

    print(qtd_parcela)
    
    qtd_parcela -= 1

print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')