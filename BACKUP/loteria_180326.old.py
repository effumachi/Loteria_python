import numpy as np
import matplotlib.pyplot as plt
from random import *
leitura = open('./DATA/meu_estatistica.txt','r')
read = leitura.readlines()
leitura.close()
#-------Fazer as estatísticas dos jogos ---------------------------------------
lista_est = []
contador = [0]*25
with open('./DATA/meu_estatistica.txt','r') as f:
    for line in f:
        lista_est.append([int(x) for x in line.split()])
               
for i in range(len(read)):
    for j in range(25):
        #print('[',i+1,']','[',j+1,']',' = ',lista[i][j])
        if (j+1)==int(lista_est[i][j]):
            #print('ok')
            contador[j]=contador[j]+1
            #print(contador)        
#print('\nQuantidade de aparições dos números em',len(read)+1,'jogos!')
#for j in range(25):
#    print('{:2.0f}'.format(j+1),' = ','{:4.0f}'.format(contador[j]),'{:6.4f}'.format(contador[j]/len(read)))
#------------ Fazer contagem dos últimos 3 sorteios----------------------------
res_3 = [0]*25
conta_3 = [0]*25
for q in range(len(read)-3,len(read)):
	for w in range(25):
		#if 0!=lista_est[q][w]:
		res_3[w] = int(lista_est[q][w]/(w+1))
		conta_3[w]+=int((res_3[w]))
#print(conta_3)
#for q in range(25):
#	print('#',q+1,'\t{:2.0f}'.format(conta_ant[q]))
#------------ Fazer contagem 4 a 7 últimos sorteios----------------------------
res_47 = [0]*25
conta_47 = [0]*25
for q in range(len(read)-7,len(read)-3):
	for w in range(25):
		#if 0!=lista_est[q][w]:
		res_47[w] = int(lista_est[q][w]/(w+1))
		conta_47[w]+=int((res_47[w]))
#print(conta_47)
#for q in range(25):
#	print('#',q+1,'\t{:2.0f}'.format(conta_ant[q]))
#------------ Fazer contagem últimos 6 sorteios----------------------------
res_6 = [0]*25
conta_6 = [0]*25
for q in range(len(read)-6,len(read)):
	for w in range(25):
		#if 0!=lista_est[q][w]:
		res_6[w] = int(lista_est[q][w]/(w+1))
		conta_6[w]+=int((res_6[w]))
#print(conta_6)
#for q in range(25):
#	print('#',q+1,'\t{:2.0f}'.format(conta_ant[q]))
#----------- Jogos realizados ---------------------------------------------
#jogos_feitos = open('./DATA/meu_feitos.txt','r')
#read_feitos = jogos_feitos.readlines()
#jogos_feitos.close()
#lista_feitos = []
#contador = [0]*15
#with open('./DATA/meu_feitos.txt','r') as f:
#    for line in f:
#        lista_feitos.append([int(x) for x in line.split()])
               
#for i in range(len(read_feitos)):
#    for j in range(15):
#        print('[',i+1,']','[',j+1,']',' = ',lista_feitos[i][j])       
#----------- Sorteio do jogo ----------------------------------------------
jogo1 = []
while len(jogo1) != 15:
	r1 = randint(1,25)
	if conta_3[r1-1]<5:
		if r1 not in jogo1:
			jogo1.append(r1)
	r2 = randint(1,25)
	if conta_47[r2-1]<4:
		if r2 not in jogo1:
			jogo1.append(r2)
	jogo1.sort()
#print(jogo1)
jogo2 = []
while len(jogo2) != 15:
	r6 = randint(1,25)
	if conta_6[r6-1]<5:
		if r6 not in jogo2:
			jogo2.append(r6)
	jogo2.sort()
#print(jogo2)
jogo = jogo1
#jogo = []
#while len(jogo) != 15:
#    r = randint(1, 25)
#    if r not in jogo:
#        jogo.append(r)     
#    jogo.sort()
#print(lista)
print('Os jogos sugeridos são: \n\n',jogo,'\n',jogo2)
#------------ Conferir se o jogo sorteado já saiu -----------------------------
lista = []
with open('./DATA/meu_ordenado.txt','r') as n:
    for linen in n:
        lista.append([int(x) for x in linen.split()])
