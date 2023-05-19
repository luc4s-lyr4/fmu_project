#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando biblioteca para tratamento dos dados:
import pandas as pd


# In[2]:


# Importando o arquivo csv:
url = ('C:/Users/User/Documents/projeto_fmu/full_data.csv')
df = pd.read_csv(url, low_memory=False)


# In[3]:


# Imprimindo dataframe:
df


# In[4]:


# Verificando as informações dos dados que iremos utilizar:
df.info()


# In[5]:


# Conversão de alguns dados para o tipo ideal que será utilizado para análise:
date_col = pd.DatetimeIndex(df['Data de cadastro'])

df['Ano'] = date_col.year
df['Mês'] = date_col.month
df['Dia'] = date_col.day

df['Data de cadastro'] = pd.to_datetime(df['Data de cadastro']) 

df.info()


# In[6]:


# Renomeando algumas colunas para facilitar a análise:
df = df.rename(columns={'sl_quantidade_vitimas':'Vítimas', 'Data de cadastro':'Data', 
                  })


# In[7]:


df.head(2)


# In[8]:


# Identificando quantos valores nulos temos na base de dados:
df.isnull().sum()


# In[9]:


# Verificando em percentual a quantidade de dados nulos de cada coluna:
df.isnull().sum()/df.shape[0]*100


# In[10]:


df.head(1)


# In[11]:


# Criando uma cópia da base de dados e mantendo a versão original caso precise buscar alguma informação:
df2 = df.copy()
df2.head(2)


# In[12]:


# Removendo colunas com % maior que 20 para não prejudicar na análise de dados:
df2.drop(["Profissão da vítima",
         "Grau de instrução da vítima", 
         "Religião da vítima", 
         "Etnia da vítima", 
         "Faixa de renda da vítima", 
         "Grau de instrução do suspeito", 
         "Religião do suspeito", 
         "Suspeito Etnia", 
         "Faixa de renda do suspeito"], axis=1, inplace=True)


# In[13]:


# Removendo colunas que não serão utilizadas na análise:
df2.drop(["Grupo vulnerável", "Motivação", "Sexo da vítima", "UF da vítima", "Natureza Jurídica do Suspeito", 
         "Sexo do suspeito", "UF do suspeito", "Violacao", "Profissão do suspeito"], axis=1, inplace=True)


# In[14]:


# Verificando a conversão da coluna data de cadastro em data:
df2.info()


# In[15]:


# Conferindo o novo formato da base de dados:
df2.head(5)


# In[16]:


# Salvando em csv pois iremos utilizar a base no Datastudio:
df2.to_csv('new_data_format.csv', index=False)

