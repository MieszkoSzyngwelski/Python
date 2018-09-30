import random
liczba = random.randint(1,10)
print("Wylsowanana liczba: ", liczba)


odp = input("Jaką liczbę od 1 do 49 wylosowano")

if liczba == int(odp):
	print("Udało się!")
else:
	print("Nie udało się!")


