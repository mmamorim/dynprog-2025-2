<img src="/assets/teste.svg" width="100%">

# Aula 05 - 18/09 - Memoização - A Revanche!

---

# ✨💰 O Desafio do Troco

Você é o **caixa da lanchonete**.  
Tem apenas moedas de **1, 2 e 5 reais** no caixa.  

Um cliente pede **troco de 5 reais**.  

---

## ❓ Pergunta
> #### ⚡ De **quantas formas diferentes** você consegue entregar esse troco usando apenas essas moedas (podendo repetir)?  

---

# 🗣️ Perguntinhas Marotas

- 🔄 **Ordem importa?**  
  (Ex.: 2 + 1 + 2 é a mesma coisa que 1 + 2 + 2?)

- 🧩 **Como evitar contar a mesma combinação duas vezes?**

- 🪙 **Se eu já sei as maneiras de formar `n - 2`, isso ajuda a formar `n`?**

- 📊 **Onde aparecem subproblemas repetidos?**

- 🚀 **O que acontece se pedirmos troco de 50 ou 100 reais?**  
  (Dá para fazer na mão ou começa a ficar impossível?)


---

# Definição Formal do Problema

#### Enunciado
Dado um valor **N** e um conjunto de moedas **[m1, m2, ..., mk]**, de quantas formas diferentes é possível formar **N** usando essas moedas, podendo repetir moedas?

#### Recorrência

**contaTroco**(n, i) = **contaTroco**(n - moedas[i], i) + **contaTroco**(n, i+1)


#### Casos Base
- Se **n == 0** → existe **1 forma** (encontramos uma solução válida).  
- Se **n < 0** ou **i >= número de moedas** → existe **0 formas** (não há solução).  



---

# Primeira Tentativa: Recursão Pura 

Exemplo em Python:

~~~py
def formas_troco(n, moedas, i=0):
    if n == 0:
        return 1
    if n < 0 or i >= len(moedas):
        return 0
    # Usando a moeda atual + ignorando a moeda atual
    return formas_troco(n - moedas[i], moedas, i) + formas_troco(n, moedas,i+1)
~~~

### O que acontece se eu pedir troco de 100 reais?


# E com Memoização?

