# -*- coding: utf-8 -*-
"""Imersao_dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11hUX4kVtP3llYH7c83fiSCeCtP8MGTm0
"""

import pandas as pd
import matplotlib.pyplot as plt

url_date = "https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_experimentos.zip?raw=true"
dados = pd.read_csv(url_date, compression= 'zip')

"""#AULA 1: Análise de dados, python, pandas e novos fármacos

"""

dados

"""## Desafio 2: 5 ultimos"""

dados.tail()

"""## Desafio 3: % de com droga e com controle (como eu fiz)



"""

com_droga = (list(dados['tratamento'].value_counts())[0]/dados['tratamento'].count())*100
com_controle = (list(dados['tratamento'].value_counts())[1]/dados['tratamento'].count())*100

print(f"Com droga {com_droga:.2f} %")
print(f"Com controle {com_controle:.2f} %")

"""##eles"""

dados['tratamento'].value_counts(normalize=True)

"""## Desafio 4: Quant. de classes"""

print(len(dados['droga'].unique()))
dados['droga'].value_counts().count()

dados['tratamento'].value_counts().plot(kind= 'pie')
plt.title('TRATAMENTO')
plt.show()

dados['dose'].value_counts().plot(kind='pie')
plt.title('DOSE')
plt.show()

dados['tempo'].value_counts(normalize=True)

"""### Desafio 7: Titulo no grafico"""

dados['tempo'].value_counts().plot(kind='pie')
plt.title('TEMPO')
plt.show()

dados['tempo'].value_counts().plot(kind='bar')
plt.title('TEMPO')
plt.show()

"""## Mascara"""

dados[dados['g-0']> 0]  # remove valor < 0

"""## Desafio 5: Nomear colunas"""

new = list()
old = list()

for dt in dados.columns:
    if "-" in dt:
        old.append(dt)
        new.append(dt.replace("-", ""))
    else:
        old.append(dt)
        new.append(dt)
dados.columns = new

dados.head()

map = {'droga': 'composto'}
dados.rename(columns=map, inplace=True)
dados

cod_composto = dados['composto'].value_counts().index[:5]

"""## VAR out usar @"""

dados.query('composto in @cod_composto')

import seaborn as sns

plt.figure(figsize=(10, 8))
sns.set()
ax = sns.countplot(x = 'composto', data=dados.query('composto in @cod_composto'),  order=cod_composto)
ax.set(xlabel='Nome dos compostos', ylabel='Quantidade de ocorrẽncia')
ax.set_title("Top 5 compostos", fontsize=30)
plt.show()

print("Total", len(dados['g0'].unique()))
print("Max", dados['g0'].min())
print("Min", dados['g0'].max())

"""# AULA 2: Estatísticas, visualização de dados e distribuições"""

dados['g0'].describe()

dados['g0'].hist(bins= 80)

dados['g19'].hist(bins= 80)

dados

dados.loc[:,'g0':'g771'].describe()

dados.loc[:,'g0':'g771'].describe().T['mean'].hist(bins=50)

dados.loc[:,'g0':'g771'].describe().T['min'].hist(bins=50)

dados.loc[:,'g0':'g771'].describe().T['max'].hist(bins=50)

dados.loc[:,'g0':'g771'].describe().T['std'].hist(bins=50)

dados.loc[:,'g0':'g771'].describe().T['50%'].hist(bins=50)

sns.boxplot(x = 'g0', data=dados)

sns.boxplot(x = 'g0', y = 'tratamento', data=dados)

plt.figure(figsize=(10,10))
sns.boxplot(x = 'tratamento', y = 'g0', data=dados)

"""#AULA 3: Correlações, causalidade e relações entre genes."""

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], normalize='index')

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], normalize='index', values=dados['g0'], aggfunc='mean')

"""## Desafio 2: Normalizar columns"""

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], normalize='columns', values=dados['g0'], aggfunc='mean')

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], values=dados['g0'], aggfunc='mean')

"""## Desafio 03: Explorar outros agregadores

### STD
"""

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], values=dados['g0'], aggfunc='std')

"""###MAX"""

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], values=dados['g0'], aggfunc='max')

"""###MIN"""

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], values=dados['g0'], aggfunc='min')

"""### MEDIAN"""

pd.crosstab([dados['dose'], dados['tempo']], dados['tratamento'], values=dados['g0'], aggfunc='median')

"""### Desafio 04: melt()"""

dados.melt(id_vars= ['composto'], value_vars = ['g0'])

plt.figure(figsize=(10, 10))
sns.scatterplot(x = 'g0', y = 'g3',  data=dados)

plt.figure(figsize=(10, 10))
sns.scatterplot(x = 'g0', y = 'g8',  data=dados)

sns.lmplot(x = 'g0', y = 'g8',  data=dados, line_kws={'color': 'black'})

sns.lmplot(x = 'g0', y = 'g8',  data=dados, line_kws={'color': 'black'}, col='tratamento')

sns.lmplot(x = 'g0', y = 'g8',  data=dados, line_kws={'color': 'black'}, col='dose')

sns.lmplot(x = 'g0', y = 'g8',  data=dados, line_kws={'color': 'black'}, col='tempo')

sns.lmplot(x = 'g0', y = 'g8',  data=dados, line_kws={'color': 'black'}, col='tratamento', row='tempo')

