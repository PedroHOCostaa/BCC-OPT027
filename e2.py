import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Carregando a base de dados
# Substitua pelo nome do arquivo que vocês usarão na entrega final
df = pd.read_csv('data-set-2016-2025.csv') # só verifica se o nome do arquivo ta certo

# 2. Pré-processamento principal: Converter a coluna 'data' para o tipo datetime
# Isso é crucial para agrupar por hora, mês e ano
df['data'] = pd.to_datetime(df['data'])

# Pré-processamento específico: Extrair a hora e calcular a média
df['hora'] = df['data'].dt.hour
df_q2 = df.groupby('hora')[['nox', 'co']].mean().reset_index()

# Criando a visualização complexa com eixos Y independentes
fig2 = go.Figure()

# Adicionando a linha do NOx (Eixo esquerdo)
fig2.add_trace(go.Scatter(
    x=df_q2['hora'], y=df_q2['nox'], 
    name='NOx (µg/m³)', mode='lines+markers', line=dict(color='blue')
))

# Adicionando a linha do CO (Eixo direito)
fig2.add_trace(go.Scatter(
    x=df_q2['hora'], y=df_q2['co'], 
    name='CO (ppm)', mode='lines+markers', line=dict(color='red'), yaxis='y2'
))

# Configurando o layout para habilitar o eixo Y duplo e a interatividade
fig2.update_layout(
    title='Padrões Diários: Concentração de NOx e CO ao longo das horas',
    xaxis_title='Hora do Dia',
    yaxis=dict(title=dict(text='Concentração NOx (µg/m³)', font=dict(color='blue')), tickfont=dict(color='blue')),
    yaxis2=dict(title=dict(text='Concentração CO (ppm)', font=dict(color='red')), tickfont=dict(color='red'), overlaying='y', side='right'),
    hovermode='x unified' # Interação: exibe os dois valores ao passar o mouse
)

fig2.show()

# Pré-processamento: Filtrar estações e remover nulos na coluna analisada
df_q3 = df[df['codnum'].isin([1, 8])].copy()
df_q3.dropna(subset=['pm10'], inplace=True)

# Mapeando os nomes das estações para o gráfico
df_q3['nome_estacao'] = df_q3['codnum'].map({1: 'Largo da Carioca (Centro)', 8: 'Pedra de Guaratiba (Afastada)'})

# Criando o Gráfico de Violino
fig3 = px.violin(
    df_q3, 
    x='nome_estacao', 
    y='pm10', 
    color='nome_estacao',
    box=True, # Adiciona um mini boxplot dentro do violino
    points=False, # Oculta os pontos individuais para não travar o PC devido ao volume
    title='Discrepância de Material Particulado (MP10): Centro vs. Zona Afastada',
    labels={'nome_estacao': 'Estação de Monitoramento', 'pm10': 'Concentração de MP10 (µg/m³)'}
)

fig3.show()

# Pré-processamento: Agrupar por ano e mês para não gerar oclusão visual
df_q4 = df.set_index('data').resample('ME')['pm10'].mean().reset_index()

# Criando a Série Temporal básica
fig4 = px.line(
    df_q4, 
    x='data', 
    y='pm10', 
    title='Impacto do Isolamento Social da Pandemia nos Níveis de MP10',
    labels={'data': 'Período', 'pm10': 'Média Mensal de MP10 (µg/m³)'}
)

# Adicionando o sombreamento interativo (Interação avançada)
fig4.add_vrect(
    x0="2020-03-01", x1="2021-12-31", 
    fillcolor="rgba(255, 0, 0, 0.2)", 
    layer="below", line_width=0,
    annotation_text="Isolamento Social (COVID-19)", 
    annotation_position="top left"
)

# Adicionando slider de tempo na base (Garante a nota de interatividade)
fig4.update_layout(xaxis=dict(rangeslider=dict(visible=True), type="date"))

fig4.show()