"""
Looping com acumuladores

utilização de while com ELSE
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(f'Valor contador {contador}, Valor acumulador {acumulador}')

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else: 
    print('Cheguei no else')

print('Isso será executado')