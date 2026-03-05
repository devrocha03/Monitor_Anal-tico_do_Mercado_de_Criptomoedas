import sqlite3
import pandas as pd
import os

print("Iniciando a conexão com o banco de dados SQL...")

# 1. Caminho do arquivo processado
caminho_csv = "processed_data/crypto_clean.csv"

# Verifica se o arquivo realmente existe
if not os.path.exists(caminho_csv):
    print("Arquivo CSV não encontrado. Verifique a Fase 2.")
    exit()

# 2. Lendo os dados limpos com o Pandas
df = pd.read_csv(caminho_csv)

# 3. Criando a conexão com o Banco de Dados SQLite
# Se o arquivo 'cripto_db.sqlite' não existir, o Python cria na hora!
banco_de_dados = "cripto_db.sqlite"
conexao = sqlite3.connect(banco_de_dados)

# 4. Inserindo os dados no SQL
# Vamos criar uma tabela chamada 'tb_mercado_cripto'
# if_exists="replace" garante que se você rodar o script amanhã, ele atualiza a tabela
df.to_sql(name="tb_mercado_cripto", con=conexao, if_exists="replace", index=False)
print("Tabela 'tb_mercado_cripto' criada e populada com sucesso!")

# 5. Testando o banco com uma consulta SQL Real
print("\n--- Testando Consulta SQL ---")
print("Query: Top 5 moedas mais caras no momento\n")

query_sql = """
    SELECT name, symbol, current_price, market_cap 
    FROM tb_mercado_cripto 
    ORDER BY current_price DESC 
    LIMIT 5;
"""

# Executando a query e mostrando o resultado
resultado_sql = pd.read_sql_query(query_sql, conexao)
print(resultado_sql)

# 6. Fechando a conexão (Boa prática de Engenharia de Dados)
conexao.close()
print(f"\nCarga finalizada! O banco de dados '{banco_de_dados}' está pronto para uso.")
