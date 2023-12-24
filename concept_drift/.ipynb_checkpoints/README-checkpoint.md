### **Model Drift**

**Quando um modelo têm seu desempenho prejudicado por seus dados de treinamento estarem defasados em relação aos dados de teste/validação**. São definidos dois motivos para tal defasagem: Data Drift e Concept Drift.

### **Data drift**

**Mudança de distribuição de características do conjunto**. Consiste do aumento/diminuição do número de instâncias para um valor de um atributo. Por exemplo, imaginando a predição do salário de uma pessoa e considerando que o nível de educação é uma característica com alta correlação; um programa do governo que aumentasse o nível de educação de pessoas com baixa renda, num dado momento isto quebraria a expectativa do modelo em predizer que uma pessoa com um nível de educação mais alto teria uma renda maior. Eventualmente estas pessoas obteriam salários melhores e a correlação entre alto nível de educação e renda se reestabeleceria.

**Frases explicativas**:

- Considerando um modelo que classifica uma imagem em "Robalo" ou "Salmão", treinado com um conjunto formado por 70% de "Robalos" e 30% de "Salmões", a realização de um teste com um conjunto formado por 15% de "Robalos" e 85% de "Salmões", provavelmente não apresentaria um bom desempenho

### **Concept drift**

**Mudança na relação das características do conjunto com o valor de predição**. Por exemplo, retomando o contexto de predição de renda, caso as empresas passassem a considerar mais a experiência de trabalho do que o nível de escolaridade, a relação "quanto maior o nível de escolaridade, maior a renda" seria deteriorada.

**Frases explicativas**:

- Quando o padrão aprendido pelo modelo não é mais válido
- Quando P_T1(Y|X) != P_T2(Y|X)
    - "Quando a probabilidade de classificar uma instância como Y, dado um conjunto de características X, num momento T1, é diferente da probabilidade de classificar uma instância como Y, dado o mesmo conjunto de características X, num momento posterior T2"
    
### **Métodos de Detecção**

Para detecção de Drift existem dois tipos de métodos: que usam medidas estatísticas (Detection by Univariate Measure) e que usam classificadores (Detection by Domain Classifier).

#### **Univariate Measure**

Se baseiam em alguma medida que avalia a diferença entre duas distribuições de dados.

**Kolmogorov–Smirnov test:**

- One-sample K-S test: verifica se um conjunto de dados pertence a uma determinada distribuição (Connhecida).

- Two-sample K-S test: verifica se dois conjuntos de dados pertence a uma mesma distribuição (Desconhecida).

#### **Domain Classifier**

Utilizam um algoritmo de aprendizado de máquina para predição do conjunto a qual uma instância pertence (treinamento ou teste).

### **Métodos de Adaptação**

O que é

#### **Exemplos**

Funcionamento

### **Aplicação nos microdados do Enade**

Métodos testados + Código feito + Resultados

### **Referências**