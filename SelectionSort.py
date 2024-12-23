lista =[]
pivo = 0

with open('num.1000.4.in', 'r') as arquivo:
    linhas = arquivo.readlines()
    lista = [int(linha.strip()) for linha in linhas]
 
for i in range(len(lista)-1):
    menor_ind = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[menor_ind]:
            menor_ind = j
    (lista[i], lista[menor_ind]) = (lista[menor_ind], lista[i])
print(lista)

#Testes
#num.100000.1 - 481.764 seconds
#num.100000.2 - 497.996 seconds
#num.100000.3 - 578.146 seconds
#num.100000.4 - 630.275 seconds
#num.10000.1 - 5.422 seconds
#num.10000.2 - 4.473 seconds
#num.10000.3 - 4.72 seconds
#num.10000.4 - 5.614 seconds
#num.1000.1 - 0.147 seconds
#num.1000.2 - 0.152 seconds
#num.1000.3 - 0.146 seconds
#num.1000.4 - 0.15 seconds