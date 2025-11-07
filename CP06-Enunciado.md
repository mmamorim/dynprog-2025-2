<img src="/assets/teste.svg" width="100%">

# DYNAMIC PROGRAMMING 2025/2

| Checkpoint | 6 | ```CURSO:``` | ENGENHARIA DE SOFTWARE |
|---|---|---|---|
| ```DISCIPLINA:``` | DYNAMIC PROGRAMMING | ```PROFESSOR:``` | Marcelo Amorim |


# 🎒 ✨💰 O Desafio da Mochila 0/1
---

Para explorar os conceitos de Recursão, Memoização, Programação Dinâmica e Heurísticas, usaremos como estudo de caso o clássico **Problema da Mochila 0/1**.

## 1.1. Contexto e Enunciado

Imagine que você tem uma **mochila com capacidade de carga limitada ($W$)**. Você tem à sua disposição uma lista de itens distintos, cada um com seu próprio **peso ($p_i$)** e **valor ($v_i$)**.

A restrição crucial é o **formato 0/1**: para cada item, você deve decidir se o inclui completamente (1) ou se o deixa de fora (0). Não é possível levar frações de um item, nem múltiplas cópias dele.

#### **Objetivo:** 
#### Escolher um subconjunto de itens tal que o **valor total seja maximizado**, e a **soma dos pesos não exceda a capacidade $W$** da mochila.

### 1.2. Conjunto de Dados de Exemplo

Para ilustrar as diferentes abordagens, utilizaremos o seguinte cenário:

* **Capacidade Máxima da Mochila ($W$):** 6 kg
* **Itens Disponíveis:**

| Item | Peso ($p_i$) | Valor ($v_i$) |
| :---: | :---: | :---: |
| A | 2 | 10 |
| B | 3 | 12 |
| C | 4 | 20 |
| D | 1 | 3 |


### 1.3. Análise Manual de Soluções Possíveis

A solução ótima para este problema é **Valor 30** (escolhendo Itens A e C).

| Itens Selecionados | Peso Total | Valor Total | Viável? (Peso $\le 6$) | Observação |
| :---: | :---: | :---: | :---: | :---: |
| B + D | 4 | 15 | Sim | Viável. |
| A + B + D | 6 | 25 | Sim | Boa, mas não ótima. |
| **A + C** | **6** | **30** | **Sim** | **SOLUÇÃO ÓTIMA!** |
| B + C | 7 | 32 | Não | Excede o peso. |


---

# MISSÃO DESTE CHECKPOINT

Você deverá implementar **quatro funções em python** que recebe como parâmetros a **Capacidade Máxima da Mochila ($W$):** e **Itens Disponíveis:** Peso e Valor de cada item. As funções devem retornar o valor total maximizado, onde a soma dos pesos não exceda a capacidade W da mochila.

***

**Funções a serem entregues**

1. Função iterativa (estratégia gulosa)
2. Função recursiva pura (sem memoização)
3. Função recursiva (com memoização) (Top down)
4. Função usando Programação Dinâmica (Bottom up)

#### Exemplo de Entrada (Estrutura Python)

~~~py
pesos = [2, 3, 4, 1]
valores = [10, 12, 20, 3]
capacidade_max = 6
~~~

Exemplo de cabeçalho das funções e possíveis chamadas:
~~~py
knapsack(pesos, valores, W) #Função iterativa estratégia gulosa
knapsackRec(pesos, valores, W) #Função recursiva simples
knapsackMemo(pesos, valores, W) #Função recursiva com memoização
knapsackPD(pesos, valores, W) #Função usando Programação Dinâmica
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
* O Problema da Mochila 
    * **Contextualização:** Apresente o problema de forma clara: Qual é o objetivo principal (maximizar o valor total)? Quais são as premissas (pesos, valores inteiros)?
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
