from etl import pipeline_consolidado

pasta = 'data'
tipo_arquivo = ['csv','parquet']

pipeline_consolidado(pasta,tipo_arquivo)