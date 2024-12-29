d = int(input('Por quantos dias você alugou o carro: '))
km = float(input('Qunatos km você rodou: '))
c = d * 60
r = km * (0.15)
soma = c + r
print('O valor a ser pago é {:.2f}'.format(soma))
