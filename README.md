# CPC e Ocorrências: Análise de Correlação

## Descrição

Este projeto realiza uma **análise de correlação** entre o **Custo por Clique (CPC)** das campanhas de Google Ads e o número de **Ocorrências de Anúncios**. O objetivo principal é entender se o aumento ou diminuição das ocorrências de anúncios influencia diretamente no CPC. Isso ajuda a avaliar como a visibilidade e a presença dos anúncios podem impactar o custo pago por cada clique.

A análise se concentra nos dados fornecidos de uma empresa fictícia que opera campanhas de Google Ads, focando na análise a partir de **abril de 2023**, quando uma nova estratégia de monitoramento foi implementada.

## Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python 3.8+**
- **Pandas**: Para manipulação e análise de dados.
- **Matplotlib**: Para criação de gráficos e visualizações.
- **Seaborn**: Para gráficos de regressão e aprimoramento visual.
- **OpenPyXL**: Para leitura de arquivos Excel.

## Instalação e Execução

Siga os passos abaixo para rodar o projeto em sua máquina:

### 1. Clonar o repositório:
Escolha um local para clonar o projeto em sua máquina.
Execute o comando para realizar o clone.
```bash
git clone https://github.com/edsondearaujo/correlation_analysis.git
```
Entrar no diretório do projeto
```bash
cd correlation_analysis
```

### 2. Criar e ativar um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar as dependências:
```bash
pip install -r requirements.txt
```

### 4. Certificar-se de que o arquivo de dados _cpc_data.xlsx_ está na pasta data/:
O arquivo Excel contém os dados da campanha de Google Ads e deve estar no diretório data/.

### 5. Executar o projeto:
```bash
python3 -m src.main
```

## Resultados e Análises
Aqui estão as visualizações e a interpretação dos gráficos gerados durante o processo de análise:

### 1. Gráfico de Dispersão:
**Relação entre Ocorrências de Anúncios e CPC**
<div align="center"> <img src="https://github.com/edsondearaujo/correlation_analysis/blob/main/assets/img/grafico_dispersao.png" alt="Gráfico de Dispersão" width="600"> </div>
O gráfico de dispersão mostra a relação entre o número de Ocorrências de Anúncios e o Custo por Clique (CPC). Cada ponto no gráfico representa um dia de dados. Embora haja uma leve correlação positiva (conforme indicado pela correlação de aproximadamente 0.21), a relação não é forte, sugerindo que outros fatores podem estar influenciando o CPC além das ocorrências de anúncios.

### 2. Gráfico de Linha:
**Média Mensal do CPC a Partir de Abril de 2023**
<div align="center"> <img src="https://github.com/edsondearaujo/correlation_analysis/blob/main/assets/img/media_mensal_cpc.png" alt="Média Mensal do CPC" width="600"> </div>
Este gráfico de linha exibe a média mensal do CPC ao longo do tempo, começando em abril de 2023, quando a nova estratégia de anúncios foi implementada. Podemos observar que houve uma leve redução no CPC nos primeiros meses, indicando que a nova estratégia pode ter ajudado a otimizar o custo da campanha.

### 3. Gráfico de Regressão Linear:
**Correlação entre CPC e Ocorrências de Anúncios**
<div align="center"> <img src="https://github.com/edsondearaujo/correlation_analysis/blob/main/assets/img/regressao_linear.png" alt="Regressão Linear" width="600"> </div>
O gráfico de regressão linear mostra a relação entre o CPC e as Ocorrências de Anúncios. A linha azul indica a melhor linha de ajuste, revelando uma tendência de aumento do CPC à medida que as ocorrências aumentam. A inclinação é leve, o que reforça a correlação moderada encontrada na análise anterior.

### 4. Saída no Terminal
<div align="center"> <img src="https://github.com/edsondearaujo/correlation_analysis/blob/main/assets/img/saida_terminal.png" alt="Saída no Terminal" width="600"> </div>
A saída no terminal mostra as principais mensagens do processo de execução:

- Dados carregados com sucesso.
- Mesclagem de dados realizada.
- Correlação calculada entre CPC e Ocorrências de Anúncios (aproximadamente 0.21), indicando uma correlação positiva, mas relativamente fraca.

## Considerações Finais
Este projeto oferece uma visão detalhada sobre como as ocorrências de anúncios podem influenciar o Custo por Clique (CPC) em campanhas de Google Ads. Embora a correlação detectada seja moderada, é possível que uma combinação de estratégias de otimização e ajustes de lances possa melhorar o desempenho da campanha e reduzir o CPC ao longo do tempo.

## Contribuição
Sinta-se à vontade para contribuir com o projeto. Sugestões e melhorias são sempre bem-vindas!