#linha_res='Inédito'
#for i in range(len(lista)):
#    if (jogo[0] == lista[i][0]) and (jogo[1] == lista[i][1]) and (jogo[2] == lista[i][2]) and (jogo[3] == lista[i][3]) and (jogo[4] == lista[i][4]) and (jogo[5] == lista[i][5]) and (jogo[6] == lista[i][6]) and (jogo[7] == lista[i][7]) and (jogo[8] == lista[i][8]) and (jogo[9] == lista[i][9]) and (jogo[10] == lista[i][10]) and (jogo[11] == lista[i][11]) and (jogo[12] == lista[i][12]) and (jogo[13] == lista[i][13]) and (jogo[14] == lista[i][14]):
#        resultado = "ok"
#        linha_res = i+1
#    else:
#        inedito = 'inedito'
#print('Concurso de aparição: '+linha_res)
#--------------- Fim da conferência
#--------------- Conferir a quantidade de numeros em cada jogo 1----------------
print('\nPara o jogo 1, tem-se a quantidade de jogos com premios:\nBaseado nos', len(read),'jogos\n')
#jogo = [2,4,5,6,8,9,10,11,12,14,16,17,18,21,23]
conta11 = []
conta_11 = 0
conta12 = []
conta_12 = 0
conta13 = []
conta_13 = 0
conta14 = []
conta_14 = 0
conta15 = []
conta_15 = 0
for i in range(len(lista)):
    numero = []
    for j in range(15):
        for k in range(15):
            if jogo[k]==lista[i][j]:
                numero.append(jogo[k])
                #print(i,j+1,jogo[k],lista[j][k])
    numero.sort()
    #if len(numero)>10:
    #    print(numero)
    if len(numero)==15:
        print('Já saiu essa combinação com o prêmio máximo!')
    #    print(numero)
    if len(numero)==11:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_11+=1
        conta11.append(conta_11)
    #    print(numero)
    if len(numero)==12:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_12 +=1
        conta12.append(conta_12)
    #    print(numero)
    if len(numero)==13:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_13 +=1
        conta13.append(conta_13)
    #    print(numero)
    if len(numero)==14:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_14 +=1
        conta14.append(conta_14)
    #    print(numero)
    if len(numero)==15:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_15 +=1
        conta15.append(conta_15)
print('11 pontos: ',len(conta11))
print('12 pontos: ',len(conta12))
print('13 pontos: ',len(conta13))
print('14 pontos: ',len(conta14))
print('15 pontos: ',len(conta15))
#--------------- Conferir a quantidade de numeros em cada jogo 2----------------
print('\nPara o jogo 2, tem-se a quantidade de jogos com premios:\n')
#jogo = [2,	3,	5,	6,	9,	10,	11,	13,	14,	16,	18,	20,	23,	24,	25]
conta11_ = []
conta_11_ = 0
conta12_ = []
conta_12_ = 0
conta13_ = []
conta_13_ = 0
conta14_ = []
conta_14_ = 0
conta15_ = []
conta_15_ = 0
for i in range(len(lista)):
    numero2 = []
    for j in range(15):
        for k in range(15):
            if jogo2[k]==lista[i][j]:
                numero2.append(jogo2[k])
                #print(i,j+1,jogo[k],lista[j][k])
    numero2.sort()
    #if len(numero)>10:
    #    print(numero)
    if len(numero2)==15:
        print('Já saiu essa combinação com o prêmio máximo!')
    #    print(numero)
    if len(numero2)==11:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_11_+=1
        conta11_.append(conta_11_)
    #    print(numero)
    if len(numero2)==12:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_12_ +=1
        conta12_.append(conta_12_)
    #    print(numero)
    if len(numero2)==13:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_13_ +=1
        conta13_.append(conta_13_)
    #    print(numero)
    if len(numero2)==14:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_14_ +=1
        conta14_.append(conta_14_)
    #    print(numero)
    if len(numero2)==15:
        #print('Concurso:',i+1,numero,'# elementos',len(numero))
        conta_15_ +=1
        conta15_.append(conta_15_)
print('11 pontos: ',len(conta11_))
print('12 pontos: ',len(conta12_))
print('13 pontos: ',len(conta13_))
print('14 pontos: ',len(conta14_))
print('15 pontos: ',len(conta15_))

input('\n\n\nDigite qualquer tecla para sair!')