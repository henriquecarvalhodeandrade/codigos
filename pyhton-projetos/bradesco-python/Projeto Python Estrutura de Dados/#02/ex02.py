
# criando dicionarios a partir de listas, usanmos dict e zip
cidades = ['maringa','itabira','uberlania','salvador','fortaleza']
populacao = [403.063,120.423,144.4654,986.234,022.667]
popCidades = dict(zip(cidades, populacao))
print("\n",popCidades)

# transformando listas em dicionarios usando dict e zip
print('maringa' in cidades, "\n") # true
print('são josé dos campos' in cidades, "\n") # false

# adicionando novas cidades e populaçao
popCidades['sao jose dos campos'] = 226.000
print(popCidades)

# deletando item do dicionario
del popCidades['salvador']
print(popCidades)
