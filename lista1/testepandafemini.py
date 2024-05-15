import pandas as pd
import os

feminicido_df = pd.read_csv("Feminicidio.csv")
pd.set_option('display.max_columns', None)

anos = feminicido_df[['ANO_ESTATISTICA','VITIMAS']].groupby('ANO_ESTATISTICA').sum('VITIMAS')
cores = feminicido_df[['COR_PELE','VITIMAS']].groupby('COR_PELE').sum('VITIMAS')
idades = feminicido_df[['IDADE_PESSOA','VITIMAS']].groupby('IDADE_PESSOA').sum('VITIMAS')


print(anos)
print(cores)
print(idades)
