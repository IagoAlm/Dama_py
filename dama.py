import sys
import string
import time
from itertools import cycle


def carregaEntrada():
    entradaPadrao = 'aaaaaaaaaaaa........bbbbbbbbbbbb:a'
    try:
        entrada = sys.argv[1]
    except:
        entrada = entradaPadrao
    entrada = entrada.split(':')
    return entrada


def transfDama(tabuleiro):
    for i in range(len(tabuleiro[0])):
        if tabuleiro[0][i] == 'b':
            tabuleiro[0][i] = 'B'
    for i in range(len(tabuleiro[7])):
        if tabuleiro[7][i] == 'a':
            tabuleiro[7][i] = 'A'


def lerInput(entrada):
    linha = list()
    tabuleiro = list()
    coluna = 1
    contr = 0
    fileira = 1
    for i in range(0, len(entrada)*2, 1):
        if fileira % 2 != 0:
            if coluna % 2 == 0:
                linha.append(entrada[contr])
                contr += 1
            else:
                linha.append(' ')

        elif fileira % 2 == 0:
            if coluna % 2 != 0:
                linha.append(entrada[contr])
                contr += 1
            else:
                linha.append(' ')

        if coluna < 8:
            coluna = coluna + 1
        else:
            tabuleiro.append(linha)
            linha = []
            coluna = 1
            fileira = fileira + 1
    return tabuleiro


def atualizarTabuleiro(tabuleiro):
    print('     ', end='')
    for i in range(8):
        print(string.ascii_uppercase[i], end=' ')
    i = 0
    print(end='\n\n')
    for linha in tabuleiro:
        i += 1
        print(i, end='   |')
        for item in linha:
            print(item, end='|')
        print()


def verCapturasAcima(tabuleiro, linha, i, alvo):
    capturas = dict()
    pos1 = False
    pos2 = False
    pos3 = False
    pos4 = False
    if i-1 >= 0 and linha-1 > 0 and (tabuleiro[linha-1][i-1] == alvo or tabuleiro[linha-1][i-1] == alvo.upper()):
        if i-2 >= 0 and tabuleiro[linha-2][i-2] == '.':
            pos1 = str(linha-2)
            pos1 = pos1 + str(i-2)
        if tabuleiro[linha-2][i] == '.':
            pos2 = str(linha-2)
            pos2 = pos2 + str(i)

        esq = str(linha-1) + str(i-1)
        if pos1 != False and pos2 != False:
            capturas[esq] = (pos1, pos2)
        elif pos1 != False and pos2 == False:
            capturas[esq] = (pos1)
        elif pos1 == False and pos2 != False:
            capturas[esq] = (pos2)

    if i+1 <= 7 and linha-1 > 0 and (tabuleiro[linha-1][i+1] == alvo or tabuleiro[linha-1][i+1] == alvo.upper()):
        if tabuleiro[linha-2][i] == '.':
            pos3 = str(linha-2)
            pos3 = pos3 + str(i)

        if i+2 <= 7 and tabuleiro[linha-2][i+2] == '.':
            pos4 = str(linha-2)
            pos4 = pos4 + str(i+2)
        direit = str(linha-1) + str(i+1)
        if pos3 != False and pos4 != False:
            capturas[direit] = (pos3, pos4)
        elif pos3 != False and pos4 == False:
            capturas[direit] = (pos3)
        elif pos3 == False and pos4 != False:
            capturas[direit] = (pos4)

    if capturas != {}:
        return capturas


def verCapturasAbaixo(tabuleiro, linha, i, alvo):
    capturas = dict()
    pos1 = False
    pos2 = False
    pos3 = False
    pos4 = False
    if i-1 >= 0 and linha+2 <= 7 and (tabuleiro[linha+1][i-1] == alvo or tabuleiro[linha+1][i-1] == alvo.upper()):
        if i-2 >= 0 and tabuleiro[linha+2][i-2] == '.':
            pos1 = str(linha+2)
            pos1 = pos1 + str(i-2)
        if tabuleiro[linha+2][i] == '.':
            pos2 = str(linha+2)
            pos2 = pos2 + str(i)

        esq = str(linha+1) + str(i-1)
        if pos1 != False and pos2 != False:
            capturas[esq] = (pos1, pos2)
        elif pos1 != False and pos2 == False:
            capturas[esq] = (pos1)
        elif pos1 == False and pos2 != False:
            capturas[esq] = (pos2)

    if i+1 <= 7 and linha+2 <= 7 and (tabuleiro[linha+1][i+1] == alvo or tabuleiro[linha+1][i+1] == alvo.upper()):
        if tabuleiro[linha+2][i] == '.':
            pos3 = str(linha+2)
            pos3 = pos3 + str(i)

        if i+2 <= 7 and tabuleiro[linha+2][i+2] == '.':
            pos4 = str(linha+2)
            pos4 = pos4 + str(i+2)
        direit = str(linha+1) + str(i+1)
        if pos3 != False and pos4 != False:
            capturas[direit] = (pos3, pos4)
        elif pos3 != False and pos4 == False:
            capturas[direit] = (pos3)
        elif pos3 == False and pos4 != False:
            capturas[direit] = (pos4)

    if capturas != {}:
        return capturas


