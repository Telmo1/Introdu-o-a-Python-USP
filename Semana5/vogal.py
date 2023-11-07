def vogal(letra):
    letra = letra.lower()
    vogais = 'aeiou'
    return letra in vogais

letra = input("Digite uma letra: ")
if vogal(letra):
    print(f"'{letra}' é uma vogal.")
else:
    print(f"'{letra}' é uma consoante.")
