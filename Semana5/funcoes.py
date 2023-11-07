def somaDigitos(n, digito, soma_digitos = 0):
    if n < 0:
        print("Erro!")
    else:
        while n > 0:
            digito = n % 10 
            soma_digitos += digito 
            n //= 10   
