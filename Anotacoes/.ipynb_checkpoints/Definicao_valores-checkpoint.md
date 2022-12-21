* **Considerações**: 
    * Para tratar dados incompletos (ausência de valores): 
        * 1 - Utilizar algum método ou heurística para automaticamente definir valores para atributos com valores ausentes;
        * 2 - Utilizar média/moda/mediana no caso de valores simbólicos, utilizando todos objetos ou apenas os da classe em questão.
    * Verificar se não há atributos redundantes, ou seja, que possuem valores muito semelhantes.
    * Inserir ou não a cat_adm especial nos que a apresentam. Ela fazia parte de uma das classificações, e agora está a parte?
    * Ver o cod da inst.
    

29 atributos selecionados:

1 - <mark>NU_ANO</mark>: Ano de realização do exame;

2 - <mark>CO_GRUPO</mark>: Área de enquadramento do curso no ENADE;
    
* **2021**:
    * <mark>72</mark> - ADS
    * <mark>4004</mark> - BCC 
    * <mark>6409</mark> - GTI
    * <mark>4005</mark> - LCC
    * <mark>79</mark> - RC
    * <mark>4006</mark> - SI

* **2017**:
    * <mark>72</mark> - ADS
    * <mark>4004</mark> - BCC
    * <mark>6409</mark> - GTI
    * <mark>4003</mark> - EC
    * <mark>4005</mark> - LCC
    * <mark>79</mark> - RC
    * <mark>4006</mark> - SI
    
* **2014**:
    * <mark>72</mark> - ADS
    * <mark>4004</mark> - BCC
    * <mark>5809</mark> - EC
    * <mark>4005</mark> - LCC
    * <mark>79</mark> - RC
    * <mark>4006</mark> - SI

* **2011**:
    * <mark>72</mark> - ADS
    * <mark>4004</mark> - BCC
    * <mark>5809</mark> - EC
    * <mark>4005</mark> - LCC
    * <mark>79</mark> - RC
    * <mark>4006</mark> - SI

3 - <mark>CO_UF_CURSO</mark>: UF de funcionamento do curso;

4 - <mark>CO_REGIAO_CURSO</mark>: Região de funcionamento do curso;

5 - <mark>CO_CATEGAD</mark>: Categoria administrativa da IES (Pública ou Privada);

* **OBS**:
    * Categoria administrativa: especial – enquadra-se nessa categoria, a instituição de educação superior criada por lei, estadual ou municipal, e existente na data da promulgação da Constituição Federal de 1988, que não seja total ou preponderantemente mantida com recursos públicos, portanto, não gratuita.
    * Quais são essas instituições, poderia ser privada? (especial) (instuições municipais, que cobram mensalidade) (pesquisar sobre e ver os cods das especiais) (ver quantas linhas são as inst. especiais)

* **2021**:
    * 1. Pública Federal
    * 2. Pública Estadual
    * 3. Pública Municipal
    * 4. Privada CFL
    * 5. Privada SFL
    * 6. Especial (valor ausente)

* **2017**:
    * 1. Pública Federal
    * 2. Pública Estadual
    * 3. Pública Municipal
    * 4. Privada CFL
    * 5. Privada SFL
    * 7. Especial -> Pública Municipal

* **2014**:

    * 1. Pública Federal
    * 2. Pública Estadual
    * 3. Pública Municipal
    * 4. Privada CFL
    * 5. Privada SFL
    * 7. Especial (valor ausente)

* **2011**:

    * 1. Pública Federal
    * 2. Pública Estadual
    * 3. Pública Municipal
    * 4. Privada CFL
    * 5. Privada SFL

6 - <mark>CO_ORGACAD</mark>: Categoria da organização acadêmica da IES (Universidade, Faculdade, 
Centro Universitário, Centro Federal de Educação Tecnológica (CEFET) ou Instituto 
Federal de Educação, Ciência e Tecnologia (IFECT));

