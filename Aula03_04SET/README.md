<img src="/assets/teste.svg" width="100%">

# Aula 03 - 04/09

## Recursão - A Revanche!

Voltando ao ponto onde o professor Francisco Elanio parou!!!
* [Slides prof. Francisco](../Aula01_21AGO/Aula2-Recursao.pdf) (Recursão)

--- 

### Exercícios sobre Recursão

Resolva os exercícios de duas formas: utilizando iteração e recursão.

##### 1. Contagem regressiva

Crie uma função que mostre na tela uma contagem regressiva de N até 0.

~~~py
def contagem(n):
    for i in range(n+1):
        print(n-i, end=" ")

contagem(5)
~~~

~~~py
def contagemRec(n):
    if n==0:
        print(n)
    else:
        print(n, end=" ")
        contagemRec(n-1)

contagemRec(5)
~~~

~~~py
def contagemRecAbner(n):
    if n<0:
        return
    print(n, end=" ")
    contagemRec(n-1)

contagem(5)
~~~

---

##### 2. Soma dos números naturais

Crie uma função que calcule a soma de todos os números inteiros de 1 até N.

~~~py
def somatoria(n):
    soma = 0
    for i in range(n+1):
        soma += i
    return soma

somatoria(7)
~~~

~~~py
def somatoriaRec(n):
    if n==0: return 0
    return n + somatoriaRec(n-1)

somatoriaRec(5)
~~~

---

##### 3. Potência de um número

Crie uma função que calcule a potência de um número inteiro N.

~~~py
def pot(x,n):
    valor = 1
    for i in range(n):
        valor *= x 
    return valor

pot(2,5)
~~~

~~~py
def potRec(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    return x*potRec(x,n-1)

potRec(2,5)
~~~

---

##### 4. Busca Sequencial

Crie uma função que verifique se um elemento está presente em uma lista.

~~~py
def busca(vet,elem):
    for i in range(len(vet)):
        if vet[i]==elem:
            return i
    return -1

busca([23,45,13,8,12,41], 40)
~~~

~~~py
def buscaRec(vet,elem):
    if len(vet) == 0:
        return -1
    if vet.pop() == elem:
        return len(vet)
    return buscaRec(vet,elem)

buscaRec([23,45,13,8,12,41], 13)
~~~

---

##### 5. Busca Binária

Crie uma função que verifique se um elemento está presente em uma lista usando a ideia de busca binária.


### Como melhorar uma função recursiva usando memoização???