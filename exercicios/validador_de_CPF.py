""""
cpf = 168.995.350-09
-----------------------------------
"""

# novo_cpf = input('Digite o seu número de CPF: ')

# def validador_cpf(novo_cpf):
#     cpf = '303.022.408-29' #Consulta de base de CPFs
#     # Retirando os pontos e - do cpf
#     caracteres = '.-'
    
#     for x in range(len(caracteres)):
#         cpf = cpf.replace(caracteres[x], '')

#     for x in range(len(caracteres)):
#         novo_cpf = novo_cpf.replace(caracteres[x], '')
#     # print(f'CPF da base: {cpf} | novo CPF: {novo_cpf}')


#     #Verificação do primeiro dígito após o "-"
#     primeiro_valor1 = 10 * int(novo_cpf[0])
#     primeiro_valor2 = 9 * int(novo_cpf[1])
#     primeiro_valor3 = 8 * int(novo_cpf[2])
#     primeiro_valor4 = 7 * int(novo_cpf[3])
#     primeiro_valor5 = 6 * int(novo_cpf[4])
#     primeiro_valor6 = 5 * int(novo_cpf[5])
#     primeiro_valor7 = 4 * int(novo_cpf[6])
#     primeiro_valor8 = 3 * int(novo_cpf[7])
#     primeiro_valor9 = 2 * int(novo_cpf[8])

#     primeira_soma_valores = primeiro_valor1 + primeiro_valor2 + primeiro_valor3 + primeiro_valor4 + primeiro_valor5 + primeiro_valor6 + primeiro_valor7 + primeiro_valor8 + primeiro_valor9

#     primeiro_resultado_formula = 11 - (primeira_soma_valores % 11)

#     """
#     Verificando se o primeiro dígito após o "-"
#     será o próprio valor do resultado_formula ou 
#     será 0
#     """
#     if primeiro_resultado_formula <= 9:
#         primeiro_resultado_formula
#     else:
#         primeiro_resultado_formula = 0


#     #Verificação do segundo dígito após o "-"
#     segundo_valor1 = 11 * int(novo_cpf[0])
#     segundo_valor2 = 10 * int(novo_cpf[1])
#     segundo_valor3 = 9 * int(novo_cpf[2])
#     segundo_valor4 = 8 * int(novo_cpf[3])
#     segundo_valor5 = 7 * int(novo_cpf[4])
#     segundo_valor6 = 6 * int(novo_cpf[5])
#     segundo_valor7 = 5 * int(novo_cpf[6])
#     segundo_valor8 = 4 * int(novo_cpf[7])
#     segundo_valor9 = 3 * int(novo_cpf[8])
#     segundo_valor10 = 2 * primeiro_resultado_formula

#     segunda_soma_valores = segundo_valor1 + segundo_valor2 + segundo_valor3 + segundo_valor4 + segundo_valor5 + segundo_valor6 + segundo_valor7 + segundo_valor8 + segundo_valor9 + segundo_valor10


#     segundo_resultado_formula = 11 - (segunda_soma_valores % 11)

#     """
#     Verificando se o primeiro dígito após o "-"
#     será o próprio valor do primeiro_resultado_valor ou 
#     será 0
#     """
#     if segundo_resultado_formula <= 9:
#         segundo_resultado_formula
#     else: 
#         segundo_resultado_formula = 0

    


#     if cpf == novo_cpf:
#         print('CPF válido')
#     else:
#         print('CPF inválido')

# validador_cpf(novo_cpf)


#Solução do curso

while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
    print(novo_cpf)
    reverse = 10
    total = 0

    """
    Ao total, serão necessárias 19 vezes para realizar
    todos os cálculos
    """
    for index in range(19): 
        #No íncide 8, retorna ele para 0 para prosseguir com a contagem a partir de 0
        if index > 8:
            index -= 9

        print(novo_cpf[index])
        total += int(novo_cpf[index]) * reverse

        reverse -=1
        if reverse < 2:
            reverse = 11
            digito = 11 - (total % 11)

            if digito > 9: 
                digito = 0
            total = 0
            novo_cpf += str(digito)

    if cpf == novo_cpf:
        print('Válido')
    else: 
        print('Inválido')

    



