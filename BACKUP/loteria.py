from random import *
#-------Fazer as estatísticas dos jogos ---------------------------------------
leitura = open('./DATA/meu_estatistica.txt','r')
read = leitura.readlines()
leitura.close()
lista_est = []
contador = [0]*25
with open('./DATA/meu_estatistica.txt','r') as f:
    for line in f:
        lista_est.append([int(x) for x in line.split()])
               
for i in range(len(read)):
    for j in range(25):
        if (j+1)==int(lista_est[i][j]):
            contador[j]=contador[j]+1
#------------ Fazer contagem dos últimos 3 sorteios----------------------------
res_3 = [0]*25
conta_3 = [0]*25
for q in range(len(read)-3,len(read)):
	for w in range(25):
		res_3[w] = int(lista_est[q][w]/(w+1))
		conta_3[w]+=int((res_3[w]))
#------------ Fazer contagem 2 a 6 últimos sorteios----------------------------
res_25 = [0]*25
conta_25 = [0]*25
for q in range(len(read)-6,len(read)-1):
	for w in range(25):
		res_25[w] = int(lista_est[q][w]/(w+1))
		conta_25[w]+=int((res_25[w]))
#------------ Fazer contagem 4 a 7 últimos sorteios----------------------------
res_47 = [0]*25
conta_47 = [0]*25
for q in range(len(read)-8,len(read)-3):
	for w in range(25):
		#if 0!=lista_est[q][w]:
		res_47[w] = int(lista_est[q][w]/(w+1))
		conta_47[w]+=int((res_47[w]))
#------------ Fazer contagem últimos 6 sorteios----------------------------
res_6 = [0]*25
conta_6 = [0]*25
for q in range(len(read)-6,len(read)):
	for w in range(25):
		#if 0!=lista_est[q][w]:
		res_6[w] = int(lista_est[q][w]/(w+1))
		conta_6[w]+=int((res_6[w]))
#----------- Sorteio do jogo ----------------------------------------------
#print(conta_3)
#print(conta_25)
jogo1 = []
while len(jogo1) != 15:
	r1 = randint(1,25)
	if conta_3[r1-1]<3 and conta_25[r1-1]<5:
		if r1 not in jogo1:
			jogo1.append(r1)
	r2 = randint(1,25)
	if conta_47[r2-1]<3:
		if r2 not in jogo1:
			jogo1.append(r2)
	jogo1.sort()
jogo2 = []
while len(jogo2) != 15:
	r6 = randint(1,25)
	if conta_6[r6-1]<5:
		if r6 not in jogo2:
			jogo2.append(r6)
	jogo2.sort()
jogo = jogo1
print('Os jogos sugeridos são: \n\n',jogo,'\n',jogo2)
#------------ Conferir se o jogo sorteado já saiu -----------------------------
lista = []
with open('./DATA/meu_ordenado.txt','r') as n:
    for linen in n:
        lista.append([int(x) for x in linen.split()])
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
    numero.sort()
    if len(numero)==15:
        print('Já saiu essa combinação com o prêmio máximo!')
    if len(numero)==11:
        conta_11+=1
        conta11.append(conta_11)
    if len(numero)==12:
        conta_12 +=1
        conta12.append(conta_12)
    if len(numero)==13:
        conta_13 +=1
        conta13.append(conta_13)
    if len(numero)==14:
        conta_14 +=1
        conta14.append(conta_14)
    if len(numero)==15:
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
    numero2.sort()
    if len(numero2)==15:
        print('Já saiu essa combinação com o prêmio máximo!')
    if len(numero2)==11:
        conta_11_+=1
        conta11_.append(conta_11_)
    if len(numero2)==12:
        conta_12_ +=1
        conta12_.append(conta_12_)
    if len(numero2)==13:
        conta_13_ +=1
        conta13_.append(conta_13_)
    if len(numero2)==14:
        conta_14_ +=1
        conta14_.append(conta_14_)
    if len(numero2)==15:
        conta_15_ +=1
        conta15_.append(conta_15_)
print('11 pontos: ',len(conta11_))
print('12 pontos: ',len(conta12_))
print('13 pontos: ',len(conta13_))
print('14 pontos: ',len(conta14_))
print('15 pontos: ',len(conta15_))

input('\n\n\nDigite qualquer tecla para sair!')