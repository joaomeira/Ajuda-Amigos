# variáveis
ag = 0
fg = 0
te = 0
a = 0
# variável elemento
elemento = 0
while True:
    elemento = str(input())
    if elemento == 'FIM':
        print('FIM')
        break
    treino = int(input())
    if elemento == 'AGUA':
        ag = (ag + treino)
        fg = (fg/2)
    if fg < 0:
        fg == 0
    elif elemento == 'FOGO':
        fg = (fg + treino)
    ag = (ag/2)
    if ag < 0:
        ag == 0
    elif elemento == 'TERRA':
        te = (te + treino)
    a = (a/2)
    if a < 0:
        a == 0
    elif elemento == 'AR':
            a = (a + treino)
    te = (te/2)
    if te < 0:
        te == 0

print('Pontuacao Final')
print (f'Agua : {ag:.1f}')
print (f'Terra : {te:.1f}')
print(f'Fogo : {fg:.1f}')
print(f'Ar : {a:.1f}')
if ag > 0 and fg > 0 and te > 0 and a > 0:
    print('Treinamento realizado com sucesso.')
else:
    print('Realize mais treinamentos.')
