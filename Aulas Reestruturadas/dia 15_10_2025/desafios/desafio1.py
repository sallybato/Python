import pandas as pd
import matplotlib.pyplot as plt

vendas = pd.read_csv("vendas_loja.csv")
print(vendas)


total_vendas = vendas.groupby("Quant")["Preço Unitário"].mean()
print(total_vendas)

#n terminei o desafio
