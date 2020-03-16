"""2 Faça um programa que percorre uma lista com o seguinte formato: [['Brasil', 'Italia',
[10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o
número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil
e Itália, o Brasil fez 10 faltas e a Itália fez 9.
O programa deve imprimir na tela:
- o total de faltas do campeonato
- o time que fez mais faltas
- o time que fez menos faltas"""

lista_paises = [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]

faltas_brasil, faltas_espanha, faltas_italia, soma = 0, 0, 0, 0


#somando os itens da lista
for item in lista_paises:
    for e in item[2]:
        soma = soma + e

#contando as faltas dos times da lista
for item in lista_paises:
    i = 0
    while i < 2:
        if item[i] == 'Brasil':
            faltas_brasil += item[2][i]
        
        elif item[i] == 'Italia':
            faltas_italia += item[2][i]

        elif item[i] == 'Espanha':
            faltas_espanha += item[2][i]            

        else:
            pass
        
        i = i + 1
#lista com países e suas faltas               
lista_faltas = [['Brasil', faltas_brasil], ['Italia', faltas_italia], ['Espanha', faltas_espanha]] 

menor, maior = lista_faltas[0][1], lista_faltas[0][1]

lista_times_mais_faltas = []
lista_times_menos_faltas = []

for item in lista_faltas:
    if item[1] > maior:
        maior = item[1]
        lista_times_mais_faltas.append(item[0])
        
    if item[1] <= menor:
        menor = item[1]
        lista_times_menos_faltas.append(item[0])
        
#mostrando o total de faltas
print(f'Total de faltas = {soma}')

#mostrando os times que fizeram mais faltas
print('Times que fizeram mais faltas: ', lista_times_mais_faltas)

#mostrando os times que fizeram menos faltas
print('Times que fizeram menos faltas: ', lista_times_menos_faltas)