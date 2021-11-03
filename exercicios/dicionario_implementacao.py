"""
Criando um sistema de perguntas e respostas
"""
print()
print('Texto Explicativo')

respostas_certas = 0

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas' : {
            'a': '4',
            'b': '6',
            'c': '9',
            'd': '5',
            'e': '8'
        },
        'resposta_certa': 'a'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 9 * 5 ?',
        'respostas' : {
            'a': '36',
            'b': '47',
            'c': '45',
            'd': '40',
            'e': '21'
        },
        'resposta_certa': 'c'
    }, 
    'Pergunta 3': {
        'pergunta': 'Quanto é 4 * 12 ? ',
        'respostas' : {
            'a': '78',
            'b': '16',
            'c': '89',
            'd': '48',
            'e': '10'
        },
        'resposta_certa': 'd'
    }, 
    'Pergunta 4': {
        'pergunta': 'Qual a raiz quadrada de 144 ?',
        'respostas' : {
            'a': '12',
            'b': '20',
            'c': '16',
            'd': '10',
            'e': '8'
        },
        'resposta_certa': 'a'
    }, 
    'Pergunta 5': {
        'pergunta': 'Quanto é 10 / 2',
        'respostas' : {
            'a': '2',
            'b': '4',
            'c': '5',
            'd': '1',
            'e': '3'
        },
        'resposta_certa': 'c'
    }, 
}

print()
#Iteração da pergunta
for pergunta_chave, pergunta_valor in perguntas.items():
    print(f'{pergunta_chave} : {pergunta_valor["pergunta"]}')
    print('Escolha uma das opções abaixo: ')
    
    for resposta_chave, resposta_valor in pergunta_valor['respostas'].items(): #imprimindo perguntas e respostas
        print(f'\t[{resposta_chave}]: {resposta_valor}')

    resposta_usuario = input('Digite sua resposta: ')

    if resposta_usuario == pergunta_valor['resposta_certa']:
        respostas_certas += 1
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

if respostas_certas == 0:
    print('Você errou todas as respostas.')
else:
    print(f'Você acertou {respostas_certas} respostas.')

print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')