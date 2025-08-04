import pandas as pd

class LerDB:
    def lerDatabase():
        try:
            #Leitura do CSV
            table = pd.read_csv("./database/gestaoTransporteSG.csv", encoding='latin1', sep=';')
            #Filtro pelo Status "Atrasada"
            tableAtrasados = table[table['OBS Status'] == 'Atrasada']
            #Realiza a impressão da tabela
            print(tableAtrasados)
            print("---------------------------------------------------------------------")
            print("Tabela lida com sucesso")
            return tableAtrasados
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")