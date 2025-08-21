def fatorial(n):
    # Caso base
    if n == 0:
        return 1
    # Passo recursivo
    return n * fatorial(n - 1)
print(fatorial(5)) # Saída: 120

n = 10 
for i in range(1, 10):
    print("oi "+i)