import matplotlib.pyplot as plt
import seaborn as sns


# Função para gráfico de dispersão
def plot_scatter(merged_data):
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_data['Ocorrencia'], merged_data['CPC'], alpha=0.7, c='blue', edgecolors='w', s=100)

    plt.title('Dispersão entre Ocorrências de Anúncios e CPC')
    plt.xlabel('Ocorrências de Anúncios')
    plt.ylabel('CPC')
    plt.grid(True)
    plt.show()


# Função para regressão linear
def plot_regression(merged_data):
    sns.lmplot(x='Ocorrencia', y='CPC', data=merged_data, aspect=1.5, scatter_kws={'alpha': 0.7})
    plt.title('Regressão Linear: Ocorrências de Anúncios vs CPC')
    plt.grid(True)
    plt.show()

# Análise temporal do CPC
def plot_monthly_cpc_trend(google_ads_data):
    """
    Gera um gráfico de linha mostrando a queda do CPC ao longo dos meses, a partir de abril de 2023.

    Args:
        google_ads_data (pandas.DataFrame): Dados filtrados de Google Ads com coluna 'Dia' e 'CPC'.
    """

    # Filtrar os dados a partir de Abril/2023
    google_ads_data_filtered = google_ads_data[google_ads_data['Dia'] >= '2023-04-01']

    # Calcular a média mensal do CPC
    monthly_cpc = google_ads_data_filtered.resample('ME', on='Dia')['CPC'].mean()

    # Plotar gráfico de linha da queda do CPC ao longo dos meses
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_cpc.index, monthly_cpc.values, marker='o', linestyle='-', color='b')
    plt.title('Média Mensal do CPC (Abril 2023 em diante)')
    plt.xlabel('Mês')
    plt.ylabel('CPC Médio')
    plt.grid(True)
    plt.show()
