limite = int(input("Entrez un nombre limite : "))

somme = 0

for i in range(0, limite + 1, 2):
    somme = somme + i
    print(somme)

print("La somme est égale à", somme)
