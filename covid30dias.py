import numpy as np
import matplotlib.pyplot as plt

dados = []
mediamovel = []
cont=0
soma=0

with open("C:\\Users\\f0fp1107\Desktop\\covid30dias.txt") as f:
    for line in f:
        dados.append(float(line))

media = np.average(dados).round(2)
desv = np.std(dados).round(2)

print("A média de casos por dia é: ",media,"+-",desv)
for k in range(0,len(dados)):
    soma=soma+dados[k]
    cont = cont+1
    if(k>=6):
        mediamovel.append(soma/cont)

plt.plot(mediamovel)
plt.show()
