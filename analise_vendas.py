"""
Análise de Vendas de Produtos de Informática

Autor: Marcus Vinicius Almeida

Objetivo:
Realizar análise exploratória de dados de vendas utilizando
Python, Pandas e Matplotlib, gerando métricas de faturamento
e visualizações gráficas para apoio à tomada de decisão.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Ler CSV
df = pd.read_csv(r"C:\Users\55939\Desktop\analise-vendas-ti\vendas.csv")

# Mostrar colunas
print(df.columns)

# Criar faturamento
df["Faturamento"] = df["Quantidade"] * df["Preco"]

# Mostrar dados
print(df.head())

# Faturamento total
faturamento_total = df["Faturamento"].sum()

print("\nFaturamento Total:")
print(f"R$ {faturamento_total:,.2f}")

# Produto
produto = df.groupby("Produto")["Faturamento"].sum().sort_values(ascending=False)

print("\nFaturamento por Produto")
print(produto)

# Cidade
cidade = df.groupby("Cidade")["Faturamento"].sum()

print("\nFaturamento por Cidade")
print(cidade)

# Categoria
categoria = df.groupby("Categoria")["Faturamento"].sum()

print("\nFaturamento por Categoria")
print(categoria)

# Grafico Produto
plt.figure(figsize=(8,5))
produto.plot(kind="bar")
plt.title("Faturamento por Produto")
plt.tight_layout()
plt.savefig("graficos_produto.png")
plt.show()

# Grafico Cidade
plt.figure(figsize=(8,5))
cidade.plot(kind="bar")
plt.title("Faturamento por Cidade")
plt.tight_layout()
plt.savefig("graficos_cidade.png")
plt.show()
