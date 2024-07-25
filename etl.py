# importando as bibliotecas
import pandas as pd
import os
import glob

# uma funcao de extract que le e consolida os json
def extrair_dados_e_consolidar(caminho_pasta: str) -> pd.DataFrame:
    # juntando todos os arquivos da pasta "data" que estão no formato json 
    arquivo_json = glob.glob(os.path.join(caminho_pasta, '*.json'))
    # percorrendo todas as linhas, inclusive os cabecalhos dos arquivos que estão no formato json
    df_list = [pd.read_json(arquivo) for arquivo in arquivo_json]
    # concatenando somente as linhas, sem o cabecalho dos arquivos e sem o index, como se fosse o UNION no SQL
    df_total = pd.concat(df_list, ignore_index=True)
    #print(df_total)
    return df_total

# uma funcao que transforma
def calcular_kpi_de_total_vendas(df_total: pd.DataFrame) -> pd.DataFrame:
    df_total["Total"] = df_total["Quantidade"] * df_total["Venda"]
    return df_total


# uma funcao que da load em csv ou parquet





if __name__ == "__main__":
    pasta = 'data'
    tabela = extrair_dados_e_consolidar(pasta)
    df_transformado = calcular_kpi_de_total_vendas(tabela)
    print(df_transformado)


