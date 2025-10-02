<img src="/assets/teste.svg" width="100%">

# Aula 07 - 02/10 

---

# RESUMÃO

### Recursão
- Resolver problemas quebrando-os em subproblemas menores.  
- **Ex.:** Fibonacci, fatorial.  
- **Vantagem:** clareza do código.  
- **Desvantagem:** pode ser ineficiente.  

### Otimização com Memoização
- Guardar resultados já calculados (**cache**) para não recomputar.  
- Aplica-se em recursões com subproblemas repetidos.  
- **Ex.:** Fibonacci otimizado → O(n) em vez de O(2^n).  

### Programação Dinâmica (PD)
- Estratégia sistemática: resolver subproblemas menores e compor a solução.  
- Pode ser:
  - **Top-Down:** recursão + memoização.  
  - **Bottom-Up:** tabela iterativa.  
- **Usada em:** mochila, caminhos mínimos, alinhamento de sequências.  

#### Qual a diferença entre Memoização x Programação Dinâmica (PD) ?
> Memoização = recursivo + cache (top-down).
> PD = iterativo + tabela (bottom-up).
> **Ambos são programação dinâmica no sentido amplo, mas o estilo de implementação muda completamente.**

### Heurísticas
- Métodos aproximados quando solução exata é inviável (tempo/complexidade).  
- Baseadas em:
  - Regras práticas.  
  - Busca local.  
  - Algoritmos gulosos.  
  - Metaheurísticas (ex.: algoritmos genéticos, simulated annealing).  

---


# ✨💰 O Desafio do Moedas II - O Retorno

Você irá programar um **caixa eletrônico**. Esse caixa trabalha com apenas alguns tipos de notas. Como entregar a quantia correta para um saque contendo a menor quantidade de notas?   

**Enunciado**

Dado um valor **N** e um conjunto de moedas de valores **[c₁, c₂, …, cₖ]**, determine o **mínimo número de moedas** necessário para representar exatamente **N** (supondo disponibilidade ilimitada de cada tipo de moeda).

- **Entrada:** inteiro não negativo `N` e lista de inteiros positivos `moedas = [c1, c2, ..., ck]`.  
- **Saída:** inteiro — menor quantidade de moedas cuja soma é `N`, ou indicação que `N` não pode ser formado (ex.: `-1`).

**Exemplo:** `N = 6`, `moedas = [1, 3, 4]` → resposta: `2` (3 + 3).

---

## ❓ Pergunta
> #### ⚡ Qual a **melhor maneira** de entregar esse troco usando a menor quantidade de moedas?  

