"""
Listas em Python
 Fatiamento
 append, insert, pop, del, clear, extend, + 
 min, mas 
 range
"""
#         0    1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]

#print(lista[::-1])

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

#print(l3)

l1.extend(l2)  #faz a extensão da lista com valores, nesse caso, adicionou toda a lista 2
# print(l1)
# print(l2)

l2.append('b') #adiciona um valor ao fim da lista
# print(l2)

l2.insert(0, 'banana')
# print(l2[0])
# print(l2)

l2.pop()  #Faz a exclusão do último item da lista
# print(l2)

l4 = [1,2,3,4,5,6,7,8,9,10]
del(l4[3:5])   #Removendo os índices del(l4[indice(s)])
# print(l4)

l5 = [1,2,3,4,5,6,7,8,9,10]
# print(max(l5))
# print(min(l5))


"""
range é um objeto iterável, podendo passar de valor em valor
entretanto, por si só, não acrescenta na lista l6 os valores de 0 a 100 configurados.
Para isso, eu posso usar a função built-in list() para iterar os valores e acrescentá-los 
na minha lista
"""
l6 = list(range(0, 100))
# print(l6) 
# for valor in l6:
#     print(valor)


l7 = ['String', True, 100, 55.79]
# for elemento in l7:
#     print(f'O tipo de {elemento} é {type(elemento)}')

def forca():
    
    palavraSecreta = 'perfume'
    digitadas = []
    chances = 7
    while True:
        if chances <= 0:
            print('Você perdeu!!!')
            break



        letra = input('Digite uma letra: ')
        
        if len(letra) > 1:
            print('Ahh, qual é?? digite apenas uma letra...')
            continue
        
        digitadas.append(letra)
    

        if letra in palavraSecreta:
            print(f'Boaaaaa, a letra "{letra}" existe na palavra secreta.')
        else:
            print(f'Puxaaa, que pena ! A letra "{letra}" não existe na palavra secreta.')
            digitadas.pop()

        secretoTemporario = ''
        for letraSecreta in palavraSecreta:
            if letraSecreta in digitadas:
                secretoTemporario += letraSecreta
            else:
                secretoTemporario += '*'
        
        if secretoTemporario == palavraSecreta:
            print(f'Parabéns !!! Você acertou a palavra secreta: {palavraSecreta}')
            break
        else:
            print(f'A palavra secreta está assim: {secretoTemporario}')

        if letra not in palavraSecreta:
            chances -= 1
            print('Você ainda tem {} chances'.format(chances))