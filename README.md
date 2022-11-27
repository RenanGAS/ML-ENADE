# ML-ENADE

## Sobre os arquivos

### dados_####

- Converte os arquivos txt para csv, os enviando de dados_#### para dados_##\_csv;

- Posiciona o atributo CO_CURSO em primeiro no arquivo 1;

- Seleciona os arquivos que contém os atributos que serão utilizados e os movem de dados_##\_csv para dados_##\_Atributos;

- Ajusta os arquivos em dados_##\_Atributos, mudando o atributo CO_CURSO para primeira posição (no ano de 2014 foi removido as linhas com C0_CURSO = DJ1 e feito a conversão para inteiro para que seja possível a ordenação), e enviando-os para dados_##_Ajustado;

- Concatena o arquivo 1 com os demais presentes em dados_##_Ajustado;

- Remove as colunas duplicadas na concatenação;

- Seleciona apenas os atributos desejados;

- Seleciona apenas dados sobre cursos de computação;

- Converte a tabela resultante em um arquivo computacao_enade_####.csv .


### pre-process_####

- Pega os dados em computacao_enade_####.csv;

- Faz a tradução e transformação de valores/nome de atributos para valores/nome autoexplicativos e comuns entre os anos trabalhados;

- Converte a tabela resultante em um arquivo pre-process_####.csv .