n = int(input("Digite um número inteiro: "))

soma_digitos = 0

while n > 0:
    digito = n % 10 
    soma_digitos += digito 
    n //= 10  

print(soma_digitos)
