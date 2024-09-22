# ML-ENADE

O projeto consiste na predição do Conceito Enade dos cursos de computação no Brasil através de **modelos de aprendizado supervisionado**, utilizando as **características socioeconômicas** dos cursos, extraídas de um questionário socioeconômico preenchido pelos estudantes antes da realização do exame do Enade. No artigo são descritas duas etapas principais do trabalho: **Pré-processamento** e **Avaliação**.

## Pré-processamento

Para o pré-processamento dos microdados do Enade, com o objetivo de adquirir um conjunto com os dados dos cursos das edições de 2011, 2014, 2017 e 2021, pronto para treinamento/teste dos modelos de classificação (**K-NN, DT, RF, SVM e MLP**), deve-se executar os seguintes arquivos:

- **gerador_tabelas_anos.ipynb**: Faz o download dos microdados de cada edição (2011, 2014, 2017 e 2021), transforma os arquivos para Dataframe, seleciona os atributos desejados e os cursos de computação (ADS, BCC, EC, GTI, RC, LCC e SI), e cria um arquivo **computacao_enade_{ano}.csv** para cada edição.

- **pre-process_{ano}.ipynb**: Substitui códigos, números e letras por seus valores nominais (por exemplo, substitui os códigos dos cursos e das questões pelo nome do curso e o tópico da questão, os números de cada estado pela sigla do estado, e as letras das alternativas por um resumo do seu conteúdo). Disto, cria-se um arquivo **pre-process_{ano}.csv** para cada edição.

- **gerador_tabela_final.ipynb**: Faz OneHotEncoding das variáveis categóricas e média das variáveis numéricas para cada curso em uma edição. Contextualização: cada linha em **pre-process_{ano}.csv** contém dados de alunos de um curso, tendo um curso **n** linhas que correspondem a **n** alunos que fizeram a prova. Para predição do conceito Enade de um curso, precisamos de um conjunto que contenha em cada linha os dados de um curso e seu conceito Enade (atributos independentes e alvo). Assim, em **gerador_tabela_final.ipynb** faz-se as operações de OneHotEncoding e média para *sumarizar* os dados dos alunos de um curso em uma só linha.
    - Estas operações podem ser aplicadas a uma única edição (**pre-process_{ano}.csv**) ou sobre um conjunto com todas edições (disponível em **merge_tabelas.csv**, formada em **merge_tabelas_processadas.ipynb**).
    - Quando utiliza-se o conjunto com todas edições, não se mistura os dados dos alunos de um curso de edições diferentes, tendo no conjunto final, quatro instâncias de cada curso (referentes as quatro edições).
    - Cria-se um arquivo **teste_OHE_curso.csv**.
    
- **calculadora_conceito_enade.ipynb**: Faz o cálculo do conceito Enade dos cursos de computação de cada edição. No site do Inep, os arquivos de algumas edições com o conceito Enade obtido pelos cursos (o conceito Enade não se encontra junto com os microdados), não contém o código do curso atrelado ao conceito, não sendo possível mapear os conceitos nestes arquivos aos cursos em **teste_OHE_curso.csv**. Assim, foi calculado manualmente o conceito Enade dos cursos, conforme a fórmula disponível na Nota técnica de cada edição (Nota técnica de 2021: https://download.inep.gov.br/educacao_superior/enade/notas_tecnicas/2019/nota_tecnica_n_7_2022_CGCQES_DAES_metodologia_calculo_conceito_enade_2021.pdf).
    - Calcula-se o conceito Enade dos cursos de cada edição, criando-se os arquivos **conceito_enade_{ano}.csv**.

- **concatena_conceito.ipynb**: Gera o arquivo utilizado para treinamento/teste dos modelos (**teste_OHE_curso_treinamento.csv**). Concatena o arquivo **teste_OHE_curso.csv** com os dados dos cursos de todas edições, ao arquivo **merge_tabelas_conceitos.csv** (gerado por **merge_tabelas_conceitos.ipynb**) com os conceitos dos cursos de todas edições.

## Avaliação

Foram realizados três experimentos preliminares para avaliação do conjunto de dados, e feito um teste de hipótese a partir dos resultados.

### Experimentos preliminares

O primeiro experimento consiste do uso do conjunto completo (com todas edições) para treinamento/teste dos modelos. No diretório **modelos** tem-se diretórios para cada algoritmo de classificação, onde este primeiro experimento é feito para cada modelo no arquivo **{nome_modelo}_conjunto_inteiro.ipynb**. Observa-se que o conjunto utilizado é o **teste_OHE_curso_treinamento.csv**.

O segundo experimento baseia-se no uso de um conjunto formado por dados de uma só edição. Para isto, o arquivo **gerador_tabela_final.ipynb** é aplicado para uma única edição, por exemplo, **pre-process_2021.csv**, e o conjunto resultante é submetido aos algoritmos de classificação. Os arquivos deste experimento se encontram próximos aos do primeiro experimento, nomeados como **{nome_modelo}_ano.ipynb**.

No terceiro experimento são feitos conjuntos com dados de um único curso de computação para todas edições. Para isto, no arquivo **gerador_tabela_final.ipynb** é acrescentado uma condição no código que filtra apenas dados de um determinado curso, do arquivo **teste_OHE_curso.csv**. O código deste experimento é o mesmo do segundo experimento, encontrando-se nos arquivos **{nome_modelo}_ano.ipynb**, uma seção em que é possível selecionar o conjunto de um curso ao invés do conjunto de uma edição, para treinamento/teste dos modelos.

Observa-se que nestes experimentos a avaliação dos modelos é feita através da validação cruzada com cinco partições, de forma manual. Disto, considera-se como resultado a média da métrica F1-Score das cinco iterações.

### Teste de hipótese

Considerando os resultados dos experimentos, em que os modelos tiveram um desempenho por volta de 50%, fez-se um experimento sob a **hipótese de que o aspecto temporal das edições estaria prejudicando o desempenho da predição**. Este aspecto temporal se refere ao intervalo de tempo entre as edições, por exemplo, entre a edição de 2011 e 2021 tem-se dez anos. Disto, este experimento tem como objetivo verificar se a diferença temporal entre as edições estaria prejudicando o desempenho dos modelos.

Para isto, organizou-se uma bateria de testes, onde cada teste realizava o treinamento de um modelo com edições anteriores à edição utilizada para teste do mesmo. Como conclusão deste experimento, obteve-se que a adição da edição de 2011 diminui o desempenho de predição.

## Model Drift

Como continuação do projeto, tem-se a proposta de uma investigação mais aprofundada da hipótese de aspecto temporal, sob a ótica do conceito de **model drift**. **Model drift** se refere à queda de desempenho de um modelo em produção, pelos seus dados de treinamento estarem defasados em relação aos dados de entrada do mundo real. Com isto em mente, está sendo feito o estudo das bibliotecas **Deepchecks**, **Scikit-multiflow** e **Frouros**, e a tentativa da reprodução de métodos de detecção de **drift**.

Os códigos relacionados estão no diretório **concept_drift**.


