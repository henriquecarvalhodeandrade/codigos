import pandas as pd

# usando dataframe do pandas, dataframe funciona como uma tabela, criamos um dicionario


disciplinas = {
    'cursos': ['estatistica', 'economia', 'calculo', 'geometria'],
    'creditos': [90,60,90,40],
    'requisito': [True, False, True, False] 
}

dataframe = pd.DataFrame(disciplinas)

print(dataframe)

# criando dataframes a partir de duas listas
print('\n')

cidades = pd.Series(['maringa','itabira','uberlania','salvador','fortaleza'])
populacao = pd.Series([403.063,120.423,144.4654,986.234,022.667])

datafram2 = pd.DataFrame({
    'cidade': cidades,
    'populacao': populacao
})


print(datafram2)
