import pandas as pd


def merge_data(google_ads_data, ad_occurrences_data):
    merged_data = pd.merge(
        google_ads_data,
        ad_occurrences_data,
        left_on='Dia',
        right_on='data_formatada',
        how='inner'  # Podemos ajustar o método dependendo do que você quiser visualizar
    )

    # Verificar o sucesso da mesclagem
    if merged_data.empty:
        print("Atenção: A mesclagem dos dados resultou em um DataFrame vazio. Verifique as datas.")
    else:
        print(f"Dados mesclados com sucesso. {len(merged_data)} linhas combinadas.")

    return merged_data
