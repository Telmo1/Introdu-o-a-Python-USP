def maior_primo(n):
    primos = []
    for num in range(2, n + 1):
        is_primos = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_primos = False
                break
        if is_primos:
            primos.append(num)
    if not primos:
        return None
    else:
        return max(primos)

num = int(input("Digite um número: "))
maior = maior_primo(num)
if maior is None:
    print("Não há números primos menores ou iguais ao número digitado.")
else:
    print(f"O maior número primo menor ou igual ao {num} é {maior}.")