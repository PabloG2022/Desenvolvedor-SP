a, b = 0, 1
n = int(input("Informe um número para verificar se pertence a sequencia Fibonacci: "))
while a < n:
    a, b = b, a + b
    print(a,b)
print(a == n)
