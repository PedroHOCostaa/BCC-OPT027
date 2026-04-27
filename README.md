# BCC-OPT027
Diretório referente a atividade realizada na disciplina de Visualização de dados do curso de Bacharelado em Ciência da Computação

# Base de dados
A base de dados que utilizamos é do projeto MonitorAr-Rio, a pagina inicial do projeto de encontra em https://ambienteclima.prefeitura.rio/monitoramento-diario-da-qualidade-do-ar/

## Links importantes
* Link para planilha da base de dados: https://www.data.rio/datasets/PCRJ::qualidade-do-ar-dados-hor%C3%A1rios/explore?layer=2
* Link para história do programa MonitorAr-Rio: https://ambienteclima.prefeitura.rio/monitorar-2026-historia/
* Link para critérios de qualidade do ar: https://ambienteclima.prefeitura.rio/monitorar-2026-criterios/

## Descrição da base de dados
Esta base de dados possui dados horários de qualidade do ar dos anos de 2011 até 2025 referentes a 8 estações de monitoramento do ar, como pode ser visto no arquivo amostra_data-set.csv presente neste repositório.
A base de dados é multivariada e topológica.
A base de dados possui até o momento 1.007.804 instancias, logo para a realização das tecnicas de visualização de dados será necessário agrupar os dados ou selecionar uma amostra menor de dados, para evitarmos oclusão visual e também não sobrecarregarmos os hardwares utilizados.

### Descrição dos parâmetros colhidos pelas estações
As estações de monitoramento por meio de sensores, colhem parametros referentes a qualidade do ar, a seguir iremos listar os parametros colhidos por todas as estações:
* Velocidade do Vento: metros por segundo
* Direção do Vento: graus
* Radiação Solar: watts por metro quadrado
* Precipitação Pluviométrica: milímetros
* Umidade Relativa do Ar: porcentagem (ou percentual)
* Temperatura: graus Celsius
* Pressão Atmosférica: milibares
* Latitude: Graus
* Longitude: Graus
* Sistema de Referência Geocêntrico para as Américas(SIRGAS 2000): coordenada x e y

Agora iremos listar os parametros especificos das estações (não são medidos em todas as estações de monitoramento):
* $SO_2$ Dióxido de Enxofre
* $HCNM$ Hidrocarbonetos Não-Metano
* $HCT$ Hidrocarbonetos Totais
* $CH_4$ Hidrocarboneto Metano, junto com $HCNM$ e $HCT$ formam o conjunto de variaveis $HC$ Hidrocarbonetos, assim como acreditamos que uma dessas variaveis é conseguida utilizando as outras duas
* $CO$ Monóxido de Carbono
* $NO$ Monóxido de Nitrogênio
* $O_3$ Ozônio
* $NO_2$ Dióxido de Nitrogênio
* $NOx$ Óxidos de Nitrogênio, junto com $NO$ e $NO_2$ formam o conjunto de variaveis $NOx$, tem seu valor calculado somando $NO$ com $NO_2$. 
* $O_3$ Gás Ozonio 
* $MP_{10}$ Material particulado com diâmetro aerodinâmico equivalente de corte de 10 micrômetros.
* $MP_{2,5}$ Material particulado com diâmetro aerodinâmico equivalente de corte de 2,5 micrômetros.

As concentrações de **Monóxido de Carbono** ($CO$) e **Hidrocarbonetos** ($HC$) são medidas em partes por milhão [ppm], enquanto as demais são medidas em microgramas por metro cúbico de ar [$\mu g/m^3$].
### Descrição das estações de monitoramento
1. Largo da Carioca / Centro (CA): O3, CO, MP10
2. Praça Cardeal Arco Verde / Copacabana (AV): O3, MP10
3. São Cristóvão (SC): O3, MP10
4. Praça Sans Peña / Tijuca (SP): NOx, O3, MP10
5. Irajá (IR): SO2, NOx, O3, CO, HC, MP2.5, MP10
6. Bangu (BG): NOx, O3, MP10
7. Campo Grande (CG): NOx, O3, MP10
8. Pedra de Guaratiba (PG): O3, MP10

## Perguntas
Os conhecimentos que buscamos explorar por meio da visualização de dados são:
1. Em quais horas do dia possui uma maior concentração de $CO$ e $NOx$? em cada estação e cada dia da semana. 
2. Qual é a amplitude termica de cada região, em cada uma das estações do ano.
3. Há alguma discrepância clara entre os dados de (definir algum) entre uma zona central e zonas mais afastadas?
  * Gráfico de Violino (Violin Plot): Eixo X com o nome das estações e eixo Y com a concentração
4. O quão significativa foi a queda geral de poluentes durante o isolamento da pandemia em comparação aos anos anteriores?
  * Gráfico de linhas com a média dos poluentes ao longo dos anos, incluindo um bloco sombreado no fundo cobrindo exatamente os meses de 2020 e 2021 para contrastar a queda.

## Pré-processameanto
### Dados redundantes
Algumas variaveis podem ser conseguidas utilziando as outras, a seguir iremos as listar:
1. $NO$, $NO_2$ e $NOx$, utilizando a formula $NOx = NO + NO_2$ pode-se conseguir o valor de qualquer uma tendo os outros dois
2. Latitude e Longitude juntos representam a mesma coisa que as coordenadas x e y do SIRGAS 2000
3. A variavel codnum e estação representam qual a estação de monitoramento que fez aquela leitura, a diferença é que uma é uma string enquanto a outra é um numero inteiro
### Pré-processameanto necessário para as perguntas propostas
1. Iremos agrupar por horário, dia da semana e estações de monitoramento, então teremos 5(número de estações com leitor de $CO$ ou $NOx$) * 7(dias da semana) * 24(horas do dia) = 840 grupos, em cada grupo então iremos calcular uma média das duas variaveis que serão apresentadas, agora iremos juntas os valores em 35 tabelas (dias da semana * estações de monitoramento) ordenando por horário, para então apresentarmos com um graficos de linhas.
2. 
3. 
4. Iremos agrupar incialmente por ano, então separado em cada ano iremos agrupar novamente por mes, e em cada mês iremos calcular a média das variaveis relacionadas a poluentes, assim iremos conseguir um grafico de cada ano com no eixo x o mes e no eixo y o índice de qualidade do ar (IQAr), assim nos teremos 15 graficos que cada um possui 
### Informações externas 
link para desrições do mapa do rio de janeiro https://www.rio.rj.gov.br/dlstatic/10112/6438610/4221811/74LUOSPLC572017.pdf
