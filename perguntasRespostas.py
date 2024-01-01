import os

perguntas = [
    {
        'Pergunta' : 'Quanto é 2 + 2 ?',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta' : 'Quanto é 5 * 5 ?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2 ?',
        'Opções' : ['2', '6', '1', '5'],
        'Resposta': '5',
    },
]
acertos = 0 
for pergunta in perguntas : 

    os.system('cls')

    print('Pergunta : ', pergunta['Pergunta'])
    print('Opções: ')
    opcoes_enumeradas = enumerate(pergunta['Opções'])
    for opcao in opcoes_enumeradas:
        print(f'{opcao[0]}) {opcao[1]}')
    try : 
        opcao_escolhida = input('Escolha uma opção: ')
        resposta = pergunta['Opções'][int(opcao_escolhida)]
        if resposta == pergunta['Resposta']:
            acertos += 1
    except TypeError : 
        continue
    except ValueError: 
        continue
    except IndexError: 
        continue

print(f'Você fez {acertos} acertos de {len(perguntas)} perguntas')