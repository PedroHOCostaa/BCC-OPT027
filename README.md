# BCC-OPT027
Diretório referente a atividade realizada na disciplina de Visualização de dados do curso de Bacharelado em Ciência da Computação

# Base de dados
A base de dados que utilizamos é do projeto MonitorAr-Rio, a pagina incial do projeto de encontra em https://ambienteclima.prefeitura.rio/monitoramento-diario-da-qualidade-do-ar/

## Links importantes
* Link para planilha da base de dados: https://www.data.rio/datasets/PCRJ::qualidade-do-ar-dados-hor%C3%A1rios/explore?layer=2
* Link para história do programa MonitorAr-Rio: https://ambienteclima.prefeitura.rio/monitorar-2026-historia/
* Link para critérios de qualidade do ar: https://ambienteclima.prefeitura.rio/monitorar-2026-historia/

## Descrição da base de dados
Esta base de dados possui dados horários de qualidade do ar dos anos de 2011 até 2025 referentes a 8 estações de monitoramento do ar, como pode ser visto no arquivo amostra_data-set.csv presente neste repositório.

### Descrição dos paremetros colhidos pelas estações
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
* Sistema de Referência Geocêntrico para as Américas: coordenada x e y

Agora iremos listar os parametros especificos das estações (não são medidos em todas as estações de monitoramento):
* $SO_2$
* $HCNM$ Hidrocarbonetos Não-Metano
* $HCT$ Hidrocarbonetos Totais
* $CH_4$ Hidrocarboneto Metado, junto com $HCNM$ e $HCT$ formam o conjunto de variaveis $HC$ Hidrocarbonetos, assim como acreditamos que uma dessas variaveis é conseguida utilizando as outras duas
* $CO$ Monóxido de Carbono
* $NO$ Monóxido de Nitrogênio
* $NO_2$ Dióxido de Nitrogênio
* $NOx$ Óxidos de Nitrogênio, junto com $NO$ e $NO_2$ formam o conjunto de variaveis $NOx$, tem seu valor calculado somando $NO$ com $NO_2$. 
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