* **2021**:
    * 10019 = CEFET
    * 10020 = Centro Universitário
    * 10022 = Faculdade 
    * 10026 = IFECT
    * 10028 = Universidade

* **2017**:
    * 10019 = CEFET
    * 10020 = Centro Universitário
    * 10022 = Faculdade 
    * 10026 = IFECT
    * 10028 = Universidade

* **2014**:
    * 10019 = CEFET
    * 10020 = Centro Universitário
    * 10022 = Faculdade 
    * 10026 = IFECT
    * 10028 = Universidade

* **2011**:
    * 10019 = CEFET
    * 10020 = Centro Universitário
    * 10022 = Faculdade 
    * 10026 = IFECT
    * 10028 = Universidade

7 - <mark>CO_TURNO_GRADUACAO</mark>: Turno do curso;

* **2021**:
    * 1 = Matutino
    * 2 = Vespertino
    * 3 = Integral (IN_MATUT: 1 && IN_VESPER: 1 || IN_VESPER && IN_NOTURNO)
    * 4 = Noturno

* **2017**:
    * 1 = Matutino
    * 2 = Vespertino
    * 3 = Integral
    * 4 = Noturno

* **2014**:
    * IN_MATUT
    * IN_VESPER
    * IN_NOTURNO

* **2011**:
    * IN_MATUT
    * IN_VESPER
    * IN_NOTURNO

8 - <mark>NT_GER</mark>: Nota geral no exame (Max);

* **2021**: 93.7

* **2017**: 98.1

* **2014**: 97.4

* **2011**: 93.2

9 - <mark>ANO_FIM_EM</mark>: Ano de conclusão do Ensino Médio;

* **2021**: 1111 - 2200

* **2017**: 1957 - 2017

* **2014**: 1955 - 2014

* **2011**: 1951 - 2011

10 - <mark>ANO_IN_GRAD</mark>: Ano de início da graduação;

* **2021**: 1 - 2081

* **2017**: 1976 - 2017

* **2014**: 1977 - 2014

* **2011**: 1971 - 2011

11 - <mark>Tipo de escola que o participante cursou o Ensino Médio</mark> (Pública ou 
Privada);

* **2021**:
    * A = Pública.
    * B = Privada.
    * C = Exterior.
    * D = Maior parte pública.
    * E = Maior parte Privada.
    * F = Brasil e exterior.

* **2017**:
    * A = Pública.
    * B = Privada.
    * C = Exterior.
    * D = Maior parte pública.
    * E = Maior parte Privada.
    * F = Brasil e exterior.

* **2014**:
    * A = Pública.
    * B = Privada.
    * C = Exterior.
    * D = Maior parte pública.
    * E = Maior parte Privada.
    * F = Brasil e exterior.

* **2011**:
    * A = Pública.
    * B = Privada.
    * C = Maior parte pública.
    * D = Maior parte Privada.
    * E = Metade em escola pública e metade em escola privada.

12 - <mark>Modalidade de Ensino Médio</mark>;

* **2021**:
    * A = Tradicional.
    * B = Técnico.
    * C = Magistério.
    * D = Supletivo.
    * E = Outra.

* **2017**:
    * A = Tradicional.
    * B = Técnico.
    * C = Magistério.
    * D = Supletivo.
    * E = Outra.

* **2014**:
    * A = Tradicional.
    * B = Técnico.
    * C = Magistério.
    * D = Supletivo.
    * E = Outra.

* **2011**:
    * A = Tradicional.
    * B = Técnico.
    * C = Magistério.
    * D = Supletivo.
    * E = Outra.

13 - <mark>NU_IDADE</mark>: Idade do participante na data de realização do exame;

14 - <mark>TP_SEXO</mark>: Sexo do participante;

* **2021**:
    * M = Masculino
    * F = Feminino

* **2017**:
    * M = Masculino
    * F = Feminino

* **2014**:
    * M = Masculino
    * F = Feminino

* **2011**:
    * M = Masculino
    * F = Feminino

* **2008**:
    * M = Masculino
    * F = Feminino