plt.figure(figsize=(10, 10))
sns.scatterplot(x = 'g0', y = 'c0',  data=dados)

dados[['g0', 'g1']]

dados.loc[:,'g0':'g771'].corr()

import numpy as np

corr = dados.loc[:,'g0':'g50'].corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

f, ax = plt.subplots(figsize=(11, 9))

cmap = sns.diverging_palette(230, 20, as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

import numpy as np

corr = dados.loc[:,'c0':'c50'].corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

f, ax = plt.subplots(figsize=(11, 9))

cmap = sns.diverging_palette(230, 20, as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

dados

cor_cg = dados[list(dados.loc[:,'g0':'g99']) + list(dados.loc[:,'c0':'c99']) ].corr()

mask = np.triu(np.ones_like(cor_cg, dtype=bool))

f, ax = plt.subplots(figsize=(20, 15))

cmap = sns.diverging_palette(230, 20, as_cmap=True)

sns.heatmap(cor_cg, mask=mask, cmap=cmap, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

"""#AULA 4: Merge de dados e análise de resultados"""

dados_resultados = pd.read_csv('https://github.com/alura-cursos/imersaodados3/blob/main/dados/dados_resultados.csv?raw=true')
dados_resultados.head()

dados_resultados['antibiotic'].unique()

dados_resultados.info()

contagem_moa = dados_resultados.select_dtypes('int64').sum().sort_values(ascending=False)
contagem_moa

contagem_moa.sum()

"""##Desafio 01: Top 10 inhibitor"""

count = 0
key_inhibitor  = list()

for key in contagem_moa.keys():
    if count < 10 and '_inhibitor' in str(key):
        key_inhibitor.append(key)
        count += 1
        print(count, key, contagem_moa[key])

dados_resultados['11-beta-hsd1_inhibitor'].sum()

dados_resultados.drop('id', axis=1).sum(axis=1)

dados_resultados.head()

dados_resultados['n_moa'] = dados_resultados.drop('id', axis=1).sum(axis=1)
dados_resultados['ativo_moa'] = (dados_resultados['n_moa']!=0)
dados_resultados.head()

dados_merge = pd.merge(dados, dados_resultados[['id', 'n_moa', 'ativo_moa']], on='id')
dados_merge.head()

dados_merge.query('tratamento == "com_controle"')['ativo_moa'].value_counts()

dados_merge.query('tratamento == "com_droga"')['ativo_moa'].value_counts()

composto_principal = dados_merge['composto'].value_counts().index[:10]
plt.figure(figsize=(12,10))
sns.boxplot(x = 'composto', y ='g0', data=dados_merge.query('composto in @composto_principal'), hue='ativo_moa')

dados_merge

"""## Desafio 2: Criar coluna eh_controle


"""

dados_merge['eh_controle'] = (dados_merge['tratamento']=='com_controle')
dados_merge.head()

"""## Desafio 3: Criar colunas dos times (24, 48, 72)"""

dados_merge['time_24'] = (dados_merge['tempo']== 24)
dados_merge['time_48'] = (dados_merge['tempo']== 48)
dados_merge['time_72'] = (dados_merge['tempo']== 72)
dados_merge.head()

"""# AULA 5: Machine Learning, Sci-kit learning e desafios envolvidos."""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

x = dados_merge.select_dtypes('float64')
y = dados_merge['ativo_moa']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, stratify=y, random_state=376)

modelo_rlogistica = LogisticRegression(max_iter=1000)
modelo_rlogistica.fit(x_train, y_train)

print("Accuracy: {:.2f}%".format(modelo_rlogistica.score(x_test, y_test)*100))

from sklearn.metrics import accuracy_score
from sklearn.dummy import DummyClassifier

modelo_dummy = DummyClassifier('most_frequent')
modelo_dummy.fit(x_train, y_train)
previsao_dummy = modelo_dummy.predict(x_test)
print("Accuracy: {:.2f}%".format(accuracy_score(y_test, previsao_dummy)*100))

from sklearn.tree import DecisionTreeClassifier

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, stratify=y, random_state=376)

modelo_Tree = DecisionTreeClassifier(max_depth = 3)
modelo_Tree.fit(x_train, y_train)
print("Accuracy: {:.2f}%".format(modelo_Tree.score(x_test, y_test)*100))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, stratify=y, random_state=376)

teste = list()
treino = list()
for i in range(1, 15):
    modelo_Tree = DecisionTreeClassifier(max_depth = i)
    modelo_Tree.fit(x_train, y_train)
    teste.append(modelo_Tree.score(x_test, y_test))
    treino.append(modelo_Tree.score(x_train, y_train))

"""## Overfit"""

sns.lineplot(x= range(1, 15), y = teste, label='Teste')
sns.lineplot(x= range(1, 15), y = treino, label='Treino')

pd.get_dummies(dados_merge, columns=['tratamento', 'dose'])

from sklearn.ensemble import RandomForestClassifier

x = dados_merge.drop(['id', 'n_moa', 'ativo_moa', 'composto'], axis=1)
x = pd.get_dummies(x, columns=['tratamento', 'dose'])
y = dados_merge['ativo_moa']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, stratify=y, random_state=376)

modelo_RandonForest = RandomForestClassifier()
modelo_RandonForest.fit(x_train, y_train)
print("Accuracy: {:.2f}%".format(modelo_RandonForest.score(x_test, y_test)*100))