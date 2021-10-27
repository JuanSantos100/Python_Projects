""""
cpf = 168.995.350-09
-----------------------------------
"""
def validador_cpf(cpf):
    # Retirando os pontos e - do cpf
    caracteres = '.-'

    for x in range(len(caracteres)):
        cpf = cpf.replace(caracteres[x], '')


    #Verificação do primeiro dígito após o "-"
    primeiro_valor1 = 10 * int(cpf[0])
    primeiro_valor2 = 9 * int(cpf[1])
    primeiro_valor3 = 8 * int(cpf[2])
    primeiro_valor4 = 7 * int(cpf[3])
    primeiro_valor5 = 6 * int(cpf[4])
    primeiro_valor6 = 5 * int(cpf[5])
    primeiro_valor7 = 4 * int(cpf[6])
    primeiro_valor8 = 3 * int(cpf[7])
    primeiro_valor9 = 2 * int(cpf[8])

    primeira_soma_valores = primeiro_valor1 + primeiro_valor2 + primeiro_valor3 + primeiro_valor4 + primeiro_valor5 + primeiro_valor6 + primeiro_valor7 + primeiro_valor8 + primeiro_valor9

    primeiro_resultado_formula = 11 - (primeira_soma_valores % 11)

    """
    Verificando se o primeiro dígito após o "-"
    será o próprio valor do resultado_formula ou 
    será 0
    """
    if primeiro_resultado_formula <= 9:
        primeiro_resultado_formula
    else:
        primeiro_resultado_formula = 0


    #Verificação do segundo dígito após o "-"
    segundo_valor1 = 11 * int(cpf[0])
    segundo_valor2 = 10 * int(cpf[1])
    segundo_valor3 = 9 * int(cpf[2])
    segundo_valor4 = 8 * int(cpf[3])
    segundo_valor5 = 7 * int(cpf[4])
    segundo_valor6 = 6 * int(cpf[5])
    segundo_valor7 = 5 * int(cpf[6])
    segundo_valor8 = 4 * int(cpf[7])
    segundo_valor9 = 3 * int(cpf[8])
    segundo_valor10 = 2 * primeiro_resultado_formula

    segunda_soma_valores = segundo_valor1 + segundo_valor2 + segundo_valor3 + segundo_valor4 + segundo_valor5 + segundo_valor6 + segundo_valor7 + segundo_valor8 + segundo_valor9 + segundo_valor10


    segundo_resultado_formula = 11 - (segunda_soma_valores % 11)

    """
    Verificando se o primeiro dígito após o "-"
    será o próprio valor do primeiro_resultado_valor ou 
    será 0
    """
    if segundo_resultado_formula <= 9:
        segundo_resultado_formula
    else: 
        segundo_resultado_formula = 0



meu_cpf = '072.995.765-97'
validador_cpf(meu_cpf)



