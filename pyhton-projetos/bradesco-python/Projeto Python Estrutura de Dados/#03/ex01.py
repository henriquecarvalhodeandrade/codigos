import pandas as pd


#projetando a estrutura dos dados para transforma-los em .csv
autor = ['sun tzu', 'fernando pessoa', 'thomas mann', 'joao guimaraes rosa']
livro = ['a arte da guerra', 'poesias selecionadas', 'a montanha magica', 'primeiras estorias']
ano = [2000, 2004, 2015, 2017]

dados = {
    'autor': autor,
    'livro': livro,
    'ano': ano
}

autores = pd.DataFrame(dados)

# vamos vizualizar qual o tipo de estrutura esta sendo criada:
print(type(autores))
df = pd.DataFrame(autores)
print(df)

# criando o arquivo .csv
df.to_csv('autores.csv')

# lendo arquivos em csv:
print()
autores = pd.read_csv('autores.csv')
print(autores)
# com formatacao em tabela
print()
autores = pd.read_csv('autores.csv', index_col=0)
print(autores)

# obter informaçoes importantes sobre o arquivo csv:
print()
print(autores.info())

# podemos visualizar apenas o que é de interesse:
print()
print(autores.columns)
print(autores.index)

# outra forma de mostrar informaçoes de um arquivo é o comando: nome_arquivo.head()

# Para sumarizar as informações estatísticas da tabela, usamos a chamada describe().


