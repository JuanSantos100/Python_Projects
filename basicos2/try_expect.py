"""
Try except 
"""


try: 
    a = 0
    try: 
        a = 1/0
    except:
        print('Erro') #Ao tratar essa exceção, não consigo me propagar para as demais exceções que poderiam ser geradas


# Tratando um erro do tipo NameError
except NameError as erro: 
    print('Erro do desenvolvedor, fale com ele')
except (IndexError, KeyError) as indice: 
    print('Erro de índice')

#Tratando uma possível nova exceção | Exception significa qualquer tipo de exceção
except Exception as erro: 
    print('Ocorreu um erro inesperado')

else: # O bloco else sempre será executado se não houver nenhum erro -> Como uma continuação do que foi escrito no Try:
    pass
finally: # Essa cláusula é SEMPRE executada
    a = None #Criando uma variável no bloco finally para evitar o erro gerado na linha 24


print(a)

print('#' * 40)


def converte_numero(valor): # Toda função retorna None como padrão
    try: 
        valor = int(valor)
        return valor
    except ValueError:
        try: 
            valor = float(valor)
            return valor   
        except:
            pass #retornando none

while True:
    numero = converte_numero(input('Digite um número: '))

    if numero is not None:
        if numero == 0:
            print('Não multiplique 0')
        else:
            print(numero * 5)
    else: 
        print('O que você digitou não é um número')