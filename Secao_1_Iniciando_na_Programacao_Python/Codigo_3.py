#sep - separador
# \r \n - quebra de linha -> CRLF
# \n - quebra de linha -> LF
# end - final do print

print(12, 34, sep=' ', end='\r\n')
print(56, 78, sep='-', end='\n')
print(90, 12, sep='=', end='!!')
print(34, 56, sep='+', end='##\n')
print(78, 90, sep='/', end='\n||')