15 - <mark>Cor ou raça do participante</mark>;

* **OBS**: Ordem não importa. O que importa é as escalas e o conteúdo dos valores estarem condizentes.

* **2021**:
    * A = Branca.
    * B = Preta.
    * C = Amarela.
    * D = Parda.
    * E = Indígena.
    * F = Não declarado.

* **2017**:
    * A = Branca.
    * B = Preta.
    * C = Amarela.
    * D = Parda.
    * E = Indígena.
    * F = Não declarado.

* **2014**:
    * A = Branco(a). -> Branca
    * B = Negro(a). -> Preta
    * C = Pardo(a)/mulato(a). -> Parda
    * D = Amarelo(a) (de origem oriental). -> Amarela
    * E = Indígena ou de origem indígena. -> Indígena
    * Nan -> F = Não declarado

* **2011**:
    * A = Branco(a). -> Branca
    * B = Negro(a). -> Preta
    * C = Pardo(a)/mulato(a). -> Parda
    * D = Amarelo(a) (de origem oriental). -> Amarela
    * E = Indígena ou de origem indígena. -> Indígena
    * Nan -> F = Não declarado

16 - <mark>Estado civil</mark>;

* **2021**:
    * A = Solteiro(a).
    * B = Casado(a).
    * C = Separado(a) judicialmente/divorciado(a). -> Separado
    * D = Viúvo(a).
    * E = Outro.

* **2017**:
    * A = Solteiro(a).
    * B = Casado(a).
    * C = Separado(a) judicialmente/divorciado(a). -> Separado
    * D = Viúvo(a).
    * E = Outro.

* **2014**:
    * A = Solteiro(a).
    * B = Casado(a).
    * C = Separado(a) judicialmente/divorciado(a). -> Separado
    * D = Viúvo(a).
    * E = Outro.

* **2011**:
    * A = Solteiro(a).
    * B = Casado(a).
    * C = Separado(a)/desquitado(a)/divorciado(a). -> Separado
    * D = Viúvo(a).
    * E = Outro.

17 - <mark>Nível de escolaridade do pai do participante</mark>;

* **2021**:
    * A = Nenhuma.
    * B = Fundamental 1-5.
    * C = Fundamental 6-9.
    * D = Médio.
    * E = Superior.
    * F = Pós-graduação.


* **2017**:
    * A = Nenhuma.
    * B = Fundamental 1-5.
    * C = Fundamental 6-9.
    * D = Médio.
    * E = Superior.
    * F = Pós-graduação.

* **2014**:
    * A = Nenhuma.
    * B = Fundamental 1-5.
    * C = Fundamental 6-9.
    * D = Médio.
    * E = Superior.
    * F = Pós-graduação.

* **2011**:
    * A = Nenhuma.
    * B = Fundamental 1-5.
    * C = Fundamental 6-9.
    * D = Médio.
    * E = Superior.
    * F = Pós-graduação.

18 - <mark>Nível de escolaridade da mãe do participante</mark>;

* **2021**:
    * A = Nenhuma.
    * B = Fundamental 1-5.
    * C = Fundamental 6-9.
    * D = Médio.
    * E = Superior.
    * F = Pós-graduação.

* **2017**:
    * A = Nenhuma.
    * B = Fundamental 1-5.
    * C = Fundamental 6-9.
    * D = Médio.
    * E = Superior.
    * F = Pós-graduação.

* **2014**:
    * A = Nenhuma.
    * B = Fundamental 1-5.
    * C = Fundamental 6-9.
    * D = Médio.
    * E = Superior.
    * F = Pós-graduação.

* **2011**:
    * A = Nenhuma.
    * B = Fundamental 1-5.
    * C = Fundamental 6-9.
    * D = Médio.
    * E = Superior.
    * F = Pós-graduação.

19 - <mark>Renda familiar do participante</mark>;

* **OBS**: Não levar em conta os valores em reais e sim em salários mínimo, considerando que não podemos comparar rendas de anos diferentes pela economia geral de cada ano ser diferente.

