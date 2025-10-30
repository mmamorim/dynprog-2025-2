<img src="/assets/teste.svg" width="100%">

# Aula 11 - 30/10 


# 🎒 ✨💰 O Desafio da Mochila 0/1

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

### 2.1. Solução Rápida, mas Não Ótima: A Heurística Gulosa (Iterativa)

#### **🤔 Pergunta:** 
#### Se a meta é o valor máximo, por que simplesmente não escolhemos os itens que oferecem o "melhor retorno por quilo"?

#### Conceito
Uma **Heurística** é um algoritmo prático que busca uma solução "suficientemente boa" de forma rápida, sem garantir a otimalidade. A **Abordagem Gulosa (Greedy)** é a heurística mais comum para este problema.

**Estratégia Gulosa Sugerida:**
1.  Calcular a razão **Valor / Peso** para cada item.
2.  Ordenar os itens do maior para o menor valor dessa razão.
3.  Incluir os itens na mochila nessa ordem até que a capacidade ($W$) seja atingida.

#### Aplicação ao Exemplo ($W=6$)

Primeiro, calculamos a razão $V/P$ para cada item:

| Item | Peso ($p$) | Valor ($v$) | Razão ($v/p$) |
| :---: | :---: | :---: | :---: |
| D | 1 | 3 | **3.0** |
| A | 2 | 10 | 5.0 |
| B | 3 | 12 | 4.0 |
| C | 4 | 20 | 5.0 |

**🚨 Reordenando e Aplicando a Estratégia:**

1.  **Item A (Razão 5.0):** Incluído.
    * **Mochila:** {A}
    * Peso Atual: 2
    * Capacidade Restante: 4
    * Valor Atual: 10
2.  **Item C (Razão 5.0):** Incluído (Peso 4 cabe em 4).
    * **Mochila:** {A, C}
    * Peso Atual: 6
    * Capacidade Restante: 0
    * Valor Atual: 30
3.  **Item B (Razão 4.0):** Excederia a capacidade.
4.  **Item D (Razão 3.0):** Excederia a capacidade.

**Resultado Guloso:** A Heurística Gulosa, neste caso, encontrou o valor **30** (Itens A e C).

---

### 🚨 Falha da Heurística Gulosa (Discussão Necessária)

* **Ponto Chave:** Embora a gulosa tenha encontrado a solução ótima no nosso exemplo *específico*, ela é conhecida por falhar no Problema da Mochila 0/1.
* **Discussão em Aula:** Apresente um contra-exemplo onde a gulosa falharia se houvesse um item de peso 1 e valor 1 (razão 1.0) e a capacidade fosse 6.

A heurística gulosa falha porque **não considera o futuro**. Uma escolha localmente ótima (alto $V/P$) pode consumir muito espaço e impedir a obtenção de um valor total maior através de uma combinação diferente de itens. Por isso, precisamos de algoritmos que garantam a otimalidade.


#### Exemplo de Entrada (Estrutura Python)

~~~py
pesos = [2, 3, 4, 1]
valores = [10, 12, 20, 3]
capacidade_max = 6
~~~

**Cabeçalho da Função a Ser Desenvolvida:**

~~~py
# Retorna o valor máximo que pode ser obtido.
# pesos: Pesos dos itens.
# valores: Valores dos itens.
# W: A capacidade W da mochila.

def knapsack(pesos, valores, W):
    # ... código a ser implementado ...
    return valor_total_otimo 
~~~

---


# Aulas futuras

### 2.2. Recursão Simples

### 2.3. Otimização 1: Memoização (Programação Dinâmica Top-Down)

### 2.4. Otimização 2: Programação Dinâmica (Bottom-Up)
