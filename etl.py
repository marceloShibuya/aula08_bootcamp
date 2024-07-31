# importando as bibliotecas
import pandas as pd
import os
import glob

def extrair_dados_e_consolidar(caminho_pasta: str) -> pd.DataFrame:
    """
    uma funcao de extract que le e consolida os arquivos json
    """
    # juntando todos os arquivos da pasta "data" que estão no formato json 
    arquivo_json = glob.glob(os.path.join(caminho_pasta, '*.json'))
    # percorrendo todas as linhas, inclusive os cabecalhos dos arquivos que estão no formato json
    df_list = [pd.read_json(arquivo) for arquivo in arquivo_json]
    # concatenando somente as linhas, sem o cabecalho dos arquivos e sem o index, como se fosse o UNION no SQL
    df_total = pd.concat(df_list, ignore_index=True)
    #print(df_total)
    return df_total


def calcular_kpi_de_total_vendas(df_total: pd.DataFrame) -> pd.DataFrame:
    """
    uma funcao que transforma
    """
    df_total["Total"] = df_total["Quantidade"] * df_total["Venda"]
    return df_total


def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    uma funcao que da load em csv ou parquet
    """
    for formato in format_saida:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet") 


def pipeline_consolidado(pasta, tipo_arquivo):
    tabela = extrair_dados_e_consolidar(pasta)
    df_transformado = calcular_kpi_de_total_vendas(tabela)
    carregar_dados(df_transformado, tipo_arquivo)
   


