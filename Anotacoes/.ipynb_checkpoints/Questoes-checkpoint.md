# Progresso

- Contar nulos pros Estados.

# Tarefas

- Terminar com os classificadores e depois montar ~10 slides para apresentar o projeto pro diego.

- Explicar o dataset do inicio.

- Ver o Top-K, Z-Score.

- Verificar se luiz colocou todo o dataset no GridSearch.

- Ver PCA.

- Trocar "Curso" para "Área".
  
- Fazer bons comentários (baixo nível) por todo os códigos. Fazer também um README explicando o que fiz no código (alto nível) e como rodá-lo.

- Em Tipo_Escola_EM, valores "Exterior" foram removidos no código do Luis. (Não excluir, juntar exterior e brasil exterior) (Conferir)

# Questões

# Anotações

- Inscritos - Participantes == Numero_Faltantes + Numero_Notas_Invalidas

- Para o cáculo do conceito enade utiliza-se as seguintes informações de um curso:

    - Número de participantes com notas válidas;
    - Notas FG e CE de tais participantes.
    
- Para que um curso tenha seu conceito calculado, é necessário que tenha pelo menos 2 participantes com notas válidas.

- Considera-se para o cálculo do conceito, apenas as notas em que TP_PRES == 555.
 
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
     


