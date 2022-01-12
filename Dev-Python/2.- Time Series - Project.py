import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users/diegoaviles/Desktop/Data Analytics - Python/2.-Time Series Data Analysis/individual_stocks_5yr/'
company_list = ['AAPL_data.csv','GOOG_data.csv','MSFT_data.csv','AMZN_data.csv']
all_data = pd.DataFrame()
for file in company_list:
    current_df=pd.read_csv(path+'/'+file)
    all_data=pd.concat([all_data,current_df])
all_data.shape

#1 Se inicia desde la terminal y nos debe arrojar (4752,7)

all_data.head()
all_data.dtypes

all_data['date']=pd.to_datetime(all_data['date'])
tech_list=all_data['Name'].unique()

plt.figure(figsize=(20,12))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df=all_data[all_data['Name']==company]
    plt.plot(df['date'],df['close'])
    plt.xticks(rotation='vertical')
    plt.title(company)

#Con estas gráficas se puede ver el cierre de stock por cada año.

#2 Analizar el volumen total de acciones que se negocian cada día.

import plotly.express as px

for company in tech_list:
    df=all_data[all_data['Name']==company]
    fig=px.line(df,x='date',y='volume',title=company)
    fig.show()

#Pregunta 1: Analizar cambios de precios en stock.

df=pd.read_csv('/Users/diegoaviles/Desktop/Data Analytics - Python/2.-Time Series Data Analysis/individual_stocks_5yr/AAPL_data.csv')
df.head()
df['Daily_Price_change']=df['close']-df['open']
df.head()
df['1day % return']=((df['close']-df['open'])/df['close'])*100
df.head()

fig=px.line(df,x='date',y='1day % return',title=company)
fig.show()

df2=df.copy()
df2.dtypes
df2['date']=pd.to_datetime(df2['date'])
df2.set_index('date',inplace=True)
df2.head()
df2['2013-02-08':'2013-02-14']
df2['close'].resample('M').mean().plot()

#Función resample es un método de conveniencia para conversión de frecuencia y remuestreo de series de tiempo.
df2['close'].resample('Y').mean().plot(kind='bar')
df2['close'].resample('D').mean()

# Pregunta 2: Analizar si los precios de las acciones de las empresas tecnológicas están correlacionados o no.

aapl=pd.read_csv('/Users/diegoaviles/Desktop/Data Analytics - Python/2.-Time Series Data Analysis/individual_stocks_5yr/AAPL_data.csv')
aapl.head()
amzn=pd.read_csv('/Users/diegoaviles/Desktop/Data Analytics - Python/2.-Time Series Data Analysis/individual_stocks_5yr/AMZN_data.csv')
amzn.head()
msft=pd.read_csv('/Users/diegoaviles/Desktop/Data Analytics - Python/2.-Time Series Data Analysis/individual_stocks_5yr/MSFT_data.csv')
msft.head()
goog=pd.read_csv('/Users/diegoaviles/Desktop/Data Analytics - Python/2.-Time Series Data Analysis/individual_stocks_5yr/GOOG_data.csv')
goog.head()

close = pd.DataFrame()
close['aapl'] = aapl['close']
close['goog'] = goog['close']
close['amzn'] = amzn['close']
close['msft'] = msft['close']

close.head()

import seaborn as sns
sns.pairplot(data=close)

sns.heatmap(close.corr(),annot=True)

#Pregunta 3: Analice el rendimiento diario de cada acción y cómo se correlacionan.

aapl.head()
data=pd.DataFrame()
data['aapl_change']=((aapl['close']-aapl['open'])/aapl['close'])*100
data['goog_change']=((goog['close']-goog['open'])/goog['close'])*100
data['amzn_change']=((amzn['close']-amzn['open'])/amzn['close'])*100
data['msft_change']=((msft['close']-msft['open'])/msft['close'])*100
data.head()

sns.pairplot(data=data)
sns.heatmap(data.corr(),annot=True)

#Pregunta 4: Analizar riesgo para empresas Amazon,Google,Microsoft y Apple.

sns.distplot(data['aapl_change'])
data['aapl_change'].std()
data['aapl_change'].quantile(0.1)
data.describe().T
