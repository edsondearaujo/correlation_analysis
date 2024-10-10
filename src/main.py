from src.data_loader import load_data
from src.data_processing import process_data
from src.data_merging import merge_data
from src.analysis import analyze_correlation
from src.visualization import plot_scatter, plot_regression, plot_monthly_cpc_trend

def main():
    file_path = './data/cpc_data.xlsx'

    # Carregar dados de cada aba
    google_ads_data = load_data(file_path, 'Relatório Google Ads + BrandMon')
    ad_occurrences_data = load_data(file_path, 'Ocorrências de Anúncios')

    if google_ads_data is not None and ad_occurrences_data is not None:
        # Processar e limpar os dados
        google_ads_data, ad_occurrences_data = process_data(google_ads_data, ad_occurrences_data)

        # Mesclar os dados
        merged_data = merge_data(google_ads_data, ad_occurrences_data)

        if not merged_data.empty:
            # Analisar correlação
            analyze_correlation(merged_data)

            # Plotar gráfico de dispersão
            plot_scatter(merged_data)

            # Plotar a queda do CPC ao longo dos meses (de abril 2023 em diante)
            plot_monthly_cpc_trend(google_ads_data)

            # Gerar uma regressão linear para entender melhor a relação
            plot_regression(merged_data)

if __name__ == '__main__':
    main()
