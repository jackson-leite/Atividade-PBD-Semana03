"""2 Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um
programa que leia todos os tempos em segundos e os guarde em um dicionário, em que
a chave é o nome do corredor. Ao final diga de quem foi a melhor volta da prova e em
que volta; e ainda a classificação final em ordem (1o
 o campeão). O campeão é o que tem a menor média de tempos."""

num_corredores = 6
num_voltas = 10

i = 0

dicionario = {}
d = {}

#entrada de dados
while i < num_corredores:
    melhor_volta, menor_volta, soma, j, k = 0, 0, 0, 0, 0
    media = 0.0
    lista_tempos = []
    lista_aux = []
    nome = input(f'Informe o nome do {i+1}o corredor: ')
    
    while j < num_voltas:
        tempo = float(input(f'Informe o tempo da {j+1}a volta: '))
        lista_tempos.append(tempo)
        soma = soma + tempo        
        j += 1
            
    media = soma/num_voltas
    lista_aux = sorted(lista_tempos)
    menor_volta = lista_aux[0]
    
    while k < len(lista_tempos):
        if menor_volta == lista_tempos[k]:
            melhor_volta = k+1
            break
        k += 1
        
    #populando o dicionario com informaçoes fornecidas
    d[nome] = [media, menor_volta, melhor_volta]
    #dicionario[nome], dicionario['media'], dicionario['menor volta'], dicionario['melhor volta'] = lista_tempos, media, menor_volta, melhor_volta
    
    
    i += 1

#menor volta de todos
melhor_media = d[nome][1]
melhor_corredor = nome
i = 0

for corredor in d:
    
    while i < num_voltas:
        if d[corredor][0] < melhor_media:
            melhor_corredor = corredor
            
        else:
            pass
        i += 1

print('O melhor corredor foi '+ melhor_corredor + '. Que fez a menor volta:', d[melhor_corredor][1], '. Na volta:', d[melhor_corredor][2])

print('Classificação final:')
colocacao = 1

#invertendo os pares chave-valor
dic_m = {}
for n in d:
    m = d[n][0]   
    dic_m[m] = n
    
l = sorted(dic_m)

#mostrando as colocações agora com a média ordenada sendo a chave e o nome dos colocados, o valor
for item in l:
    
    print(f'{colocacao}o Lugar:', dic_m[item])
    colocacao += 1
