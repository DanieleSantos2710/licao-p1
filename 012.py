preço = float(input('Digite o preço do produto: '))
porcentagem = (preço / 100) * 5
r = preço - porcentagem
print('Esse é o valor do novo preço {}'.format(r))
