import random
slowa=("python","gdansk","dlaczego","gdynia","wsb")
word = random.choice(slowa)
print(word)
poprawnie = word;
print("""Witaj w grze 'Wygenerowane slowo'! Uporządkuj litery, aby odtworzyć prawidłowe słowo.(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)""")
print("Wygenerowane slowo ma liter:", len(poprawnie))
pomie=""
for x in range(0, 5):
	zgaduj = input("\nEkstra litera! Sprawdz czy slowo ja zawiera: ")
	if poprawnie.count(zgaduj)>0:
		print("tak")
	else:
		print("nie")
zgaduj = input("\nTwojaodpowiedź: ")
ktoraProba = 0
superWynik = 0
while zgaduj != poprawnie and zgaduj != "":
	print("Niestety, to nie to słowo.")
	ktoraProba += 1
	zgaduj = input("Twoja odpowiedź: ")
	if zgaduj == poprawnie:
		print("Zgadza się! Zgadłeś!\n")
	else:
		if ktoraProba >= 3:
			print("pierwsza litera to: " , poprawnie[0])
			print("ostatnia litera to: " , poprawnie[len(poprawnie)-1])
if ktoraProba < 3:
	superWynik += 1
	print("Gratulacje, udalo ci sie zgadnac  w co najwyzej 3 probach. Twoj super wynik to: ", superWynik)
print("Dziękuję za udział w grze.")
