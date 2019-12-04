import numpy as np
import matplotlib.pyplot as plt
import csv
from random import *
leitura = open('./meu.txt','r')
read = leitura.readlines()
leitura.close()
lista = []
contador = [0]*25

with open('meu.txt', newline='') as csvfile:
    # o nome 'spamreader' abaixo é só exemplo, poderia ser qq. coisa
    spamreader = csv.reader(csvfile, delimiter='\t') # separe por vírgula

    # o módulo csv detectará novas linhas automaticamente
    for linha in spamreader:
        lista.append(linha)
#print(lista)

for i in range(len(read)):
    for j in range(25):
        #print('[',i+1,']','[',j+1,']',' = ',lista[i][j])
        if (j+1)==int(lista[i][j]):
            #print('ok')
            contador[j]=contador[j]+1
            #print(contador)
        else:
            continue
print('\nQuantidade de aparições dos números em',len(read)+1,'jogos!')
for j in range(25):
    print('{:2.0f}'.format(j+1),' = ','{:4.0f}'.format(contador[j]),'{:6.4f}'.format(contador[j]/len(read)))

jogo = []
while len(jogo) != 15:
    r = randint(1, 25)
    if r not in jogo:
        jogo.append(r)     
    jogo.sort()
print(jogo)

result = []
while len(result) != 15:
    r = randint(1, 25)
    if r not in result:
        result.append(r)
    result.sort()
print(result)

if jogo==result:
    print('igual')
else:
    print('diferente')


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    