# 📊 Monitor Analítico do Mercado de Criptomoedas (End-to-End)

Este é um projeto de Análise e Engenharia de Dados de ponta a ponta (End-to-End). O objetivo principal foi construir um pipeline automatizado que extrai dados em tempo real de uma API pública, realiza o tratamento dos dados, armazena em um banco de dados relacional e os consome em um dashboard gerencial.

O design do dashboard foi focado no minimalismo, garantindo uma leitura rápida e clara dos principais indicadores (KPIs) do mercado.

## 🛠️ Tecnologias Utilizadas
* **Python:** Linguagem principal para orquestração.
* **API REST (CoinGecko):** Fonte dos dados brutos em formato JSON.
* **Pandas:** Biblioteca utilizada para a limpeza e transformação dos dados (ETL).
* **SQLite:** Banco de dados relacional para armazenamento local estruturado.
* **Power BI:** Ferramenta de visualização conectada via script Python para a criação do painel.

## 🗺️ Arquitetura do Projeto

1. **Fase 1: Extração (Raw Data)** Script (`extracao_coingecko.py`) que consome o endpoint público da CoinGecko e salva uma "fotografia" do Top 100 criptomoedas em um arquivo `.json`.
   
2. **Fase 2: Transformação (Processed Data)** Script (`processamento_pandas.py`) que lê o JSON bruto, filtra apenas as colunas de interesse analítico (Preço, Volume, Market Cap), trata os tipos de dados e salva o resultado em formato `.csv`.
   
3. **Fase 3: Armazenamento (Banco de Dados SQL)** Script (`carga_sql.py`) que ingere o arquivo CSV limpo em um banco de dados **SQLite**, criando a tabela `tb_mercado_cripto`.
   
4. **Fase 4: Visualização de Dados** Conexão direta do Power BI ao arquivo `.sqlite` utilizando um script Python para gerar um dashboard com foco em UI/UX limpa e direta.

## 📌 Principais Insights
* O projeto permitiu lidar com desafios reais de coleta de dados, como paginação de APIs e formatação de JSON.
* A visualização foi construída destacando o domínio de mercado (Volume e Market Cap) de gigantes como Bitcoin e Ethereum de forma visualmente limpa.
