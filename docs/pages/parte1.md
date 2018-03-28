 # Operação Sentinela dos Pampas: Análise de dados da Assembleia Legislativa do RS - Parte 1
 
 Após algumas semanas estudando Ciência de Dados, estou lançando meu primeiro projeto, me inspirando na [Operação Política Supervisionada] (https://ops.net.br/#!/) e na [Operação Serenata de Amor](https://serenata.ai/): Tirar análises dos dados públicos da Transparência da Assembleia Legislativa do RS.

Já se passaram 3 anos da legislatura atual e, portanto, temos dados suficientes para comparar como anda o desempenho de cada deputado. Para isso, está lançada a Operação Sentinela dos Pampas, cuja primeira fase será responsável por verificar *o quanto andam gastando nossos deputados*. Os resultados a seguir compreendem o período de janeiro de 2015 a dezembro de 2017 e *estão disponíveis na íntegra [aqui](https://public.tableau.com/profile/giovani.de.quadros#!/vizhome/GastosALRS/Destaques)*.


Cada deputado tem direito a uma cota para exercício da atividade, isto é, há uma certa quantidade de dinheiro disponível para o deputado gastar em diversas categorias. A despesa que mais pesou no orçamento durante esses 3 anos de legislatura foi a *INDENIZAÇÃO POR USO DE VEÍCULO PARTICULAR EM SERVIÇO*. Quase *9 milhões de reais* foram destinados somente para pagar essa despesa. O motivo disso será investigado mais a fundo nas próximas etapas da Operação.

Agora, vamos analisar cada deputado individualmente. Os gráficos a seguir são divididos em duas partes: O gasto total entre 2015 e 2017 e o gasto por mês. Essa divisão é necessária porque alguns deputados foram substituídos durante o período. Considerando os GASTOS POR MÊS, temos o nosso ranking:

*Os 5 Deputados que MENOS gastaram:*
* Ibsen Pinheiro: R$ 1.773/mês
* Marcel Van Hattem: R$3.938/mês
* João Reinelli: R$4.863/mês
* Pedro Ruas: R$6.813/mês
* Tarcísio Zimmermann: R$7.310/mês

*Os 5 Deputados que MAIS gastaram:*
Luís Augusto Lara: R$ 16.265/mês
Edu Oliveira: R$16.204/mês
Liziane Bayer: R$16.047/mês
Aloísio Classmann: R$15.984/mês
Vilmar Zanchin: R$15.589/mês


Os gráficos a seguir mostrarão os destaques para as principais categorias, isto é, os 5 que mais gastaram e os 5 que menos gastaram, além de outros deputados que tiveram um desempenho diferente da média.

As categorias Indenização por Uso de Veículo Particular em Serviço e Combustíveis estão ordenadas pelos GASTOS POR MÊS. As outras categorias levaram em conta os GASTOS NO TOTAL, pois sua frequência é menor, então é mais interessante verificar quem acumulou mais gastos durante todo o período.

## Vamos aos gráficos:

*Indenização por uso de veículo Particular em Serviço* - O deputado Edu Oliveira obteve um gasto geral baixo, pois permaneceu na Assembleia por apenas um ano. Os 5 deputados que mais gastaram nessa categoria pagaram, mensalmente, quase 7 mil reais cada. Em 3 anos, Ibsen Pinheiro gastou apenas 13 mil.

*Combustível* - Luis Augusto Lara gasta, por mês, 10 vezes o que Ibsen Pinheiro gasta.

*Requisições de impressos*: Embora Liziane Bayer tenha uma média mensal relativamente baixa, ela acumula quase o dobro de gastos que Nelsinho Metalúrgico, o segundo colocado. No centro do gráfico, temos deputados que gastaram mensalmente um valor acima da média, o que indica que foram feitas menos requisições, mas a um preço médio maior.

Vamos verificar melhor o que está acontecendo: Gilmar Sossella fez apenas uma requisição a um valor relativamente baixo. Pedro Pereira possui a maior média mensal porque fez apenas uma requisição, mas a um valor muito alto. Liziane Bayer e Nelsinho Metalúrgico possuem um gasto total maior por causa da frequência com que usam a cota para esta categoria.

*Postagens* - Nesta categoria, temos uma considerável diferença de comportamento entre os deputados. Os 5 deputados que mais gastaram com postagens tiveram uma média mensal bem menor que Luis Augusto Lara.

O motivo é semelhante ao observado anteriormente: Lara gastou apenas uma vez com postagens, mas a um preço bastante alto em relação aos outros deputados listados neste gráfico. Os 3 deputados que mais gastaram com postagens possuem uma certa frequência nos gastos, com um considerável pico nos meses de dezembro.


*Débitos Automáticos* - Outro caso fora do padrão. Enquanto alguns deputados tiveram um gasto mínimo, outros acumularam um total enorme, mas com uma média mensal baixa. Além disso, temos Maurício Dziedricki apresentando uma média mensal muito alta, mas um gasto total baixo. Vamos atrás do motivo:

Comparando os dois que menos gastaram com os dois que mais gastaram, vemos que Gilberto Capoani e Marcel Van Hattem usaram a cota pouquíssimas vezes nos finais de 2015 e 2016. Esse mesmo período representa uma alta nos gastos de Luiz Fernando Mainardi e Frederico Antunes. No final de 2017, temos o único gasto de Maurício Dziedricki, que resultou em uma média mensal tão alta.

*Os próximos gráficos mostram os destaques de mais três categorias, mas sem valores que fogem consideravelmente do padrão.*


## Geral

Esta é a comparação do total de gastos acumulados durante o período estudado (Isto é, substituindo Edu Oliveira, que tem uma média mensal alta, mas só entrou na ALRS em 2017, por Zilá Breitenbach). Os gráficos a seguir comparam o desempenho dos deputados que menos gastaram com os que mais gastaram. Os primeiros acumulam,juntos, um custo de R$0,8mi . Os outros custaram, juntos, R$ 2,8mi no mesmo período de tempo.


## Conclusões

É enorme a diferença de gastos que dois deputados podem apresentar no mesmo período de tempo. Um padrão perceptível é que deputados que gastam pouco em uma categoria tendem a gastar pouco nas outras categorias: Ibsen Pinheiro, além de ser o deputado que menos gastou no geral, aparece com um bom resultado em 5 das categorias listadas acima. O mesmo vale para os que mais gastaram: Luis Augusto Lara, o campeão de gastos, aparece com um gasto geral entre os 5 mais altos em 2 categorias, além de aparecer em uma categoria com um gasto mensal alto.

Observação: Não foi possível obter os dados dos ex-deputados Jorge Drumm, Alexandre Postal, Décio Franzen e Mário Jardel. Os dados do ex-deputado Marcel Van Hattem conseguiram ser obtidos dois dias após o deputado ter deixado a Assembleia.

Considerando a progressão de tempo, algumas categorias apresentaram uma diferença de padrões entre os gastos de deputados. É necessário fazer uma análise mais completa desses dados, a fim de identificar os tipos de comportamento possíveis. Clustering pode ser uma técnica bem útil para essa tarefa.

Além disso, classificar deputados pelo seu comportamento pode ajudar a identificar atividades suspeitas, onde pode estar havendo algum caso de corrupção. Mas os dados ainda não são suficientes para detectar ou supor essas atividades: É preciso obter os dados de cada gasto, com atenção especial ao CNPJ do destinatário de cada gasto. Esses dados não estão disponíveis diretamente no site da ALRS, mas (acho que) podem ser obtidos pelo sistema [e-SIC](http://www.al.rs.gov.br/e-sic/site/index.html?ReturnUrl=%2fe-sic).

Caso esses dados mais detalhados possam ser obtidos, o projeto tem potencial para evoluir de diversas formas, com alto potencial para aplicar inteligência artificial.

A Operação Sentinela dos Pampas está só começando. Até mais.


## EXTRA: Como os dados foram obtidos?

Se você se interessa por programação ou ciência de dados, seja muito bem-vindo a essa parte extra do texto!

Bom, no primeiro momento, pensei que os dados da Transparência da ALRS estivessem bem estruturados, detalhados e distribuídos como no site da Câmara dos Deputados, que [disponibiliza os dados das cotas de atividade parlamentar em vários formatos de arquivo](http://www2.camara.leg.br/transparencia/cota-para-exercicio-da-atividade-parlamentar/dados-abertos-cota-parlamentar). Pensei errado.

No site da Assembleia Legislativa, os dados estão disponíveis como na figura abaixo: Você seleciona o ano e o mês e o resumo dos gastos do deputado é disponibilizado em uma tabela.

Digamos que você queira acessar os dados de novembro de 2017. Para um usuário humano, o correto seria apenas selecionar o mês, clicar em "Pesquisar" e os dados seriam atualizados. Bastante intuitivo, mas queremos obter dados de todos os deputados em todos os meses de 2015 a 2017, *uma tarefa demorada demais para ser realizada humanamente.*

Então, *vamos automatizar a tarefa*. Para obter os dados, então, o necessário seria obter o código-fonte da página e filtrar esse código até chegar aos números, certo? Não é bem assim. Quando você seleciona o mês de novembro, o site atualiza a página usando um [View State](https://msdn.microsoft.com/en-us/library/bb386448.aspx), que informa "eu quero acessar os dados de novembro", só que em texto codificado e possivelmente criptografado. É necessário informar o View State certo para que a página possa carregar os dados do mês certo. Caso contrário, a página vai mostrar os dados mais recentes disponíveis. Isso foi um grande obstáculo para a automatização, então os dados tiveram que ser obtidos de outra forma.

Felizmente, o site da Assembleia disponibiliza os dados de outra forma: A versão para impressão. No caso da imagem anterior, para os gastos do deputado Adão Villaverde no mês de dezembro de 2017, você clica no ícone da impressora e chega na versão para impressão:

[http://ww1.al.rs.gov.br/*adaovillaverde*/DesktopModules/alrsTranspRelatorioGastos/Impressao.aspx?Tipo=1&IdCategoriaCota=*444*&DataGasto=1/12/2017%200:00:00](http://ww1.al.rs.gov.br/adaovillaverde/DesktopModules/alrsTranspRelatorioGastos/Impressao.aspx?Tipo=1&IdCategoriaCota=444&DataGasto=*1/12/2017*%200:00:00)

Esse link tem tudo que precisamos. O primeiro item grifado nele é o identificador do deputado. O segundo item é o identificador numérico do deputado. O terceiro é o mês do qual queremos os dados. Mas, se você olhar a imagem abaixo com atenção, vai ver que são apresentados os movimentos do mês de JANEIRO em vez de DEZEMBRO. Por quê? Porque o programador confundiu o padrão dia/mês/ano com o padrão mês/dia/ano. Espero que esse erro não tenha prejudicado alguém.

Enfim, só precisamos obter os identificadores dos deputados para automatizar a tarefa.

O primeiro passo é obter a [lista de deputados](http://www.al.rs.gov.br/deputados/ListadeDeputados.aspx). Por algum motivo, o servidor recusou minha solicitação para acessar a lista via script Python. Mas não tem problema. Salvei manualmente o código da página no [repositório do projeto](https://github.com/antiframes/sentinelaDosPampas).

A partir desse código, o script [findids.py](https://github.com/antiframes/sentinelaDosPampas/blob/master/findids.py) pega os links para as páginas dos deputados (que contêm o identificador). Acessando essas páginas, o script procura pelo link para a versão de impressão, que contém o identificador numérico. Os identificadores são salvos em [depids.csv](https://github.com/antiframes/sentinelaDosPampas/blob/master/depids.csv).

O script [getDepInfo.py](https://github.com/antiframes/sentinelaDosPampas/blob/master/getDepInfo.py) busca, a partir da lista de deputados, seus respectivos nomes e partidos e salva em [depinfo.csv](https://github.com/antiframes/sentinelaDosPampas/blob/master/depinfo.csv).

O script [innerjoin.py](https://github.com/antiframes/sentinelaDosPampas/blob/master/innerjoin.py) junta em uma tabela única as informações dos dois CSVs em um arquivo com todas as informações, [deps.csv](https://github.com/antiframes/sentinelaDosPampas/blob/master/2_prepared_data/deps.csv).

O útltimo script, [expenses.py](https://github.com/antiframes/sentinelaDosPampas/blob/master/expenses.py), obtém, para cada deputado, suas respectivas movimentações de 2015 a 2017. Em meia hora, está preparado o [expenses.csv](https://github.com/antiframes/sentinelaDosPampas/blob/master/2_prepared_data/expenses.csv), que contém todos os dados que queremos e *você tem permissão para baixá-lo e fazer suas próprias análises*.

Aguarde por mais dados, informações e investigações nas próximas partes da Operação.
