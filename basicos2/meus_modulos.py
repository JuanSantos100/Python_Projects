import math

PI = math.pi

def dobra_lista(lista):
    return [x * 2 for x in lista]



def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r

#Todo módulo por padrão executa main
#Condicional para impressão de testes
if __name__ == '__main__':
    lista = [2,4,6,8,10]
    print(multiplica(lista))
    print(PI)