def verCapturasExtras(tabuleiro, linha, coluna, jogador, alvo):
    resTot = dict
    capturas = dict()
    res = ''

    if jogador == 'b':
        resTot = verCapturasAcima(tabuleiro, linha, coluna, alvo)
    elif jogador == 'a':
        resTot = verCapturasAbaixo(tabuleiro, linha, coluna, alvo)

    if jogador == 'A' or jogador == 'B':
        resAcima = verCapturasAcima(tabuleiro, linha, coluna, alvo)
        resAbaixo = verCapturasAbaixo(tabuleiro, linha, coluna, alvo)
        if resAcima != None and resAbaixo != None:

            resTot = {k: v for d in (resAcima, resAbaixo)
                      for (k, v) in d.items()}
        elif resAcima != None and resAbaixo == None:
            resTot = resAcima

        elif resAbaixo != None and resAcima == None:
            resTot = resAbaixo

        else:
            resTot = None
    return resTot


def verCapturas(tabuleiro, linha, jogador, alvo):
    resTot = dict
    capturas = dict()
    res = ''
    for i in range(len(tabuleiro[linha])):
        if tabuleiro[linha][i] == jogador:
            if jogador == 'b':
                res = verCapturasAcima(tabuleiro, linha, i, alvo)
            elif jogador == 'a':
                res = verCapturasAbaixo(tabuleiro, linha, i, alvo)
            if res != None:
                capturas[str(linha)+str(i)] = res
        if tabuleiro[linha][i] == jogador.upper():
            resAcima = verCapturasAcima(tabuleiro, linha, i, alvo)
            resAbaixo = verCapturasAbaixo(tabuleiro, linha, i, alvo)
            if resAcima != None and resAbaixo != None:

                resTot = {k: v for d in (resAcima, resAbaixo)
                          for (k, v) in d.items()}
            elif resAcima != None and resAbaixo == None:
                resTot = resAcima

            elif resAbaixo != None and resAcima == None:
                resTot = resAbaixo

            else:
                resTot = None

            if resTot != None:
                capturas[str(linha)+str(i)] = resTot

    return capturas


def verQuant(tabuleiro, letra):
    quant = 0
    for linha in tabuleiro:
        for item in linha:
            if item == letra or item == letra.upper():
                quant += 1
    return quant


def verAcima(tabuleiro, linha, i):
    esquerdaInt = False
    direitaInt = False
    if i-1 >= 0 and linha-1 >= 0 and tabuleiro[linha-1][i-1] == '.':
        esquerdaInt = str(linha-1)
        esquerdaInt = esquerdaInt + str(i-1)
    if i+1 <= 7 and linha-1 >= 0 and tabuleiro[linha-1][i+1] == '.':
        direitaInt = str(linha-1)
        direitaInt = direitaInt + str(i+1)
    # o retorno desses dados é 1 a mais na linha
    if esquerdaInt and direitaInt:
        return (esquerdaInt, direitaInt)
    elif direitaInt:
        return (direitaInt,)
    elif esquerdaInt:
        return (esquerdaInt,)


def verAbaixo(tabuleiro, linha, i):
    esquerdaInt = False
    direitaInt = False
    if i-1 >= 0 and linha+1 < 8 and tabuleiro[linha+1][i-1] == '.':
        esquerdaInt = str(linha+1)
        esquerdaInt = esquerdaInt + str(i-1)
    if i+1 <= 7 and linha+1 < 8 and tabuleiro[linha+1][i+1] == '.':
        direitaInt = str(linha+1)
        direitaInt = direitaInt + str(i+1)
    # o retorno desses dados é 1 a mais na linha
    if esquerdaInt and direitaInt:
        return (esquerdaInt, direitaInt)
    elif direitaInt:
        return (direitaInt,)
    elif esquerdaInt:
        return (esquerdaInt,)


