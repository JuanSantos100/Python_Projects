from pacote_1_vendas.formata import preco

def aumento(valor, porcentagem, formata=False):
    resultado = valor + (valor * (porcentagem / 100))
    
    if formata:
        return preco.converteReal(resultado)
    else: 
        return resultado

def reducao(valor, porcentagem, formata=False):
    resultado = valor - (valor * (porcentagem / 100))

    if formata:
        return preco.converteReal(resultado)
    else:
        return resultado