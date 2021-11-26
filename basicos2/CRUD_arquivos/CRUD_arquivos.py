#https://docs.python.org/3/library/functions.html#open

# file = open('teste.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
# file.write('Linha 4\n')
# file.write('Linha 5\n')

# #Volta o cursor ao topo do arquivo
# file.seek(0,0)
# print('Lendo linhas: ')
# print(file.read())
# file.seek(0,0)

# print(file.readline(), end='')#Mando um end para não quebrar tantas linhas. A função print quebra uma linha por padrão
# print(file.readline(), end='')
# print(file.readline(), end='')

# print('###########################')

# file.seek(0,0)

# for linha in file.readlines():
#     print(linha, end='')


# file.close()


# try:
#     file = open('teste.txt', 'w+')
#     file.write('Linha')
#     file.seek(0,0)
#     print(file.read())

# finally:
#     file.close()



#OU 

with open('teste.txt', 'w+') as file:
    file.write('Linha\n')