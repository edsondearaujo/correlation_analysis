import pandas as pd

def process_data(google_ads_data, ad_occurrences_data):
    # Renomear colunas para consistência
    google_ads_data.columns = ['Dia', 'Cliques', 'Impr.', 'Custo', 'CPC']
    ad_occurrences_data.columns = ['data_formatada', 'Ocorrencia']

    # Converter as colunas de data para datetime
    google_ads_data['Dia'] = pd.to_datetime(google_ads_data['Dia'], errors='coerce')
    ad_occurrences_data['data_formatada'] = pd.to_datetime(ad_occurrences_data['data_formatada'], errors='coerce')

    # Checar se há valores nulos
    if google_ads_data['Dia'].isnull().sum() > 0 or ad_occurrences_data['data_formatada'].isnull().sum() > 0:
        print("Atenção: Existem datas inválidas ou nulas nos dados.")

    return google_ads_data, ad_occurrences_data