* **2021**:
    * A = Até 1,5 salário mínimo (até 1.650,00).
    * B = De 1,5 a 3 salários mínimos (1.650,01 a 3.300,00).
    * C = De 3 a 4,5 salários mínimos (3.300,01 a 4.950,00).
    * D = De 4,5 a 6 salários mínimos (4.950,01 a 6.600,00).
    * E = De 6 a 10 salários mínimos (6.600,01 a 11.000,00).
    * F = De 10 a 30 salários mínimos (11.000,01 a 33.000,00).
    * G = Acima de 30 salários mínimos (mais de 33.000,00).

* **2017**:
    * A = Até 1,5 salário mínimo (até 1.405,50).
    * B = De 1,5 a 3 salários mínimos (1.405,51 a 2.811,00).
    * C = De 3 a 4,5 salários mínimos (2.811,01 a 4.216,50).
    * D = De 4,5 a 6 salários mínimos (4.216,51 a 5.622,00).
    * E = De 6 a 10 salários mínimos (5. 622,01 a 9.370,00).
    * F = De 10 a 30 salários mínimos (9.370,01 a 28.110,00).
    * G = Acima de 30 salários mínimos (mais de 28.110,00).

* **2014**:
    * A = Até 1,5 salário mínimo (até  1.086,00).
    * B = De 1,5 a 3 salários mínimos (1.086,01 a 2.172,00).
    * C = De 3 a 4,5 salários mínimos (2.172,01 a 3.258,00).
    * D = De 4,5 a 6 salários mínimos (3.258,01 a 4.344,00).
    * E = De 6 a 10 salários mínimos (4.344,01 a 7.240,00).
    * F = De 10 a 30 salários mínimos (7.240,01 a 21.720,00).
    * G = Acima de 30 salários mínimos (mais de 21.720,00).

* **2011**:
    * A = Nenhuma
    * B = Até 1,5 salário mínimo (até  817,50).
    * C = De 1,5 a 3 salários mínimos (817,51 a 1.635,00).
    * D = De 3 a 4,5 salários mínimos (1.635,01 a 2.452,50).
    * E = De 4,5 a 6 salários mínimos (2.452,51 a 3.270,00).
    * F = De 6 a 10 salários mínimos (3.270,01 a 5.450,00).
    * G = De 10 a 30 salários mínimos (5.450,01 a 16.350,00).
    * H = Acima de 30 salários mínimos (mais de 16.350,01).

20 - <mark>Tipo de moradia</mark> (Com quem mora);

* **2021**:
    * A = Sozinho.
    * B = Parentes.
    * C = Cônjuge/Filhos.
    * D = Outras pessoas.
    * E = Universidade.
    * F = Habitação individual/coletiva.

* **2017**:
    * A = Sozinho.
    * B = Parentes.
    * C = Cônjuge/Filhos.
    * D = Outras pessoas.
    * E = Universidade.
    * F = Habitação individual/coletiva.

* **2014**:
    * A = Sozinho.
    * B = Parentes.
    * C = Cônjuge/Filhos.
    * D = Outras pessoas.
    * E = Universidade.
    * F = Habitação individual/coletiva.

* **2011**:
    * A = Sozinho.
    * B = Parentes.
    * C = Cônjuge/Filhos.
    * D = Outras pessoas.
    * E = Universidade.
    * F = Habitação individual/coletiva.

21 - <mark>Quantidade de pessoas em sua moradia</mark>;

* **2021**:
    * A = Nenhuma.
    * B = Uma.
    * C = Duas.
    * D = Três.
    * E = Quatro.
    * F = Cinco.
    * G = Seis.
    * H = Sete ou mais.

* **2017**:
    * A = Nenhuma.
    * B = Uma.
    * C = Duas.
    * D = Três.
    * E = Quatro.
    * F = Cinco.
    * G = Seis.
    * H = Sete ou mais.

