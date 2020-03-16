"""1 Espião: Escreva uma função que receba uma lista de
inteiros e retorne True se contém um 007 em ordem, mesmo
que não contínuo. Exemplo:
espiao([1,2,4,0,0,7,5]) --> True
espiao([1,0,2,4,0,5,7]) --> True
espiao([1,7,2,4,0,5,0]) --> False"""

def espiao(lista):
    i, pos, ocorrencia_zero = 0, 0, 0
    
    while i < len(lista):
        
        if lista[i] == 0:
            ocorrencia_zero += 1
            if ocorrencia_zero == 2:
                pos = i
                if 7 in lista[pos:]:
                    return True
    
        i += 1
            
    return False


lista1 = [1,2,4,0,0,7,5]
lista2 = [1,0,2,4,0,5,7]
lista3 = [1,7,2,4,0,5,0]


print(espiao(lista1))
print(espiao(lista2))
print(espiao(lista3))