def verJogadas(tabuleiro, linha, jogador):
    jogadas = dict()

    for i in range(len(tabuleiro[linha])):
        if tabuleiro[linha][i] == jogador:
            if jogador == 'b':

                res = verAcima(tabuleiro, linha, i)
            elif jogador == 'a':
                res = verAbaixo(tabuleiro, linha, i)
            if res != None:
                jogadas[str(linha)+str(i)] = [x for x in res]

        if tabuleiro[linha][i] == jogador.upper():
            resAcima = verAcima(tabuleiro, linha, i)
            resAbaixo = verAbaixo(tabuleiro, linha, i)
            if resAcima != None and resAbaixo != None:
                resTot = resAcima + resAbaixo
            elif resAcima != None and resAbaixo == None:
                resTot = resAcima
            elif resAbaixo != None and resAcima == None:
                resTot = resAbaixo
            else:
                resTot = None
            if resTot != None:
                jogadas[str(linha)+str(i)] = [x for x in resTot]
    return jogadas


def verMov(tabuleiro, jogador, alvo):
    capturas = list()
    jogadas = list()
    for linha in tabuleiro:
        for i in range(len(linha)):
            if verCapturas(tabuleiro, i, jogador, alvo) != {}:
                capturas.append(verCapturas(
                    tabuleiro, i, jogador, alvo))
            if verJogadas(tabuleiro, i, jogador) != {}:
                jogadas.append(verJogadas(tabuleiro, i, jogador))
    return (capturas, jogadas)


def tradutor(coordenadas):
    linha = str((int(coordenadas[0]) + 1))
    coluna = string.ascii_uppercase[int(coordenadas[1])]
    traduzid = linha + coluna
    return traduzid


def interpretador(coordenadas):
    if coordenadas.lower() == 'sair':
        exit()
    try:
        linha = str((int(coordenadas[0]) - 1))
        for i in range(len(string.ascii_lowercase)):
            if string.ascii_lowercase[i] == coordenadas[1].lower():
                coluna = str(i)
                break
        interp = linha + coluna
        return interp
    except:
        return None


def jogadaCaptura(linhaCapt):
    print("Capturas:")
    for linha in linhaCapt:
        listaPecas = list()
        pos = dict()
        loc = dict()
        alvo = ''
        print("As peças que podem capturar (por linha):")
        for peca in linhaCapt[linha]:
            print(tradutor(peca), 'pode capturar ', end='')
            for pecasAlvo in linhaCapt[linha][peca]:
                listaPecas.append(peca)
                print(tradutor(pecasAlvo), end=' ')
                print("e ir para:")
                jogador = tabuleiro[int(peca[0])][int(peca[1])]
                if jogador.lower() == 'a':
                    alvo = 'b'
                elif jogador.lower() == 'b':
                    alvo = 'a'

                if type(linhaCapt[linha][peca][pecasAlvo]) == str:
                    print(tradutor(linhaCapt[linha][peca][pecasAlvo]), end=' ')
                else:
                    for item in linhaCapt[linha][peca][pecasAlvo]:
                        print(tradutor(item), end=' ')
                print()
    entradaPeca = ''
    while entradaPeca not in listaPecas:
        print("Digite uma peça da lista informada")
        entradaPeca = interpretador(
            input("Escolha a peça que vai capturar: "))

    entradaAlvo = ''
    if type(linhaCapt[linha][entradaPeca]) == str:
        while entradaAlvo != linhaCapt[linha][entradaPeca]:
            print("Digite uma peça da lista informada")
            entradaAlvo = interpretador(input("Escolha o alvo: "))
    else:
        while entradaAlvo not in linhaCapt[linha][entradaPeca]:
            print("Digite uma peça da lista informada")
            entradaAlvo = interpretador(input("Escolha o alvo: "))

    entradaDestino = ''
    if type(linhaCapt[linha][entradaPeca][entradaAlvo]) == str:
        while entradaDestino != linhaCapt[linha][entradaPeca][entradaAlvo]:
            print("Digite um destino da lista informada")
            entradaDestino = interpretador(input("Escolha o destino: "))
    else:
        while entradaDestino not in linhaCapt[linha][entradaPeca][entradaAlvo]:
            print("Digite um destino da lista informada")
            entradaDestino = interpretador(input("Escolha o destino: "))

    peca = tabuleiro[int(entradaPeca[0])][int(entradaPeca[1])]

    tabuleiro[int(entradaPeca[0])][int(entradaPeca[1])] = '.'
    tabuleiro[int(entradaAlvo[0])][int(entradaAlvo[1])] = '.'
    tabuleiro[int(entradaDestino[0])][int(entradaDestino[1])] = peca

    if verCapturasExtras(
            tabuleiro, int(entradaDestino[0]), int(entradaDestino[1]), peca, alvo) != None:
        verif = ''
        while verif != 'S' and verif != 'N':
            verif = input("Deseja continuar capturando?(S/N)").upper()
        if verif == 'S':
            #jogadaCaptura(verCapturas(tabuleiro, int(entradaDestino[0]), int(entradaDestino[1]), 'a'))
            pos[entradaDestino[0] + entradaDestino[1]] = verCapturasExtras(tabuleiro, int(
                entradaDestino[0]), int(entradaDestino[1]), peca, alvo)
            loc[int(entradaDestino[0])] = pos
            jogadaCaptura(loc)
            atualizarTabuleiro(tabuleiro)


