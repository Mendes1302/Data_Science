# LIBS
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# Function of prepare of dataset
def organizad_dataset(dataset):
    data = pd.DataFrame(dataset.data)
    features = list(dataset.feature_names)
    data.columns = features
    data['PRICE'] = boston.target
    return data


# Load and describe of data
boston = load_boston()
print(boston.DESCR)

# Call function of organization of data
data = organizad_dataset(boston)
print(data.head())

# Details of values
print(data.describe())

# Correlation between variables (raw)
print(data.corr())

# Correlation between variables (grafh)
fig, ax = plt.subplots(figsize=(15,15))
ax = sns.heatmap(data.corr(), annot= True)

# Datatype
print(data.info())


# Brief description of statistics [PRICE]
txt_price = f"""Mean: {data['PRICE'].mean()}
Median: {data['PRICE'].median()}
STD: {data['PRICE'].std()}"""

# Distribution of PRICE
print(txt_price)
fig, ax = plt.subplots(figsize = (10,5))
data['PRICE'].plot(kind = "hist", density = True)
data['PRICE'].plot(kind = "kde", color = 'red')
plt.xlim([0, 55])
plt.title('Distribution of PRICE')
plt.show()
fig, ax = plt.subplots(figsize = (10,5))
np.log(data['PRICE']).plot(kind = "hist", density = True)
np.log(data['PRICE']).plot(kind = "kde", color = 'red')
plt.xlim([0, 5])
plt.title('Distribution of PRICE with normalizing distribution')
plt.show()


# Brief description of statistics [LSTAT]
txt_lstat = f"""Mean: {data['LSTAT'].mean()}
Median: {data['LSTAT'].median()}
STD: {data['LSTAT'].std()}"""

# Distribution of LSTAT
print(txt_lstat)
fig, ax = plt.subplots(figsize = (10,5))
data['LSTAT'].plot(kind = "hist", density = True)
data['LSTAT'].plot(kind = "kde", color = 'red')
plt.xlim([0, 40])
plt.title('Distribution of LSTAT')
plt.show()
fig, ax = plt.subplots(figsize = (10,5))
np.log(data['LSTAT']).plot(kind = "hist", density = True)
np.log(data['LSTAT']).plot(kind = "kde", color = 'red')
plt.xlim([0, 5])
plt.title('Distribution of LSTAT with normalizing distribution')
plt.show()


# Brief description of statistics [RM]
txt_rm = f"""Mean: {data['RM'].mean()}
Median: {data['RM'].median()}
STD: {data['RM'].std()}"""

# Distribution of ROOM
print(txt_rm)
fig, ax = plt.subplots(figsize = (10,5))
ax.patch.set_facecolor('whitesmoke')
data['RM'].plot(kind = "hist", color = 'blue', density = True)
data['RM'].plot(kind = "kde", color = 'red')
plt.axvline(data['RM'].mean(), color='green', linestyle='dashed', linewidth=2)
plt.axvline(data['RM'].mean()+data['RM'].std(), color='black',  linewidth=2)
plt.axvline(data['RM'].mean()-data['RM'].std(), color='black',  linewidth=2)
plt.xlim([2, 10])
plt.title('Distribution of RM')
plt.show()

# Brief description of statistics [PTRATIO]
txt_ptratio = f"""Mean: {data['PTRATIO'].mean()}
Median: {data['PTRATIO'].median()}
STD: {data['PTRATIO'].std()}"""

# Distribution of STATUS
print(txt_rm)
fig, ax = plt.subplots(figsize = (10,5))
data['PTRATIO'].plot(kind = "hist", density = True)
data['PTRATIO'].plot(kind = "kde", color = 'red')
plt.xlim([10, 25])
plt.title('Distribution of PTRATIO')
plt.show()
fig, ax = plt.subplots(figsize = (10,5))
np.log(data['PTRATIO']).plot(kind = "hist", density = True)
np.log(data['PTRATIO']).plot(kind = "kde", color = 'red')
plt.xlim([2, 4])
plt.title('Distribution of PTRATIO with normalizing distribution')
plt.show()

# Correlation POSITIVE [RM]
plt.figure(figsize=(10,5))
plt.scatter(data['RM'], data['PRICE'])
plt.xlabel('RM')
plt.ylabel('PRICE')
plt.title('Quantos quartos por preço')
plt.show()

# Correlation NEGATIVE [LSTAT]
plt.figure(figsize=(10,5))
plt.scatter(data['LSTAT'], data['PRICE'])
plt.xlabel('LSTAT')
plt.ylabel('PRICE')
plt.title('Status do bairro por preço')
plt.show()

# Correlation NEGATIVE [PTRATIO]
plt.figure(figsize=(10,5))
plt.scatter(data['PTRATIO'], data['PRICE'])
plt.xlabel('PTRATIO')
plt.ylabel('PRICE')
plt.title('Escola/bairro por preço')
plt.show()

# Predict multi linear regression
x = data.iloc[:, [5,10, 12]].values
y = data['PRICE']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state =1)
print('Shape of x_train: ', x_train.shape)
print('Shape of x_test:  ', x_test.shape)
print()

regression = LinearRegression()
regression.fit(x_train, y_train)
print('y = a.x + b')
print('b: ', regression.intercept_)
print('a: ', regression.coef_)

print()
print('R² train: ', regression.score(x_train, y_train))
print('R² test:  ', regression.score(x_test, y_test))

print()
print('Mean:   ', data['PTRATIO'].mean())
print('Median: ', data['PTRATIO'].median())
print('STD:    ', data['PTRATIO'].std())

# Predict multi linear regression with normalizing distribution
x = np.log(data.iloc[:, [5,10, 12]].values)
y = data['PRICE']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state =1)
print('Shape of x_train: ', x_train.shape)
print('Shape of x_test:  ', x_test.shape)
print()

regression = LinearRegression()
regression.fit(x_train, y_train)
print('y = a.x + b')
print('b: ', regression.intercept_)
print('a: ', regression.coef_)

print()
print('R² train: ', regression.score(x_train, y_train))
print('R² test:  ', regression.score(x_test, y_test))

print()
print('Mean:   ', data['PTRATIO'].mean())
print('Median: ', data['PTRATIO'].median())
print('STD:    ', data['PTRATIO'].std())