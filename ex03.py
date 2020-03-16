"""1 Escreva um programa que lê̂ duas notas de vários alunos e armazena tais notas em
um dicionário, em que a chave é o nome do aluno. A entrada de dados deve terminar
quando for lida uma string vazia como nome. A seguir, faça um loop que pede o nome
do aluno e mostra sua média.
"""

#dicionario vazio
dicionario = {}

#entrada de dados
while True:
    nome = input('Informe o nome do aluno: ')
    if nome == '':# nomes vazios são inválidos
        break
    else:
        n1, n2 = float(input(f'Informe a primeira nota de {nome}: ')), float(input(f'Informe a segunda nota de {nome}: '))
    #populando o dicionario com informaçoes fornecidas
    dicionario[nome] = n1, n2

#lista vazia
notas_aluno = []

media = 0.0

while True:
    aluno = input('De que aluno deseja saber a média? ')
    if aluno == '':
        break
    else:
        if aluno in dicionario:
            notas_aluno = dicionario[aluno]
            media = (notas_aluno[0] + notas_aluno[1])/2
            print(f'A media de {aluno} é {media}')
        
        else:
            print('Aluno inexistente!')




