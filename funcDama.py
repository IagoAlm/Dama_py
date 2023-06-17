import sys
import string
from itertools import cycle

# ---------------------------FUNÇÕES QUE FUNCIONAM CORRETAMENTE E NÃO PRECISA ALTERAR NADA PELO AMOR DE DEUS--------------------------------------#


def carregaEntrada():
    entradaPadrao = 'aaaaaaaaaaaa.b......bbbbbbbbbbbb:a'
    try:
        entrada = sys.argv[1]
    except:
        entrada = entradaPadrao
    entrada = entrada.split(':')
    return entrada


def tradutor(coordenadas):

    linha = str((int(coordenadas[0]) + 1))
    coluna = string.ascii_uppercase[int(coordenadas[1])]
    traduzid = linha + coluna
    return traduzid


def interpretador(coordenadas):
    try:
        linha = str((int(coordenadas[0]) - 1))
        for i in range(len(string.ascii_lowercase)):
            if string.ascii_lowercase[i] == coordenadas[1].lower():
                coluna = str(i)
        interp = linha + coluna
        return interp
    except:
        return None


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


def verCapturaAcima(tabuleiro, linha, i, alvo):
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


def verCapturaAbaixo(tabuleiro, linha, i, alvo):
    capturas = dict()
    pos1 = False
    pos2 = False
    pos3 = False
    pos4 = False
    if i-1 >= 0 and linha+1 < 8 and (tabuleiro[linha+1][i-1] == alvo or tabuleiro[linha+1][i-1] == alvo.upper()):
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

    if i+1 <= 7 and linha+1 < 8 and (tabuleiro[linha+1][i+1] == alvo or tabuleiro[linha+1][i+1] == alvo.upper()):
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


def verCapturas(tabuleiro, linha, jogador, alvo):
    resTot = dict
    capturas = dict()

    for i in range(len(tabuleiro[linha])):
        if tabuleiro[linha][i] == jogador:
            if jogador == 'b':
                res = verCapturaAcima(tabuleiro, linha, i, alvo)
            elif jogador == 'a':
                res = verCapturaAbaixo(tabuleiro, linha, i, alvo)
            if res != None:
                capturas[str(linha)+str(i)] = res
        if tabuleiro[linha][i] == jogador.upper():
            resAcima = verCapturaAcima(tabuleiro, linha, i, alvo)
            resAbaixo = verCapturaAbaixo(tabuleiro, linha, i, alvo)
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
                capturas.append(verCapturas(tabuleiro, i, jogador, alvo))
            if verJogadas(tabuleiro, i, jogador) != {}:
                jogadas.append(verJogadas(tabuleiro, i, jogador))
    return (capturas, jogadas)

# ---------------------------FUNÇÕES QUE FUNCIONAM CORRETAMENTE E NÃO PRECISA ALTERAR NADA PELO AMOR DE DEUS--------------------------------------#
