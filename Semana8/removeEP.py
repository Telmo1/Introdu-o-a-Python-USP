def remove_repetidos(lista):
    return sorted(set(lista))

print(remove_repetidos([1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10]))
