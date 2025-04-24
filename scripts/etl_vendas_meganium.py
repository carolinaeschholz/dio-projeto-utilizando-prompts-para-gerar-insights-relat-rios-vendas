import pandas as pd
from pathlib import Path

def carregar_dados(caminho_raw_data):
    arquivos = list(Path(caminho_raw_data).glob("*.csv"))
    lista_df = []
    for arquivo in arquivos:
        df = pd.read_csv(arquivo)
        df['source'] = arquivo.stem.split("_")[-1]  # Nome do site
        lista_df.append(df)
    return pd.concat(lista_df, ignore_index=True)

def limpar_dados(df):
    df['date'] = pd.to_datetime(df['date'])
    df['delivery_country'] = df['delivery_country'].str.strip().str.title()
    df['product_sold'] = df['product_sold'].str.upper()
    return df

def salvar_dados_processados(df, caminho_destino):
    Path(caminho_destino).mkdir(parents=True, exist_ok=True)
    df.to_csv(Path(caminho_destino) / "vendas_consolidadas.csv", index=False)

def executar_etl():
    raw_path = "data/raw_data"
    processed_path = "data/processed_data"

    print("🔄 Carregando dados...")
    dados = carregar_dados(raw_path)

    print("🧹 Limpando dados...")
    dados_limpos = limpar_dados(dados)

    print("💾 Salvando dados consolidados...")
    salvar_dados_processados(dados_limpos, processed_path)

    print("✅ Processo ETL finalizado com sucesso!")

if __name__ == "__main__":
    executar_etl()