* **2014**:
    * A = Nenhuma.
    * B = Uma.
    * C = Duas.
    * D = Três.
    * E = Quatro.
    * F = Cinco.
    * G = Seis.
    * H = Sete ou mais.

* **2011**:
    * A = Nenhuma.
    * B = Uma.
    * C = Duas.
    * D = Três.
    * E = Quatro.
    * F = Cinco.
    * G = Seis.
    * H = Sete ou mais.

22 - <mark>Política de ação afirmativa ou inclusão social utilizada para ingresso no curso</mark>;

* **2021**:
    * A = Não.
    * B = Critério étnico-racial.
    * C = Critério de renda.
    * D = Bolsa de estudos.
    * E = Combinação de critérios.
    * F = Critérios diferentes.

* **2017**:
    * A = Não.
    * B = Critério étnico-racial.
    * C = Critério de renda.
    * D = Bolsa de estudos.
    * E = Combinação de critérios.
    * F = Critérios diferentes.

* **2014**:
    * A = Não.
    * B = Critério étnico-racial.
    * C = Critério de renda.
    * D = Bolsa de estudos.
    * E = Combinação de critérios.
    * F = Critérios diferentes.

* **2011**:
    * A = Não.
    * B = Critério étnico-racial.
    * C = Critério de renda.
    * D = Bolsa de estudos.
    * E = Combinação de critérios.
    * F = Critérios diferentes.

23 - <mark>Situação de trabalho do participante</mark>;

* **2021**:
    * A = Não.
    * B = Eventualmente.
    * C = Até 20 horas. (semanais)
    * D = 21 a 39 horas. (semanais)
    * E = 40 horas ou mais. (semanais)

* **2017**:
    * A = Não.
    * B = Eventualmente.
    * C = Até 20 horas. (semanais)
    * D = 21 a 39 horas. (semanais)
    * E = 40 horas ou mais. (semanais)

* **2014**:
    * A = Não.
    * B = Eventualmente.
    * C = Até 20 horas. (semanais)
    * D = 21 a 39 horas. (semanais)
    * E = 40 horas ou mais. (semanais)

* **2011**:
    * A = Não.
    * B = Eventualmente.
    * C = Até 20 horas. (semanais)
    * D = 21 a 39 horas. (semanais)
    * E = 40 horas ou mais. (semanais)

24 - <mark>Quantidade de livros lidos no ano de realização do exame</mark>;

* **2021**:
    * A = Nenhum.
    * B = 1 ou 2.
    * C = 3-5.
    * D = 6-8.
    * E = +8.

* **2017**:
    * A = Nenhum.
    * B = 1 ou 2.
    * C = 3-5.
    * D = 6-8.
    * E = +8.

* **2014**:
    * A = Nenhum.
    * B = 1 ou 2.
    * C = 3-5.
    * D = 6-8.
    * E = +8.

* **2011**:
    * A = Nenhum.
    * B = 1 ou 2.
    * C = 3-5.
    * D = 6-8.
    * E = +8.

25 - <mark>Horas dedicadas à estudos, além das horas de aula</mark>;

* **2021**:
    * A = Nenhuma.
    * B = 1-3.
    * C = 4-7.
    * D = 8-12.
    * E = +12.

* **2017**:
    * A = Nenhuma.
    * B = 1-3.
    * C = 4-7.
    * D = 8-12.
    * E = +12.

* **2014**:
    * A = Nenhuma.
    * B = 1-3.
    * C = 4-7.
    * D = 8-12.
    * E = +12.

* **2011**:
    * A = Nenhuma.
    * B = 1-3.
    * C = 4-7.
    * D = 8-12.
    * E = +12.

26 - <mark>Opinião sobre as condições das salas de aulas</mark>;

* **OBS**: Faltar opções não importa pelo fato de naquele ano estas serem as disponíveis. Desde que os atributos tenham valores padronizados, está certo.

* **2021**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2017**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2014**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2011**:
    * A = Sim, todas. -> Concordo totalmente
    * B = Sim, a maior parte. -> Concordo
    * C = Somente algumas. -> Concordo parcialmente
    * D = Nenhuma. -> Discordo totalmente

