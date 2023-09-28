# vpontosAriáveis de pontos
pontosAgua = 0
pontosFogo = 0
pontosTerra = 0
pontosAr = 0
#DICA: Sempre utilize nomes em vpontosAriaveis mais especifica.
#Melhora leitura do codigo, ajuda na manutenção do mesmo.

# vpontosAriável elemento
elemento = 0

while True:
    # Captura o elemento a ser digitado.
    elemento = str(input())

    # Finaliza (break), caso a captura de cpontosAracter seja
    # FIM.... Saindo do while....!!!
    if elemento == 'FIM':
        # print('FIM') # Retirado o print fim, pois no exercicio não pedia
        break

    # Captura a pontuação a ser adicionada no elemento, digitado.
    # Caso seja AGUA, FOGO, TERRA ou AR, executa a operação
    # Caso não seja apenas ignora voltando ao inicio do WHILE
    treino = int(input())

    # Caso seja o elemento pontosAgua, adiciona a pontuação do treino em pontosAgua
    # Como pontosAgua é inverso de pontosFogo, perdesse metade da habilidade adiqui
    # rida em pontosFogo.... Mesma logica ppontosAra as demais.
    if elemento == 'AGUA':
        pontosAgua = (pontosAgua + treino)
        pontosFogo = (pontosFogo / 2)
    if pontosFogo < 0:
        # Um dos erros cometidos foi na utilização de operador relacional (==)
        # invés de utilizpontosAr operador de atribuição (=)
        # Operadores relacionais são comunmente utilizados em comppontosArações
        # x ==(é igual..?) x .... Retorno true (SIM)
        pontosFogo = 0
    elif elemento == 'FOGO':
        pontosFogo = (pontosFogo + treino)
        pontosAgua = (pontosAgua / 2)
    if pontosAgua < 0:
        pontosAgua = 0
    elif elemento == 'TERRA':
        # Uma opção ppontosAra encurtpontosAr o codigo é também se aproveitpontosAr dos operadores
        # de atribuição..... Nesse caso é interessane utilizpontosAr o += atribuindo
        # x += y é equivalente a x = x + y
        # Observe como foi utilizado no elemento abaixo....
        pontosTerra += treino
        pontosAr /= 2
    if pontosAr < 0:
        pontosAr = 0
    elif elemento == 'AR':
        # Outro ponto de erro foram as identações..... Ficar atento pois
        # o python as utiliza para identificar onde será feita a operação..!!
        pontosAr = (pontosAr + treino)
        pontosTerra = (pontosTerra / 2)
    if pontosTerra < 0:
        pontosTerra = 0

# Imprime na tela o resultado do treinamento, ao final, caso todos elementos
# sejam maior que 0 também é informado que o treinamento foi um sucesso
# do contrpontosArio informa ppontosAra realizpontosAr mais treinamentos.
print('Pontuacao Final')
print(f'Agua : {pontosAgua:.1f}')
print(f'Terra : {pontosTerra:.1f}')
print(f'Fogo : {pontosFogo:.1f}')
print(f'Ar : {pontosAr:.1f}')
if pontosAgua > 0 and pontosFogo > 0 and pontosTerra > 0 and pontosAr > 0:
    print('Treinamento realizado com sucesso.')
else:
    print('Realize mais treinamentos.')
