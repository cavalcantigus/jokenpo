from random import randint

continuar = 's'
pontuação = 0
print("Bem vindo ao Game")
while continuar.lower() == 's':

    pedra_papel_tesoura = ("Pedra", "Papel", "Tesoura")
    maquina = randint(0, 2)
    pergunta = int(
        input("""Suas opcções:
[0] Pedra
[1] Papel
[2] Tesoura
Faça sua escolha: """))
    print('JO')
    print('KEN')
    print('PO!')
    print('=' * 22)
    print(f'Você escolheu {pedra_papel_tesoura[pergunta]}')
    print(f'O computador escolheu: {pedra_papel_tesoura[maquina]}')
    print('=' * 22)
    if maquina == 0:
        if pergunta == 0:
            print('Empate!')
            print('=' * 22)
        elif pergunta == 1:
            print('Você ganhou! Parabéns, você ganhou 1 ponto')
            pontuação += 1
            print(f'Você tem {pontuação} pontos!')
            print('=' * 22)

        elif pergunta == 2:
            print('Você perdeu!')
            pontuação = pontuação - 1
            print(f'Você tem {pontuação} pontos')
            print('=' * 22)
    elif maquina == 1:
        if pergunta == 0:
            print('Você perdeu!')
            pontuação = pontuação - 1
            print(f'Você tem {pontuação} pontos')
            print('=' * 22)
        elif pergunta == 1:
            print('Empate!')
            print('=' * 22)
        elif pergunta == 2:
            print('Você ganhou! Parabéns, você ganhou 1 ponto')
            pontuação += 1
            print(f'Você tem {pontuação} pontos')
            print('=' * 22)
    elif maquina == 2:
        if pergunta == 0:
            print('Você ganhou! Parabéns, você ganhou 1 ponto')
            pontuação += 1
            print(f'Você tem {pontuação} pontos')
            print('=' * 22)
        elif pergunta == 1:
            print('Você perdeu!')
            pontuação = pontuação - 1
            print(f'Você tem {pontuação} pontos')
            print('=' * 22)
        elif pergunta == 2:
            print('Empate!')
            print('=' * 22)
    else:
        if pergunta == 0:
            print('Você perdeu!')
            pontuação = pontuação - 1
            print(f'Você tem {pontuação} pontos')
            print('=' * 22)
        elif pergunta == 1:
            print('Você ganhou! Parabéns, você ganhou 1 ponto')
            pontuação += 1
            print(f'Você tem {pontuação} pontos')
            print('=' * 22)
        elif pergunta == 2:
            print('Empate!')
            print('=' * 22)

    continuar = input('Deseja continuar?  [S] - Sim [N] - Não: ')
    if continuar == 'N':
        print('Jogo encerrado')
        print(f'Você ficou com um total de {pontuação} pontos!')
