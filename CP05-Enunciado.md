<img src="/assets/teste.svg" width="100%">

# DYNAMIC PROGRAMMING 2025/2

| Checkpoint | 5 | ```CURSO:``` | ENGENHARIA DE SOFTWARE |
|---|---|---|---|
| ```DISCIPLINA:``` | DYNAMIC PROGRAMMING | ```PROFESSOR:``` | Marcelo Amorim |


# ✨💰 O Desafio das Moedas 

---

# MISSÃO DESTE CHECKPOINT

Você deverá implementar **quatro funções em python** que recebe como parâmetros um valor de montante **M**, um vetor **moedas** contendo o valor das notas e determina **a menor quantidade de notas** a ser entregue de forma que somadas seja igual ao montante **M**.  

### Regras do Problema (Troca de Moedas)

1.  **Objetivo:** Determinar a **menor quantidade de moedas** cuja soma dos valores seja exatamente igual ao montante $M$.
2.  **Disponibilidade:** A quantidade de cada moeda no vetor `moedas` é **ilimitada**.
3.  **Restrições:** As moedas e o montante $M$ são números inteiros positivos.
4.  **Impossibilidade:** Se for impossível formar o montante $M$ com as moedas dadas, a função deve retornar um valor que indique isso (por exemplo, `-1` ou `float('inf')`).

***

**Funções a serem entregues**

1. Função iterativa (estratégia gulosa)
2. Função recursiva pura (sem memoização)
3. Função recursiva (com memoização) (Top down)
4. Função usando Programação Dinâmica (Bottom up)

Exemplo de cabeçalho das funções e possíveis chamadas:
~~~py
qtdeMoedas(M,moedas) #Função iterativa estratégia gulosa
qtdeMoedasRec(M,moedas) #Função recursiva simples
qtdeMoedasRecMemo(M,moedas) #Função recursiva com memoização
qtdeMoedasPD(M,moedas) #Função usando Programação Dinâmica

# CHAMADAS EXEMPLO DE TESTE
qtdeMoedas(6,[1,3,4])
qtdeMoedasRec(6,[1,3,4])
qtdeMoedasRecMemo(6,[1,3,4])
qtdeMoedasPD(6,[1,3,4])
~~~



### Estrutura de Entrega e Documentação

Todas as quatro funções devem seguir as melhores práticas de programação em Python, incluindo:

**Documentação (Docstrings):**

Cada função deve possuir um `docstring` (documentação interna em Python) claro e conciso que explique os seguintes pontos:

* **O que a função faz.**
* **Os parâmetros de entrada** (`M`, `moedas`).
* **O valor de retorno** (incluindo o caso de impossibilidade).
* **A complexidade de tempo teórica da função (Notação $O$ (Big O Notation), $\Omega$ (Big Omega) e $\Theta$ (Big Theta)).** 

#### Além da implementação das funções, o grupo deverá escrever um relatório em Markdown como readme.md (Github do repositório a ser entregue). Este relatório deve conter:

> IMPORTANTE: **Informar todos os integrantes do grupo (RA e NOME COMPLETO)**.

1. Introdução e Contextualização do Problema
* O Problema da Troca de Moedas (Coin Change Problem)
    * **Contextualização:** Apresente o problema de forma clara: Qual é o objetivo principal (minimizar a quantidade de moedas)? Quais são as premissas (moedas ilimitadas, valores inteiros)?
    * **Natureza do Problema:** Explique por que este problema é classificado como um **Problema de Otimização**.
* Definição de Programação Dinâmica (PD)
    * **Conceito:** O que é Programação Dinâmica? Defina-a em termos de seus dois pilares fundamentais:
  * **Subestrutura Ótima:** Descreva como a solução ótima do problema principal depende das soluções ótimas de subproblemas menores.
  * **Subproblemas Sobrepostos:** Explique o que são e por que a presença deles é o que torna a PD (e a memoização) uma técnica poderosa.

2. Análise Detalhada das Abordagens

* Para cada uma das quatro funções implementadas, você deverá fornecer a análise teórica e prática.

* Função 1: Estratégia Gulosa (Iterativa)
    * **Conceito:** Descreva a lógica da estratégia gulosa.
    * **Análise Crítica:** Explique por que esta abordagem **não garante** a solução ótima para *qualquer* conjunto de moedas.
    * **Demonstração:** Utilize casos de teste para ilustrar o **fracasso** do algoritmo guloso, comparando o resultado obtido com o resultado ótimo real.
    * **Complexidade:** Apresente a complexidade de tempo.

* Função 2: Recursiva Pura (Ingênua)
    * **Conceito:** Descreva o algoritmo recursivo sem otimizações.
    * **Análise de Desempenho:**
      * Explique e ilustre (com um esboço ou exemplo simples) a **Árvore de Recursão** para um pequeno $M$. Destaque onde o **reprocessamento** dos subproblemas sobrepostos ocorre.
      * Explique por que esta abordagem tem uma complexidade de tempo **exponencial** e é inaceitável para valores grandes de $M$.

* Função 3: Recursiva com Memoização (Top Down)
  * **Conceito:** Descreva o mecanismo de **Memoização** (usando um *cache* ou dicionário). Como isso se relaciona com a Recursão Pura?
  * **Ligação com a PD:** Explique por que a Memoização é considerada uma forma de Programação Dinâmica (**Top Down**).
  * **Melhoria na Eficiência:** Explique como a Memoização elimina o reprocessamento, reduzindo drasticamente a complexidade.
  * **Complexidade:** Apresente a complexidade de tempo.

* Função 4: Programação Dinâmica (Bottom Up)
  * **Conceito:** Descreva o mecanismo de **Programação Dinâmica *Bottom Up***. O que a tabela/vetor $\mathbf{dp}$ armazena em cada índice $i$?
  * **Fluxo do Algoritmo:** Explique como a solução para um montante $i$ é construída de forma iterativa a partir das soluções *já calculadas* para montantes menores ($i - \text{moeda}$).
  * **Vantagem sobre Memoização:** Mencione a pequena vantagem de performance (se houver) do *Bottom Up* sobre o *Top Down* em relação à sobrecarga de chamadas recursivas.
  * **Complexidade:** Apresente a complexidade de tempo.

3. Conclusão

* **Resumo Comparativo:** Apresente uma tabela comparativa com as complexidades de tempo das quatro abordagens implementadas.
* **Escolha Ótima:** Qual é o algoritmo mais eficiente e robusto para resolver o Problema da Troca de Moedas e por quê?
* **Reflexão:** Conclusão geral sobre a importância da Programação Dinâmica na resolução de problemas de otimização onde há subestrutura ótima e subproblemas sobrepostos.

---

# ENTREGA: 

1. Entregar o link do github do repositório do projeto
2. O repositório do github deverá conter os códigos em python e no arquivo ```readme.md``` o relatório. IMPORTANTE: **Informar todos os integrantes do grupo (RA e NOME COMPLETO)**.  
3. O Checkpoint poderá ser realizado em grupo de até 4 integrantes.
4. A entrega deverá ser feita por apenas um integrante do grupo.

> QUE A FORÇA DA PROGRAMAÇÃO DINÂMICA ESTEJA COM TODOS!
