#       indices
#       0123456789.............33

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
print(tamanho_frase)
contador = 0
novaString = ''

letra_usuario = input('Qual letra você deseja colocar como maiúsculas: ')

while len(letra_usuario) > 1:
    print('Jovem, você deve digitar apenas uma letra.')
    letra_usuario = input('Qual letra você deseja colocar como maiúsculas: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == letra_usuario:
        novaString += letra_usuario.upper()
    else: 
        novaString += letra
    #print(novaString)
    contador += 1

print(novaString)


