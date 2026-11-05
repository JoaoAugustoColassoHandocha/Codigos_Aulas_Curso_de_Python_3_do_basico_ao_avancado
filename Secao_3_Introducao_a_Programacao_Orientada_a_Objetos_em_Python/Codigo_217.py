'''
Update Codigo_217.py

Exercício solucionado: calculando as datas e parcelas de um empréstimo

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


fmt = '%d/%m/%Y'
data_emprestimo_inicio = datetime.strptime('20/12/2020', fmt)

data_inicio_cobranca = (data_emprestimo_inicio + relativedelta(month = 1, year = 1) if data_emprestimo_inicio.month == '12' else data_emprestimo_inicio + relativedelta(month = 1))

print('\n------------------------------\n')



print('\n------------------------------\n')

input('Clique em qualquer tecla para continuar...')
os.system('cls' if os.name == 'nt' else 'clear')