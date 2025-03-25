# criando a lista da semana
lista_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

# recebendo o dia e o horário do usuário
dia = input('Qual o dia de hoje?\n:')
horario = int(input('Qual o horário da refeição do passarinho?\n (Digite apenas a hora)\n:'))
dia = dia.lower().capitalize()

# identificando qual o dia é na lista
if dia in lista_semana:
    indice_dia = lista_semana.index(dia)
else:
    print("Dia inválido.")
    exit()

# verificando se o horário é válido
if 0 <= horario < 24:
    indice_horario = horario
else:
    print("Horário inválido.")
    exit()

# iterando por 7 dias para simular uma semana
for _ in range(14):
    print(f'{lista_semana[indice_dia]} - {indice_horario}:00')
    indice_horario = (indice_horario + 23) % 24
    if indice_horario < horario:
        indice_dia = (indice_dia + 1) % 7
