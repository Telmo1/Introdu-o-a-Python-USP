fat = int(input("Digite um número para saber o seu fatorial: "))
i = 1 
n = 1

if fat == 0:    
    fat = 1
    print(fat)
elif fat == 1:
    print(fat)   
else: 
   while i <= fat:
       n *= i
       i = i + 1

print(n)