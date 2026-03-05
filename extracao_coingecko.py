import requests
import json
from datetime import datetime
import os


# 1. Endpoint público da CoinGecko (trazendo as moedas em Dólar)
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
response = requests.get(url)

if response.status_code == 200:
  
  # Pegamos o texto da resposta e convertemos para uma lista de dicionários Python
  dados_json = response.json()
  
  # Mostrando primeiro item para confirmar
  primeira_moeda = dados_json[0]["name"]
  preco = dados_json[0]["current_price"]
  
  print(f"Sucesso! A moeda número 1 é o {primeira_moeda} custando ${preco}")
  
  # Criando pasta
  pasta_destino = "raw_data"
  os.makedirs(pasta_destino, exist_ok=True)
    
  # Criando o nome do arquivo com a data e hora de agora
  data_hora_atual = datetime.now().strftime("%Y%m%d_%H%M%S")
  caminho_arquivo = f"{pasta_destino}/crypto_raw_{data_hora_atual}.json"
  
    
  # Salvando o arquivo fisicamente  
  with open (caminho_arquivo, "w", encoding="utf-8") as arquivo:
      json.dump(dados_json, arquivo, indent=4)
    
  print(f"Sucesso! Dados salvos em: {caminho_arquivo}")
  
else:
  print(f"Erro na API. Código: {response.status_code}")