27 - <mark>Opinião sobre as condições das salas de aulas práticas</mark>;

* **2021**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2017**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2014**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2011**:
    * A = Sim, todos. -> Concordo totalmente
    * B = Sim, a maior parte. -> Concordo
    * C = Somente alguns. -> Concordo parcialmente
    * D = Nenhuma. -> Discordo totalmente

28 - <mark>Opinião sobre o plano de ensino do curso</mark>;

* **2021**: "Os planos de ensino apresentados pelos professores contribuíram para o desenvolvimento das atividades acadêmicas e para seus estudos"
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2017**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2014**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2011** (34/52): "Você considera que seu curso contribui para a aquisição de formação teórica na área?"
    * A = Contribui amplamente. -> Concordo totalmente
    * B = Contribui parcialmente. -> Concordo parcialmente
    * C = Contribui muito pouco. -> Discordo
    * D = Não contribui. -> Discordo totalmente

29 - <mark>Avaliação pessoal da contribuição do curso para a formação</mark>;

* **2021**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2017**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2014**:
    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2011**:
    * A = Muito boa. -> Concordo totalmente
    * B = Boa. -> Concordo
    * C = Regular. -> Concordo parcialmente
    * D = Fraca. -> Discordo
    * E = Muito fraca. -> Discordo totalmente
    
# Atributos adicionados
    
30 - <mark>Situação Financeira</mark> (QE_I09 (2021), QE_I06 (2011));

* **2021**:
    * A = Não tenho renda e meus gastos são financiados por programas governamentais. -> Sem renda/Outros
    * B = Não tenho renda e meus gastos são financiados pela minha família ou por outras pessoas. -> Sem renda/Outros
    * C = Tenho renda, mas recebo ajuda da família ou de outras pessoas para financiar meus gastos. -> Tem renda/Outros
    * D = Tenho renda e não preciso de ajuda para financiar meus gastos. -> Tem renda/Independente
    * E = Tenho renda e contribuo com o sustento da família. -> Tem renda/Sustenta
    * F = Sou o principal responsável pelo sustento da família. -> Tem renda/Principal

* **2017**:
    * A = Sem renda/Outros
    * B = Sem renda/Outros
    * C = Tem renda/Outros
    * D = Tem renda/Independente
    * E = Tem renda/Sustenta
    * F = Tem renda/Principal

* **2014**:
    * A = Sem renda/Outros
    * B = Sem renda/Outros
    * C = Tem renda/Outros
    * D = Tem renda/Independente
    * E = Tem renda/Sustenta
    * F = Tem renda/Principal

* **2011**:
    * A = Não tenho renda e meus gastos são financiados pela minha família ou por outras pessoas. -> Sem renda/Outros
    * B = Tenho renda, mas recebo ajuda da família ou de outras pessoas para financiar meus gastos. -> Tem renda/Outros
    * C = Tenho renda e me sustento totalmente. -> Tem renda/Independente
    * D = Tenho renda, me sustento e contribuo com o sustento da família. -> Tem renda/Sustenta
    * E = Tenho renda, me sustento e sou o principal responsável pelo sustento da família. -> Tem renda/Principal

31 - <mark>Tipo de bolsa/Financiamento</mark> (QE_I11 (2021), QE_I10 (2011));

* **2021**:

    * A = Nenhum, pois meu curso é gratuito.
    * B = Nenhum, embora meu curso não seja gratuito.
    * C = ProUni integral.
    * D = ProUni parcial, apenas.
    * E = FIES, apenas.
    * F = ProUni Parcial e FIES.
    * G = Bolsa oferecida por governo estadual, distrital ou municipal.
    * H = Bolsa oferecida pela própria instituição.
    * I = Bolsa oferecida por outra entidade (empresa, ONG, outra).
    * J = Financiamento oferecido pela própria instituição.
    * K = Financiamento bancário.

