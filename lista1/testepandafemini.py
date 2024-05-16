import pandas as pd
import matplotlib as plt
import os

cidades = [
    'Santo André',
    'São Bernardo do Campo',
    'São Caetano do Sul',
    'Diadema',
    'Mauá',
    'Riberão Pires',
    'Rio Grande da Serra'
]

feminicidio_df = pd.read_csv("Feminicidio.csv")
pd.set_option('display.max_columns', None)

#anos = feminicidio_df[['ANO_ESTATISTICA','VITIMAS']].groupby('ANO_ESTATISTICA').sum('VITIMAS')
#cores = feminicidio_df[['COR_PELE','VITIMAS']].groupby('COR_PELE').sum('VITIMAS')
#idades = feminicidio_df[['IDADE_PESSOA','VITIMAS']].groupby('IDADE_PESSOA').sum('VITIMAS')
#femOsasco = feminicidio_df[feminicidio_df['MUNICIPIO_CIRCUNSCRICAO']=='Osasco']

femABC = feminicidio_df[feminicidio_df['MUNICIPIO_CIRCUNSCRICAO'].isin(cidades)]
#femVitABC = femABC[['MUNICIPIO_CIRCUNSCRICAO','VITIMAS']].groupby('MUNICIPIO_CIRCUNSCRICAO').sum('VITIMAS')
femVitCorABC = femABC[['COR_PELE','VITIMAS']].groupby('COR_PELE').sum('VITIMAS').sort_values().reset_index(names="Cidades")

raca_df = feminicidio_df.groupby('COR_PELE').size().reset_index(name="QTDE")
#femOsascoRaca = femOsasco.groupby('COR_PELE').size().reset_index(name="QTDE")





#print(anos)
#print(cores)
#print(idades)
#print(raca_df)
#print(femOsascoRaca)

print(femVitCorABC)

plt.figure(figsize=(8,8))
plt.pie(raca_df['QUANTIDADE'], labels=raca_df['Cidades'], autopct='%1.1f%%', startangle='140')
plt.title("Vitimas por cor da pele no ABCDMR")
plt.axis('equal')
plt.show()