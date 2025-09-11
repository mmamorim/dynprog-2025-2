<img src="/assets/teste.svg" width="100%">

# Aula 04 - 11/09

## Memoização em Funções Recursivas

# Aula: Memoização em Funções Recursivas no Python

## 1. Introdução
- **Problema comum**: Funções recursivas muitas vezes repetem cálculos já feitos.  
- **Exemplo**: Cálculo do n-ésimo número de Fibonacci de forma recursiva.  
- **Solução**: **Memoização** → técnica de otimização que armazena resultados intermediários para evitar recomputações.

---

## 2. Exemplo sem Memoização
~~~py
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Funciona rápido
print(fib(35))  # Fica lento!
~~~

- Problema: Para `fib(35)`, a função recalcula várias vezes o mesmo valor.  
- Complexidade: **O(2^n)**.

---

## 3. Exemplo com Memoização Manual
~~~py
memo = {}

def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

print(fib_memo(35))  # Muito mais rápido
~~~

- Agora, cada valor de `fib(n)` é calculado **apenas uma vez**.  
- Complexidade: **O(n)**.

---

## 4. Usando `functools.lru_cache`
O Python já traz uma solução pronta: `functools.lru_cache`.

~~~py
from functools import lru_cache

@lru_cache(maxsize=None)  # None = cache ilimitado
def fib_cache(n):
    if n <= 1:
        return n
    return fib_cache(n-1) + fib_cache(n-2)

print(fib_cache(35))  # Rápido e simples
~~~

- **Vantagem**: evita escrever código extra de cache.  
- `maxsize`: define limite do cache (ex: `128`).  
- `fib_cache.cache_info()`: mostra estatísticas (hits, misses, etc).


# Entendendo o `functools.lru_cache` no Python

## O que é?
- O `lru_cache` é um **decorador** da biblioteca padrão do Python (`functools`).  
- Ele implementa **memoização automática**, ou seja, armazena em cache os resultados de chamadas de função.  
- "LRU" significa **Least Recently Used** (menos recentemente usado):  
  quando o cache atinge o limite, os valores mais antigos são descartados.  

---

## Como usar
Basta importar e aplicar como decorador em uma função:

~~~py
from functools import lru_cache

@lru_cache(maxsize=None)  # None = cache ilimitado
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Calcula normalmente
print(fib(10))  # Recupera do cache (muito mais rápido)
~~~

---

## Parâmetros principais
- **`maxsize`**  
  - Define o número máximo de valores guardados.  
  - Exemplo: `@lru_cache(maxsize=128)` → guarda até 128 resultados.  
  - `None` = cache ilimitado.  

- **`typed`**  
  - Se `True`, considera tipos diferentes como entradas diferentes.  
  - Exemplo: `f(3)` e `f(3.0)` → seriam resultados distintos.  
  - Por padrão, `typed=False`.  

---

## Monitorando o cache
Funções decoradas ganham métodos especiais:

~~~py
print(fib.cache_info())
# Saída: CacheInfo(hits=9, misses=11, maxsize=None, currsize=11)

fib.cache_clear()  # Limpa todo o cache
~~~

- **hits** → quantas vezes encontrou no cache.  
- **misses** → quantas vezes precisou calcular.  
- **currsize** → quantos valores estão guardados.  
- **maxsize** → limite configurado.  

---

## Comparação de performance
~~~py
import time
from functools import lru_cache

def fib_no_cache(n):
    if n <= 1:
        return n
    return fib_no_cache(n-1) + fib_no_cache(n-2)

@lru_cache(maxsize=None)
def fib_cache(n):
    if n <= 1:
        return n
    return fib_cache(n-1) + fib_cache(n-2)

n = 35

# Sem cache
start = time.time()
fib_no_cache(n)
print("Sem cache:", time.time() - start, "s")

# Com cache
start = time.time()
fib_cache(n)
print("Com cache:", time.time() - start, "s")
~~~

➡️ Diferença: sem cache pode demorar **segundos**, com cache retorna em **milissegundos**.  

---

## Quando usar?
✅ Casos ideais:
- Funções recursivas com cálculos repetidos (ex.: Fibonacci, caminhos em grafos).  
- Funções "caras" (demoram para rodar) chamadas várias vezes com os mesmos parâmetros.  
- Consultas externas (ex.: API, banco de dados) que podem se repetir.  

⚠️ Evite usar se:
- A função depende de variáveis externas que mudam constantemente.  
- O resultado varia a cada chamada (ex.: `random()`, `time.now()`).  

---

## 5. Outros Exemplos de Uso
- **Fatorial** (não precisa muito, mas serve de exemplo).  
- **Problema do Troco** (quantas formas de dar troco com certas moedas).  
- **Programação dinâmica** em geral (caminhos em uma grade, subsequências, etc).

---

