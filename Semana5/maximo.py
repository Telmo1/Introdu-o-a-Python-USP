def maximo(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

primeiroN = int(input("Digite um valor para o primeiro número: "))
segundoN = int(input("Digite um valor para o segundo número: "))

maiorN = maximo(primeiroN, segundoN)
print(maiorN)

