### **Model Drift**

**Quando um modelo têm seu desempenho prejudicado por seus dados de treinamento estarem defasados em relação aos dados de teste/validação**. São definidos dois motivos para tal defasagem: Data Drift e Concept Drift.

### **Data drift**

**Mudança de distribuição de características do conjunto**. Consiste do aumento/diminuição do número de instâncias para um valor de um atributo. Por exemplo, imaginando a predição do salário de uma pessoa e considerando que o nível de educação é uma característica com alta correlação; um programa do governo que aumentasse o nível de educação de pessoas com baixa renda, num dado momento isto quebraria a expectativa do modelo em predizer que uma pessoa com um nível de educação mais alto teria uma renda maior. Eventualmente estas pessoas obteriam salários melhores e a correlação entre alto nível de educação e renda se reestabeleceria.

**Frases explicativas**:

- Considerando um modelo que classifica uma imagem em "Robalo" ou "Salmão", treinado com um conjunto formado por 70% de "Robalos" e 30% de "Salmões", a realização de um teste com um conjunto formado por 15% de "Robalos" e 85% de "Salmões", provavelmente não apresentaria um bom desempenho

### **Concept drift**

**Mudança na relação das características do conjunto com o valor de predição ou na relação entre as próprias características**. Por exemplo, retomando o contexto de predição de renda, caso as empresas passassem a considerar mais a experiência de trabalho do que o nível de escolaridade, a relação "quanto maior o nível de escolaridade, maior a renda" seria deteriorada.

**Frases explicativas**:

- Quando o padrão aprendido pelo modelo não é mais válido
- Quando P_T1(Y|X) != P_T2(Y|X)
    - "Quando a probabilidade de classificar uma instância como Y, dado um conjunto de características X, num momento T1, é diferente da probabilidade de classificar uma instância como Y, dado o mesmo conjunto de características X, num momento posterior T2"
- Pensando na relação idade x renda, se observado um conjunto de pessoas mais jovens (15\~40 anos), a relação é direta: quanto mais velho, maior a renda. No entanto, se observado um conjunto de pessoas mais velhas (30\~80 anos), a relação muda: quanto mais velho, menor a renda (por questões de aposentadoria)
    
### **Métodos de Detecção**

Para **detecção de Drift** existem dois tipos de métodos: que **avaliam uma única variável** do conjunto (**Univariate Drift**) e que **avaliam o conjunto inteiro**, considerando que podem haver **relações entre as variáveis** (**Multivariate Drift**).

### **1. Univariate Drift**

Se baseiam em alguma **função** para avaliar a **diferença entre duas distribuições de uma variável** (isoladamente das outras variáveis do conjunto). Imagina-se que a distribuição de alguma variável posssa mudar devido a algum fator externo. Para distribuições de **valores numéricos contínuos** tem-se as medidas: **Kolmogorov–Smirnov test** e **Wasserstein metric**, e para distribuições de **valores discretos ou categóricos**: **Cramer’s V** e **Population Stability Index (PSI)**.

#### **1.1 Kolmogorov–Smirnov test (K-S test):**

K-S test é um teste não paramétrico da igualdade de distribuições probabilísticas. Dessa forma, pode ser usado para verificar se uma amostra pertence ou não a uma distribuição de referência (One-sample K-S test), ou se duas amostras vieram de uma mesma distribuição (Two-sample K-S test). Sobre o segundo caso, é dito que o método é sensível a diferenças na localização e forma das distribuições.

#### **1.2 Wasserstein metric (Earth Movers Distance):**

#### **1.3 Cramer’s V:**

#### **1.4 Population Stability Index (PSI):**

### **2. Multivariate Drift**

Utilizam um **algoritmo de aprendizado de máquina** para predição do conjunto a qual uma instância pertence (treinamento ou teste). Define-se que há Drift se o algoritmo apresenta um bom desempenho, ou seja, se o modelo diferencia os dois conjuntos. Nisto, ganha-se a capacidade de avaliar a **mudança de distribuição conjunta de duas ou mais variáveis** (não apenas de uma variável isolada). Imagina-se que a distribuição conjunta de duas ou mais variáveis (a visualização de seus pontos num plano) posssa mudar devido a algum fator externo.

#### **2.1 PCA (Principal Component Analysis):**

Seleciona as variáveis que apresentam uma maior variância, descartando as outras do conjunto. Tem como objetivo diminuir a dimensionalidade do conjunto para dois propósitos: tornar o pipeline de processamento dos dados mais rápido e melhorar o desempenho de modelos com o filtro das variáveis menos impactantes no conjunto.

Utilizando o PCA, a biblioteca NannyML fez um método para detecção de Multivariate Drift. Baseia-se em construir um modelo PCA com um conjunto de dados, e detectar a presença de drift num conjunto em produção, compactando e descompactando-o com este modelo, definindo a ocorrência de drift se o erro de reconstrução do conjunto na descompactação é alto. "Compactação" se refere ao processo de diminuição de dimensionalidade, e "Descompactação" à possibilidade de reversão do processo, reconstruindo o conjunto a partir do conjunto compactado. Disto, imagina-se que se o conjunto em produção apresenta drift, o modelo PCA que observou as variáveis do conjunto de treinamento não fará uma boa compressão do conjunto em produção. Assim, no processo de reconstrução não terá um bom desempenho, apresentando um erro maior que o esperado.

**Ideias:**

- Fazer PCA para três variáveis e plotar um gráfico disso pra ver como fica pras edições

### **Métodos de Adaptação**

O que é

#### **Exemplos**

Funcionamento

### **Aplicação nos microdados do Enade**

Métodos testados + Código feito + Resultados

### **Referências**