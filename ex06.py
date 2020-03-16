"""2 Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros, houver
em alguma posição da lista um 3 do lado de outro 3. Exemplo:
tem_33([1,3,3]) --> True
tem_33([1,3,1,3]) --> False
tem_33([3,1,3]) --> False """


def tem_33(lista):
    if len(lista) > 1:
        i = 0  
        while i < len(lista) - 1:
            if lista[i] == 3 and lista[i+1] == 3:
                return True  

            else:
                i = i + 1    
    return False
    
lista_teste1 = []
lista_teste2 = [1]
lista_teste3 = [1,2]
lista_teste4 = [1,3]
lista_teste5 = [3,3]
lista_teste6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_teste7 = [1, 3, 3, 4, 3, 6, 7, 8, 9]
lista_teste8 = [1, 2, 3, 4, 3, 3, 7, 8, 9]
lista_teste9 = [1, 2, 3, 4, 5, 6, 7, 3, 3]

print(tem_33(lista_teste1))
print(tem_33(lista_teste2))
print(tem_33(lista_teste3))
print(tem_33(lista_teste4))
print(tem_33(lista_teste5))
print(tem_33(lista_teste6))
print(tem_33(lista_teste7))
print(tem_33(lista_teste8))
print(tem_33(lista_teste9))