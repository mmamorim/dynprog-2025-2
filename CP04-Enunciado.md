<img src="/assets/teste.svg" width="100%">

# DYNAMIC PROGRAMMING 2025/2

| Checkpoint | 4 | ```CURSO:``` | ENGENHARIA DE SOFTWARE |
|---|---|---|---|
| ```DISCIPLINA:``` | DYNAMIC PROGRAMMING | ```PROFESSOR:``` | Marcelo Amorim |


# 👑 Em busca da Coroa de Pedra

Em um reino distante, dois irmãos disputam uma antiga tradição: o **Jogo das Pedras**.  
O jogo é simples, mas requer estratégia:

- Existe um monte com várias pedras.
- Os irmãos jogam alternadamente.
- Em cada jogada, um jogador pode retirar **1, 2 ou 3 pedras**.
- Quem retirar a **última pedra** é considerado o vencedor e recebe uma coroa simbólica.

Os habitantes do reino perceberam que, com um pouco de lógica, é possível **sempre ganhar** se você fizer as jogadas corretas.  
Sua missão é ajudar os irmãos a determinar, para qualquer número de pedras, se o jogador da vez **tem uma estratégia vencedora**, assumindo que ambos jogam de forma ótima.


# Como funciona o Jogo das Pedras 👑🪨

O Jogo das Pedras é um jogo de estratégia simples, mas que exige raciocínio lógico para vencer. A seguir estão as regras detalhadas:

## Regras do Jogo

1. Existe um **monte com n pedras**.
2. Dois jogadores jogam **alternadamente**.
3. Em cada jogada, um jogador pode retirar **1, 2 ou 3 pedras** do monte.
4. Quem retirar a **última pedra** vence o jogo.
5. O jogador que não conseguir fazer uma jogada válida (quando não há pedras restantes) perde.

---

## Conceitos importantes

- **Posição vencedora (V):** É uma configuração do jogo em que o jogador da vez pode garantir a vitória se jogar de forma ótima.
- **Posição perdedora (P):** É uma configuração em que o jogador da vez **não pode vencer**, mesmo jogando da melhor forma possível.

### Exemplos de posições

### Exemplos de posições

| Pedras restantes | Tipo de posição | Comentário / Estratégia |
|-----------------|----------------|------------------------|
| 0               | P              | Sem pedras, jogador atual perde |
| 1               | V              | Pega a última pedra e vence |
| 2               | V              | Pega 2 pedras e vence |
| 3               | V              | Pega 3 pedras e vence |
| 4               | P              | Qualquer jogada deixa o oponente em V |
| 5               | V              | Tirar 1 deixa o oponente em 4 (P) |
| 6               | V              | Tirar 2 deixa o oponente em 4 (P) |
| 7               | V              | Tirar 3 deixa o oponente em 4 (P) |
| 8               | P              | Qualquer jogada deixa o oponente em V |
| 9               | V              | Tirar 1 deixa o oponente em 8 (P) |
| 10              | V              | Tirar 2 deixa o oponente em 8 (P) |
| 11              | V              | Tirar 3 deixa o oponente em 8 (P) |
| 12              | P              | Qualquer jogada deixa o oponente em V |
| 13              | V              | Tirar 1 deixa o oponente em 12 (P) |
| 14              | V              | Tirar 2 deixa o oponente em 12 (P) |
| 15              | V              | Tirar 3 deixa o oponente em 12 (P) |
| 16              | P              | Qualquer jogada deixa o oponente em V |


---

## Estratégia básica

A ideia principal do jogo é **deixar o oponente em uma posição perdedora (P)** sempre que possível.  
- Se você consegue fazer isso, independentemente da jogada do adversário, você garante a vitória.  
- Para o jogo clássico onde se pode retirar 1, 2 ou 3 pedras, a regra é: **tente sempre deixar múltiplos de 4 para o oponente**.

---

# MISSÃO DESTE CHECKPOINT

Você deverá implementar **uma função em python que determina se o jogador da vez tem estratégia vencedora** no Jogo das Pedras.  

A função deve ser capaz de resolver o problema de duas formas:

### 1. Função recursiva pura (sem memoização)

- Crie uma função `vence(n)` que recebe o número de pedras restantes `n`.  
- Utilize **recursão** para testar todos os movimentos possíveis (1, 2 ou 3 pedras).  
- Retorne:
  - `True` → se existe pelo menos um movimento que deixa o oponente em posição perdedora.  
  - `False` → se todos os movimentos deixam o oponente vencer.  

**Exemplo de chamada:**

~~~py
vence(4)  # False
vence(5)  # True
~~~

> ⚠️ Observação: Para valores grandes de `n`, a versão recursiva pura pode ser muito lenta.

---

### 2. Função recursiva com memoização

- Reescreva a função usando **memoização** para armazenar os resultados de subproblemas já calculados.  
- Você pode usar:
  - `functools.lru_cache`, **ou**
  - um **dicionário** para guardar resultados.  
- Com memoização, a função deve ser eficiente mesmo para valores grandes, por exemplo, `n = 10000`.  

**Exemplo com lru_cache:**

~~~py
from functools import lru_cache

@lru_cache(maxsize=None)
def vence(n: int) -> bool:
    # Implementação recursiva aqui
    ...
~~~

---

# ENTREGA: 

1. Entregar o link do github do repositório do projeto
2. O repositório do github deverá conter um arquivo ```readme.md``` informando todos os integrantes do grupo (RA e NOME COMPLETO).  
3. O Checkpoint poderá ser realizado em grupo de até 4 integrantes.
4. A entrega deverá ser feita por apenas um integrante do grupo.
5. O prazo para entrega é 22/09.

> QUE A FORÇA DA RECURSÃO ESTEJA COM TODOS!
