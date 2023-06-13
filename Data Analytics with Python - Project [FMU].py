#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


url = ('C:/Users/DELL/Documents/Projeto FMU/format.1 - Página2.csv')
df = pd.read_csv(url)


# In[3]:


df['sl_quantidade_vitimas'] = df['sl_quantidade_vitimas'].replace('NÃO SOUBE INFORMAR', 0)
df['sl_quantidade_vitimas'] = df['sl_quantidade_vitimas'].astype(float)
df['sl_quantidade_vitimas'] = df['sl_quantidade_vitimas'].astype(int)


# In[4]:


df.dtypes


# In[5]:


df.drop(['Religião do suspeito', 'Raça\Cor do suspeito', 'Suspeito Etnia', 'Violacao'], axis=1, inplace=True)


# In[6]:


df.head()


# In[7]:


df2 = df


# In[8]:


df2 = df2.drop(['Faixa de renda do suspeito', 'Grau de instrução do suspeito', 'UF do suspeito', 'Sexo do suspeito', 'Natureza Jurídica do Suspeito',
         'Faixa de renda da vítima', 'Etnia da vítima', 'Profissão da vítima',
               'UF da vítima', 'Profissão do suspeito', 'Religião da vítima', 'Grau de instrução da vítima',
               'Profissão da vítima', 'UF da vítima', 'Orientação sexual da vítima'], axis=1, inplace=False)


# In[9]:


df2.select_dtypes(include='object').describe()


# In[10]:


df2['Canal de atendimento'].unique()


# In[11]:


df2['id_canais'] = df2['Canal de atendimento'].replace({'TELEFÔNICO': 0, 'TELEGRAM':1, 'WEBCHAT':2, 'WHATSAPP':3,
                                                       'E-MAIL':4, 'MOBILE DH':5, 'MOBILE SABE':6,
                                                       'PORTAL':7, 'APLICATIVO':8, 'PRESENCIAL':9, 'MOBILE GDF':10})


# In[12]:


df3 = df2[['id_canais', 'Canal de atendimento', 'sl_quantidade_vitimas']]


# In[13]:


df3


# In[14]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[15]:


sns.set_style("white")
plt.figure(figsize=(20, 15))


# In[16]:


g = sns.scatterplot(x='id_canais', y='sl_quantidade_vitimas',
                   data=df3, hue='Canal de atendimento')
plt.legend( bbox_to_anchor = (2,1))
plt.show()


# In[17]:


ft = df3['sl_quantidade_vitimas'] > 0 


# In[18]:


df4 = df3[ft]
df4


# In[19]:


g = sns.scatterplot(x='id_canais', y='sl_quantidade_vitimas',
                   data=df4, hue='Canal de atendimento')

plt.show()


# In[20]:


df2['year'] = pd.DatetimeIndex(df['Data de cadastro']).year


# In[21]:


only_2020 = df2['year'] == 2020


# In[22]:


only_2020


# In[23]:


df5 = df2[only_2020]


# In[24]:


frame_5 = df5[['year', 'sl_quantidade_vitimas', 'id_canais', 'Canal de atendimento']]

frame_5


# In[25]:


def graph_2020():
    g = sns.scatterplot(x='id_canais', y='sl_quantidade_vitimas',
                   data=frame_5, hue='Canal de atendimento')
    plt.legend( bbox_to_anchor = (2,1))
    plt.xlabel('Canais de atendimento')
    plt.ylabel('Qtd. Vítimas')
    plt.title('Referência ao ano de 2020 sobre agressões contra a mulher')
    plt.show()


# In[26]:


only_2021 = df2['year'] == 2021
df6 = df2[only_2021]
frame_6 = df6[['year', 'sl_quantidade_vitimas', 'id_canais', 'Canal de atendimento']]


# In[27]:


frame_6


# In[28]:


def graph_2021():
    g = sns.scatterplot(x='id_canais', y='sl_quantidade_vitimas',
                   data=frame_6, hue='Canal de atendimento')
    plt.legend( bbox_to_anchor = (2,1))
    plt.xlabel('Canais de atendimento')
    plt.ylabel('Qtd. Vítimas')
    plt.title('Referência ao ano de 2021 sobre agressões contra a mulher')
    plt.show()


# In[29]:


only_2022 = df2['year'] == 2022
df7 = df2[only_2022]
frame_7 = df7[['year', 'sl_quantidade_vitimas', 'id_canais', 'Canal de atendimento']]


# In[30]:


frame_7


# In[31]:


def graph_2022():
    g = sns.scatterplot(x='id_canais', y='sl_quantidade_vitimas',
                   data=frame_7, hue='Canal de atendimento')
    plt.legend( bbox_to_anchor = (2,1))
    plt.xlabel('Canais de atendimento')
    plt.ylabel('Qtd. Vítimas')
    plt.title('Referência ao ano de 2022 sobre agressões contra a mulher')
    plt.show()


# In[32]:


only_2023 = df2['year'] == 2023
df8 = df2[only_2023]
frame_8 = df8[['year', 'sl_quantidade_vitimas', 'id_canais', 'Canal de atendimento']]


# In[33]:


frame_8


# In[34]:


def graph_2023():
    g = sns.scatterplot(x='id_canais', y='sl_quantidade_vitimas',
                   data=frame_8, hue='Canal de atendimento')
    plt.legend( bbox_to_anchor = (2,1))
    plt.xlabel('Canais de atendimento')
    plt.ylabel('Qtd. Vítimas')
    plt.title('Referência ao ano de 2023 sobre agressões contra a mulher')
    plt.show()


# In[35]:


graph_2020()
graph_2021()
graph_2022()
graph_2023()

