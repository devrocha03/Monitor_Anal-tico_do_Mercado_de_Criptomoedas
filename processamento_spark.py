import pandas as pd
import glob
import os

print("Iniciando a sessão do Pandas...")

# 1. Encontrar o arquivo JSON mais recente na pasta raw_data
arquivos = glob.glob("raw_data/crypto_raw_20260305_104743.json")
if not arquivos:
    print("❌ Nenhum arquivo encontrado na pasta raw_data.")
    exit()

# Ordena os arquivos pela data de modificação e pega o mais novo
arquivos.sort(key=os.path.getmtime, reverse=True)
arquivo_mais_recente = arquivos[0]

print(f"Lendo o arquivo: {arquivo_mais_recente}")

# 2. Carregar os dados para um DataFrame do Pandas
df = pd.read_json(arquivo_mais_recente)

# 3. Selecionar apenas as colunas importantes para a Análise de Dados
colunas_selecionadas = [
    "id", 
    "symbol", 
    "name", 
    "current_price", 
    "market_cap", 
    "total_volume", 
    "price_change_percentage_24h", 
    "last_updated"
]

# Criar um novo DataFrame apenas com essas colunas
df_limpo = df[colunas_selecionadas].copy()

# 4. Tratamento de Tipos de Dados
# A coluna de data vem como texto, vamos converter para o tipo datetime
df_limpo['last_updated'] = pd.to_datetime(df_limpo['last_updated'])


# 5. Visualizar o resultado no terminal
print("\n--- Estrutura dos Dados Limpos ---")
print(df_limpo.info())

print("\n--- Amostra dos Dados ---")
print(df_limpo.head())


# 6. Salvar o dado processado em uma nova pasta
pasta_destino = "processed_data"
os.makedirs(pasta_destino, exist_ok=True)

caminho_salvamento = f"{pasta_destino}/crypto_clean.csv"
df_limpo.to_csv(caminho_salvamento, index=False)

print(f"\nSucesso! Dados limpos e salvos em: {caminho_salvamento}")