import pandas as pd

def load_data(file_path, sheet_name):
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        print(f"Dados carregados com sucesso da aba '{sheet_name}'")
        return data
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
