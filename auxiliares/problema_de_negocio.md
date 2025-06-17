# DS_Junho_2025

Created time: 13 de junho de 2025 01:21
Category: Extratégia de Negócio, Planning, Portifólio
Last updated time: 14 de junho de 2025 01:17

# **Case Prático – RH Estratégico com Dados**

# **🏢 Contexto da Empresa Fictícia**

**Empresa:** *Datavox Intelligence***Segmento:** Consultoria de Dados e BI**Localização:** Belo Horizonte, com atuação nacional**Equipe atual:** 45 colaboradores na área de dados (analistas, engenheiros e cientistas), com previsão de dobrar esse número nos próximos 6 meses

A Datavox está em crescimento acelerado e precisa contratar novos **analistas de dados**. O CEO quer tomar decisões baseadas em dados sobre onde buscar profissionais, qual perfil atrair e o que oferecer para se tornar uma empresa mais atrativa no mercado de dados brasileiro.

# **❗ Problema de Negócio**

O RH precisa:

- Entender o perfil dos profissionais de dados no Brasil
- Saber onde estão os talentos com maior potencial
- Descobrir o que motiva os profissionais a trocarem de empresa
- Criar uma estratégia de atração e retenção baseada em dados

Para isso, o time recebeu uma base **anonimizada da pesquisa nacional do Kaggle 2023/2024** (versão brasileira) com respostas reais de centenas de profissionais (5293 entrevistados).

# **🧠 Objetivo do Exercício**

- [X]  **Explorar e entender as colunas disponíveis no dataset**
- [ ]  **Cruzar dados técnicos (linguagens, ferramentas)** com **dados demográficos e de satisfação**
- [ ]  **Criar dashboards visuais claros** com as ferramentas permitidas
- [ ]  **Responder às perguntas de negócio do CEO**
- [ ]  **Fazer recomendações práticas para o RH**

# **🧰 Ferramentas que vamos utilizar:**

- Excel
- Power BI
- *Python para análise mais robusta*

# **📌 10 Perguntas que o CEO quer responder**

### 1. Quais estados concentram os profissionais com mais conhecimento em Python e SQL?

P1_i (cidade), P1_i_1(estado), P1_i_2(região)   

versus 

P4_d, P4_d_1 (SQL), P4_d_3 (Python), P4_e (mais utilizada), P4_f (preferida)

### 2. Existe correlação entre idade e domínio de ferramentas como Power BI e Tableau?

P1_1, P1_a_1

versus

P4_j, P4_j_1 (SQL), P4_j_3 (Python),  P4_k (preferida)

### 3. Qual o nível de inglês predominante entre os profissionais mais experientes?

P2_g (Níveis), P2_i (anos de experiência) (Precisa formatar essa coluna/number+string)

versus

Não achei nada relacionado a lingua (aqui o mais próximo que encontrei foi as pessoas que trabalham para empresas internacionais)

### 4. Quais ferramentas de nuvem são mais dominadas por quem tem +5 anos de experiência?

P2_g (N=ivel Senior), P2_i (anos de experiência) (Precisa formatar essa coluna/number+string)

versus

P4_h, P4_i

### 5. Qual o perfil dos profissionais que mais demonstram insatisfação com o trabalho atual?

Caracteristicas que definem um perfil profissional:

1. Nível (senior, pleno, junior) (P2_g)
2. Tempo de experiência (P2_i)
3. Cargo (P2_f)
4. Faixa salarial (P2_h)
5. Formação (P1_m)
6. Setor que trabalha (P2_b)
7. Tamanho da empresa (P2_c)
8. Idade (P1_a)
9. Localização  P1_i_1(estado), P1_i_2(região))
10. Forma de trabalho (P2_r)
11. Forma de trabalho ideal (P2_s)
    
    versus
    
    insatisfação (P2_k)
    

### 6. Qual a linguagem de programação mais comum entre quem ganha mais de R$10 mil por mês?

Faixa salarial (P2_h) 

versus 

P4_e (mais utilizada), P4_f (preferida)

### 7. Que fatores aparecem entre os profissionais mais satisfeitos com o trabalho atual?

Podemos usar a análise da pergunta: “Qual o perfil dos profissionais que mais demonstram insatisfação com o trabalho atual?” utilizando o outro ponto de vista dessa análise.

### 8. Qual o nível de escolaridade dos profissionais que atuam como Cientista de Dados Sênior?

Nível de ensino (P1_l)

versus

Nível (senior, pleno, junior) (P2_g)

Cargo (P2_f)

### 9. Os profissionais com mais de um curso ou certificação possuem salários maiores?

Faixa salarial (P2_h)