def rodada(tabuleiro, jogador):
    multi = True
    parar = False
    qntA = 1
    qntB = 1
    print("Instruções:")
    print("Digite 'sair' em qualquer solicitação para fechar")
    print("A ordem das requisições de movimentação é: Peça que pode mover -> Lugar para onde quer mover")
    print("A ordem das requisições de captura é: Peça que pode capturar -> Peça que pode ser capturada -> Lugar para onde quer mover")
    if input("Aperte qualquer tecla para começar ou digite 'sair' para fechar").lower() == 'sair':
        exit()
    if jogador == 'a':
        ciclo = cycle(['a', 'b'])
    elif jogador == 'b':
        ciclo = cycle(['b', 'a'])
    i = 0

    while qntA > 0 and qntB > 0:

        transfDama(tabuleiro)
        atualizarTabuleiro(tabuleiro)

        qntA = int(verQuant(tabuleiro, 'a'))
        qntB = int(verQuant(tabuleiro, 'b'))

        if qntA <= 0 and qntB <= 0:
            parar = True
            print("Não existem peças")
            break
        elif qntA <= 0 and qntB >= 0:
            parar = True
            print("O jogador b venceu")
            break
        elif qntA >= 0 and qntB <= 0:
            parar = True
            print("O jogador a venceu")
            break

        vez = next(ciclo)
        print("-----Jogada de ", vez, '-----', sep='')
        linhaCapt = dict()
        linhaJog = dict()

        if vez == 'a':
            alvo = 'b'
        elif vez == 'b':
            alvo = 'a'

        if verMov(tabuleiro, 'a', 'b') == ([], []) and verMov(tabuleiro, 'b', 'a') == ([], []):
            print("Não existem jogadas disponíveis")
            break
        elif verMov(tabuleiro, 'a', 'b') != ([], []) and verMov(tabuleiro, 'b', 'a') == ([], []):
            print("O jogador a é o vencedor pois não há movimentos para o jogador b")
            break
        elif verMov(tabuleiro, 'a', 'b') == ([], []) and verMov(tabuleiro, 'b', 'a') != ([], []):
            print("O jogador b é o vencedor pois não há movimentos para o jogador a")
            break

        for i in range(len(tabuleiro)):
            if verCapturas(tabuleiro, i, vez, alvo) != {}:
                linhaCapt[i] = verCapturas(tabuleiro, i, vez, alvo)

            if verJogadas(tabuleiro, i, vez) != {}:
                linhaJog[i] = verJogadas(tabuleiro, i, vez)

        if linhaCapt != {}:
            jogadaCaptura(linhaCapt)
        else:
            print("Movimentação: ")
            print("As peças que podem se mover: ")
            disponiveis = list()
            for linha in linhaJog:
                for peca in linhaJog[linha]:
                    print(tradutor(peca), "para", end=' ')
                    for item in linhaJog[linha][peca]:
                        print(tradutor(item), end=' ')
                    print()
                    disponiveis.append(peca)
            entradaMov = interpretador(
                input("Digite a peça que deseja movimentar: "))
            while entradaMov not in disponiveis:
                print("Por favor, digite uma peça da lista informada")
                entradaMov = interpretador(
                    input("Digite a peça que deseja movimentar: "))
            if entradaMov in disponiveis:
                print("Pode se movimentar para: ")
                for item in linhaJog[int(entradaMov[0])][entradaMov]:
                    print(tradutor(item))
                entradaDestino = interpretador(input(
                    "Digite o lugar para onde vai se movimentar: "))

                while entradaDestino not in linhaJog[int(entradaMov[0])][entradaMov]:
                    print("Por favor, digite um movimento válido")
                    entradaDestino = interpretador(input(
                        "Digite o lugar para onde vai se movimentar: "))
                if entradaDestino in linhaJog[int(entradaMov[0])][entradaMov]:
                    peca = tabuleiro[int(entradaMov[0])][int(
                        entradaMov[1])]
                    tabuleiro[int(entradaMov[0])][int(
                        entradaMov[1])] = '.'
                    tabuleiro[int(entradaDestino[0])][int(
                        entradaDestino[1])] = peca


tabEntrada = carregaEntrada()[0]
jogInic = carregaEntrada()[1]
tabuleiro = lerInput(tabEntrada)
rodada(tabuleiro, jogInic)
