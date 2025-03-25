from passaro import Passaro

nome = input('Qual o nome do passáro?\n:')
raca = input('Qual o raça do passáro?\n:')
tamanho = input('Qual o tamanho do passáro?\n:')

birdo = Passaro(nome, raca, tamanho)
birdo.cantar()
birdo.alimentarSe()
birdo.dormir()
birdo.informacoes()
