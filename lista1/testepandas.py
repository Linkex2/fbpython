import pandas as pd
import os

vendas_df = pd.read_excel("Vendas.xlsx")
pd.set_option('display.max_columns', None)

faturamento = vendas_df[['ID Loja','Valor Final']].groupby('ID Loja').sum()

print(faturamento)

quantidade_loja = vendas_df[['ID Loja','Quantidade']].groupby('ID Loja').sum()

ticket_medio = (faturamento['Valor Final'] / quantidade_loja['Quantidade']).to_frame()

print(ticket_medio)