* **2017**:

    * A = Nenhum, pois meu curso é gratuito.
    * B = Nenhum, embora meu curso não seja gratuito.
    * C = ProUni integral.
    * D = ProUni parcial, apenas.
    * E = FIES, apenas.
    * F = ProUni Parcial e FIES.
    * G = Bolsa oferecida por governo estadual, distrital ou municipal.
    * H = Bolsa oferecida pela própria instituição.
    * I = Bolsa oferecida por outra entidade (empresa, ONG, outra).
    * J = Financiamento oferecido pela própria instituição.
    * K = Financiamento bancário.

* **2014**:

    * A = Nenhum, pois meu curso é gratuito.
    * B = Nenhum, embora meu curso não seja gratuito.
    * C = ProUni integral.
    * D = ProUni parcial, apenas.
    * E = FIES, apenas.
    * F = ProUni Parcial e FIES.
    * G = Bolsa oferecida por governo estadual, distrital ou municipal.
    * H = Bolsa oferecida pela própria instituição.
    * I = Bolsa oferecida por outra entidade (empresa, ONG, outra).
    * J = Financiamento oferecido pela própria instituição.
    * K = Financiamento bancário.

* **2011**:

    * A = ProUni integral.
    * B = ProUni parcial.
    * C = FIES.
    * D = ProUni Parcial e FIES.
    * E = Outro tipo de bolsa oferecido por governo estadual, distrital ou municipal.
    * F = Bolsa integral ou parcial oferecida pela própria instituição de ensino.
    * G = Bolsa integral ou parcial oferecida por outra entidade (empresa, ONG, outra).
    * H = Financiamento oferecido pela própria instituição de ensino.
    * I = Financiamento oferecido por outra entidade (banco privado, etc).
    * J = Mais de um dos tipos de bolsa ou financiamento citados.

32 - <mark>UF de Conclusão do Ensino Médio</mark> (QE_I16 (2021), QE_I15 (2011)); # Ver se está no mesmo arquivo de onde o cara fez o EM

37 - <mark>Os professores apresentaram disponibilidade para atender os estudantes fora do horário das aulas</mark> (QE_I56 (2021), QE_I41 (2011));

* **2021**:

    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2017**:

    * 1 = Discordo totalmente.
    * 2 = Discordo.
    * 3 = Discordo parcialmente.
    * 4 = Concordo parcialmente.
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2014**:

    * 1 = Discordo totalmente. -> Nenhum
    * 2 = Discordo. -> Nenhum
    * 3 = Discordo parcialmente. -> Somente alguns
    * 4 = Concordo parcialmente. 
    * 5 = Concordo.
    * 6 = Concordo totalmente.
    * 7 = Não sei responder.
    * 8 = Não se aplica.

* **2011**:

    * A = Sim, todos os professores.
    * B  = Sim, a maior parte. 
    * C = Somente alguns. 
    * D = Nenhum.

38 - <mark>Os professores demonstraram domínio dos conteúdos abordados nas disciplinas</mark> (QE_I57 (2021), QE_I42 (2011));

Variáveis derivadas das variáveis selecionadas:

1 - Indicativo dicotômico de utilização de política de ação afirmativa ou inclusão social;

* Exemplo:
    * A = Não. -> Não
    * B = Sim, por critério étnico-racial. -> Sim
    * C = Sim, por critério de renda. -> Sim
    * D = Sim, por ter estudado em escola pública ou particular com bolsa de estudos. -> Sim
    * E = Sim, por sistema que combina dois ou mais critérios anteriores. -> Sim
    * F = Sim, por sistema diferente dos anteriores. -> Sim
    
2 - Quantidade de anos que o participante esteve ocioso entre a conclusão do Ensino Médio até o início da graduação;
* ANO_IN_GRAD - ANO_FIM_EM

3 - Quantidade de anos que o participante está na graduação.
* NU_ANO - ANO_IN_GRAD

-1 - Idade do participante no início da graduação (**Atributo inválido**);
* NU_IDADE e ANO_IN_GRAD em arquivos diferentes

