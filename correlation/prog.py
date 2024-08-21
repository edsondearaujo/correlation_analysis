import pandas as pd
import matplotlib.pyplot as plt

excel_file = '../data/cpc_data.xlsx'

google_ads_data = pd.read_excel(
    excel_file,
    sheet_name='Relatório Google Ads + BrandMon',
    engine='openpyxl',
    header=0
)
ad_occurrences_data = pd.read_excel(
    excel_file,
    sheet_name='Ocorrências de Anúncios',
    engine='openpyxl',
    header=0
)

google_ads_data.columns = ['Dia', 'Cliques', 'Impr.', 'Custo', 'CPC']
ad_occurrences_data.columns = ['data_formatada', 'Ocorrencia']
google_ads_data['Dia'] = pd.to_datetime(google_ads_data['Dia'], errors='coerce')
ad_occurrences_data['data_formatada'] = pd.to_datetime(ad_occurrences_data['data_formatada'], errors='coerce')

merged_data = pd.merge(
    google_ads_data,
    ad_occurrences_data,
    left_on='Dia',
    right_on='data_formatada',
    how='inner'
)

# Correlação entre CPC e Ocorrencias
correlation = merged_data['CPC'].corr(merged_data['Ocorrencia'])
print(f'Correlação entre CPC e Ocorrências de Anúncios: {correlation}')

# Gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['Ocorrencia'], merged_data['CPC'])
plt.title('Correlação entre CPC e Ocorrências de Anúncios')
plt.xlabel('Ocorrências de Anúncios')
plt.ylabel('CPC')
plt.grid(True)
plt.show()