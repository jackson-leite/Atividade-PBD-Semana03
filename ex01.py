"""1 Faça um programa que decide se duas listas são iguais. Duas listas são iguais se
possuem os mesmos valores e na mesma ordem."""

lista1 = [1, 2, 3, 4, 5, 6]

lista2 = [1, 2, 3, 5, 5, 6]

if(len(lista1) != len(lista2)):
    diferente = True

else:
    i = 0
    for item in lista2:
        if(lista1[i] != lista2[i]):
            diferente = True
            break
        else:
            diferente = False
        i += 1
        
print('Listas diferentes' if diferente else 'Listas iguais')