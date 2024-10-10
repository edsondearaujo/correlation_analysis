def analyze_correlation(merged_data):
    correlation = merged_data['CPC'].corr(merged_data['Ocorrencia'])
    print(f"Correlação entre CPC e Ocorrências de Anúncios: {correlation}")
    return correlation
