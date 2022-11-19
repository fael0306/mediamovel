import statistics as lr
import numpy as np
import matplotlib.pyplot as plt

dados = []
mediamovel = []
x = []
cont=0
soma=0

# Rodando o arquivo para incluir os dados no vetor
with open("C:\\Users\\f0fp1107\Desktop\\covid60dias.txt") as f:
    for line in f:
        dados.append(float(line))

# Calculando a média e o desvio padrão com 2 casas decimais
media = np.average(dados).round(2)
desv = np.std(dados).round(2)

# Salvando a média num arquivo
arq = open("media.txt","a")
arq.write('A média de casos por dia é: ')
arq.write(str(media))
arq.write("+-")
arq.write(str(desv))
arq.close()

# Calculando as médias móveis e incluindo no vetor
tam = int(np.sqrt(len(dados)))
for k in range(tam,len(dados)+1):
    if k>=tam:
        for i in range(k-tam,k):
            soma = soma+dados[i]
        media = soma/tam
        mediamovel.append(media)    
    soma = 0

# Limitando os valores de x inferiormente para começar a partir de onde a média móvel passou a ser calculada
for k in range(tam,len(dados)+1):
    x.append(k)

# Achando coeficientes da regressão linear
a1,a2=lr.linear_regression(x,mediamovel)

# Limitando o x da reta de regressão
xi = np.linspace(tam,120)

# Plotando a reta usando os coeficientes
plt.plot(xi,a1*xi+a2)

# Plotando o gráfico da média móvel
plt.plot(x,mediamovel)

# Salvando uma imagem do gráfico gerado
plt.savefig("grafico.png")

# Caso seja necessário mostrar o gráfico, é só usar plt.show()