# Tarefas

- Arrumar posições dos atributos e gerar as tabelas dos anos;

- Ver quantas linhas as IESes especiais ocupam nos anos. (Talvez vamos eliminá-las);

- Ver o que aconteceu com Engenharia da Computação no ENADE. (Enquadrando em outra área?) (Um CO_GRUPO engloba CO_CURSOs) (Pode ter ido pra um outro ciclo de ano (de engenharias));

- Seria ideal os conjuntos (2008, 2011, 2014, 2017, 2021), (2011, 2014, 2017, 2021), (2014, 2017, 2021). (por agora, inserir os 5 não marcados no dataset atual);

- Integrar os 4 anos.

# Perguntas

- O que fazer com valores não pertencentes ao padronizado ? (Metade pública e metade privada) (Se poucas exclui, se muitas, separa os dados em 2: publica e privada)

- Atributo Derivado "Indicativo dicotômico de utilização de política de ação afirmativa ou inclusão social" (Sim ou não): Mesma pergunta que "Política de ação afirmativa ou inclusão social utilizada para ingresso no curso" ? ( Exclui derivado)
 
- Ausência de valores em um atributo em um ano é um problema ? (Atributos de 2011 tem bastante valores a menos em atributos, mas iguais também) (**Tem problema**) (Fazer junção de valores, normalizar de acordo com 2011) (Não se aplica é um problema)
 
- Valores DJ1 em 2014 (Ver o porque, e dar um número para estes valores (que não existe). Não excluir) (Fazer de tudo para não excluir amostras)
 
- Código das IESes especiais: 21103 (FIEP - Privada CFL), 37862, 107988, 150138, 150268, 1286381 (Públicas mas cobram mensalidade)

    - Site: https://emec.mec.gov.br/emec/nova
     
- Em 2021:
    - Arquivo 4: NU_ANO, CO_CURSO, QE_I27 ~ QE_I68;
    - Arquivo 42: NU_ANO, CO_CURSO, QE_I78, QE_I79, QE_I80 e QE_I81;
    - Arquivo 43: NU_ANO, CO_CURSO, QE_I82, QE_I83, QE_I84, QE_I85, QE_I86, QE_I87, QE_I88, QE_I89, QE_I90, QE_I91, QE_I92.

- Em 2017:
    - Arquivo 4: NU_ANO, CO_CURSO, QE_I27 ~ QE_I68;
    - Arquivo 42: NU_ANO, CO_CURSO, QE_I78, QE_I79, QE_I80 e QE_I81.
    
- Em 2014:
    - Arquivo 4: NU_ANO, CO_CURSO, QE_I27 ~ QE_I68;
    - Arquivo 42: NU_ANO, CO_CURSO, QE_I78, QE_I79, QE_I80 e QE_I81.
    
- Em 2011:
    - Arquivo 4: NU_ANO, CO_CURSO, QE_I22 ~ QE_I54;
 
 - Sobre os novos atributos:
 
- Atributo 30: 
     - 2021, 2017, 2014: "Qual alternativa a seguir melhor descreve sua situação financeira (incluindo bolsas)?";
     - 2011: "Assinale a situação financeira abaixo que melhor descreve seu caso (incluindo bolsa).".
 
- Atributo 31:
     - 2021, 2017, 2014: "Que tipo de bolsa de estudos ou financiamento do curso você recebeu para custear todas ou a maior parte das mensalidades? No caso de haver mais de uma opção, marcar apenas a bolsa de maior duração.";
     - 2011: "Que tipo de bolsa de estudos ou financiamento você recebe ou recebeu para custear as mensalidades do curso?".
 
- Atributo 32: (UF diff da universidade)
     - 2021, 2017, 2014: "UF de Conclusão do Ensino Médio";
     - 2011: "Em que unidade da Federação você concluiu o ensino médio?".
 
- Atributo 33 (No arquivo 4 de todos os anos): (Não vale)
     - 2021, 2017, 2014: "O curso contribuiu para o desenvolvimento da sua consciência ética para o exercício profissional";
     - 2011: "Você considera que seu curso contribui na preparação para o exercício profissional?".
     
- Atributo 34 (No arquivo 4 de todos os anos): (Não vale)
     - 2021, 2017, 2014: "O curso exigiu de você organização e dedicação frequente aos estudos";
     - 2011: "Como você avalia o nível de exigência do curso?".
 
- Atributo 35 (No arquivo 4 de todos os anos): (Não vale)
     - 2021, 2017, 2014: "Foram oferecidas oportunidades para os estudantes participarem de programas, projetos ou atividades de extensão universitária";
     - 2011: "Seu curso oferece atividades complementares?".

- Atributo 36 (No arquivo 4 de todos os anos): (Não vale)
     - 2021, 2017, 2014: "O curso ofereceu condições para os estudantes participarem de eventos internos e/ou externos à instituição";
     - 2011: "Sua IES apoia financeiramente a participação dos estudantes em eventos (congressos, encontros, seminários, visitas técnicas etc.)?".
 
- Atributo 37 (No arquivo 4 de todos os anos):
     - 2021, 2017, 2014: "Os professores apresentaram disponibilidade para atender os estudantes fora do horário das aulas";
     - 2011: "Os professores têm disponibilidade para atendimento fora do período de aula?".
     
- Atributo 38 (No arquivo 4 de todos os anos): 
     - 2021, 2017, 2014: "Os professores demonstraram domínio dos conteúdos abordados nas disciplinas";
     - 2011: "Os professores demonstram domínio do conteúdo das disciplinas?".
 
- Atributo 39 (No arquivo 4 de todos os anos): (Mais ou menos)
     - 2021, 2017, 2014: "A biblioteca dispôs das referências bibliográficas que os estudantes necessitaram";
     - 2011: "Como você avalia o acervo da biblioteca, quanto à atualização, em face das necessidades curriculares do seu curso?".
     
- Atributo 40 (No arquivo 4 de todos os anos): (Não vale)
     - 2021, 2017, 2014: "A instituição promoveu atividades de cultura, de lazer e de interação social";
     - 2011: "Você considera que seu curso contribui para a aquisição de cultura geral?".
     


