lista =[]
pivo = 0

with open('num.100000.4.in', 'r') as arquivo:
    linhas = arquivo.readlines()
    lista = [int(linha.strip()) for linha in linhas]

for i in range(1, len(lista)):
    pivo = lista[i]
    j = i-1
    while j >= 0 and lista[j] > pivo:
        lista[j+1]=lista[j]
        j = j-1
    lista[j+1] = pivo
print(lista)

#Testes
#num.100000.1 - 642.809 seconds
#num.100000.2 - 645.759 seconds
#num.100000.3 - 525.918 seconds
#num.100000.4 - 765.851 seconds
#num.10000.1 - 6.007 seconds
#num.10000.2 - 5.633 seconds
#num.10000.3 - 4.689 seconds
#num.10000.4 - 6.197 seconds
#num.1000.1 - 0.157 seconds
#num.1000.2 - 0.147 seconds
#num.1000.3 - 0.15 seconds
#num.1000.4 - 0.138 seconds