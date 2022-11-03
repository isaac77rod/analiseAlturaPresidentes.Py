from gettext import npgettext
import numpy as npgettext
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# -> o código abaixo lê a minha planilha ou csv e aplica a variável tabela1.
tabela1 = pd.read_csv(r"C:\Users\isaac\Documents\president_heights.csv")
print(tabela1)  # -> mostra a tabela1(Que é minha b a s e  de dados)

# -> digo que o conteúdo da coluna "height(cm)" na minha csv vai estar na varviavel height
altura = npgettext.array(tabela1["height(cm)"])

print(altura)  # -> mostro as alturas

print("Media das alturas =", altura.mean())
print("Desvio padrao das alturas =", altura.std())
print("Altura minima =", altura.min())
print("Altura Maxima =", altura.max())

plt.hist(altura)  # -> gráfico historograma da altura.
plt.title("Distruição de Altura dos Presidentes Americanos")  # -> título do gráfico
plt.xlabel("Altura(cm)")  # eixo horizonte == altura
plt.ylabel("Quantidade")  # eixo vertical == quantidade
plt.show()  # mostrar