versus

Nível de ensino (P1_l)

### 10. Com base nos dados, quais 3 ações o RH pode tomar para ser mais competitivo na atração de talentos?

1. Garimpar entre os profissionais insatisfeitos, suprindo os principais fatores de insatisfação dos profissionais. Ver análise da pergunta (Qual o perfil dos profissionais que mais demonstram insatisfação com o trabalho atual?)
2. Salários competitivos e de acordo nível, mas levando em consideração um plano de carreira com métricas bem claras para promoções e incentivo para aperfeiçoamento profissional.
3. A partir da análise sobre o perfil dos proficionais satisfeitos, mapear os setores onde estes profissionais atuam, identificar e recrutar estes profissionais.

### 11. Quais as principais habilidades dos profissionais contratados?

O que eles querem dizer com contratados? Que estão empregados.

### 12. Qual a faixa salarial por senioridade de analistas e cientistas de dados?

Faixa salarial (P2_h)

versus

Cargo (P2_f), Nível (senior, pleno, junior) (P2_g)

### 13. Os profissionais da área de dados estão trabalhando em qual modalidade?

Cargo (P2_f), Nível (senior, pleno, junior) (P2_g)

versus

Forma de trabalho (P2_r)

Forma de trabalho ideal (P2_s)

# **📌 Recomendações práticas**

- Se pretende dobrar o número do pessoal da área de dados, talvez não precise contratar engenheiros, DBAs e outros também, além dos analistas de dados? Essa pergunta puxa a analise de: empregadores com uma infraestutura "imatura" de dados possuem empregados menos satisfeitos?

# **Instruções Finais para os Alunos**

- [ ]  Trabalhem em grupos de 2 a 4 pessoas.
- [ ]  Criem dashboards simples e objetivos.
- [ ]  Utilizem filtros e gráficos interativos sempre que possível.
- [ ]  Montem uma apresentação com os principais achados + recomendações práticas.
- [ ]  Preparem-se para apresentar como se estivessem numa reunião com o time de RH e o CEO.

# Objetivo geral

## Como a empresa pode utilizar a análise de dados para conhecer, contratar e reter os melhores profissionais de dados do Brasil?

# Características e fatores dos objetivos:

## CONHECER OS PROFISSIONAIS

- Quais caracteristicas definem que conhecemos um profissional de dados?
    - Geograficamente
    - Gênero/idade/cor
    - Percepções pessoais individuais
    - Níveis carreira
    - Ferramentas
        - Linguagens  que utilizam
            - Quais mais gostam?
            - Principal ferramenta
        - Bancos de dados que utilizam
        - Clouds
            - Utilizam
            - Preferidas
        - BI
            - Utilizam
            - Preferidas
        - AI e LLMs
    - Formação
    - Maior titulação
    - Gestores?
    - Salário
    - Forma de trabalho
        - (presencial/remoto/hibrido)
        - Como gostaia?
    - Tempo Experiência
    - Satisfação no atual emprego
        - Se não. Pq?
    - Quer ou busca novas oportunidades?
        - O que busca?
    - Cargos e Papéis que desempenham
        - Cargos
        - Papéis que desempenham
    - Entender a percepção e os desafios dos gestores
    - Objetivos na area de dados
        - O que buscam?
        
- Engenheiros
    - Tarefas / Rotinas de trabalho
    - Ferramentas ETL
    - Data Lake
    - Warehouse
    - Atividade que mais fazem
    
- Analistas
    - Tarefas / Rotinas de trabalho
    - Ferramentas ETL
    - Ferramentas para autonomia em análises
    - Atividade que mais fazem
    
- Cientistas
    - Tarefas / Rotinas de trabalho
    - Técnicas que utilizam
    - Tecnologias no dia-a-dia
    - Atividade que mais fazem

## CONTRATAR  E RETER OS MELHORES PROFISSIONAIS

### Quais as principais condições que a empresa pode ou deve oferecer para atrair bons proficionais?

- Como diferenciar bons profissionais?
    - Onde trabalham
        - Setor
        - Cargo
    - Tempo experiência
    - Formação
        - Tipo
        - Nível
    - Pelos seus objetivos
- O que eles valorizam
    - Salário
    - Ferramentas
    - Forma de trabalho (remoto, presencial ou híbrido)
- Salário
    - Média desse segmento
        - Calcular por area (DE / DA / DS)
    - % acima da média
        - Calcular por area (DE / DA / DS)
    - Relação insatisfação e salário
    - Salário x senioriedade
- O que buscam
- Principais causas de insatisfação na empresa atual.
- Entender os desafios atuais dos gestores.
