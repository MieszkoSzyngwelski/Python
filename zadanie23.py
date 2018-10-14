import random
slowa = ("python","gdansk","dlaczego","gdynia","wsb")
word= random.choice(slowa)
#print(word)
poprawnie = word
pomie =""
while word:
	position = random.randrange(len(word))
	pomie+= word[position]
	word = word[:position] + word[(position + 1):]
print (pomie)
print("""
Witaj w grze 'Wymieszane litery'!  
Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz 
Enter bez podawania odpowiedzi.)
""")
print("Zgadnij, jakie to słowo:", pomie)
zgaduj = input("\nTwojaodpowiedź: ")
while zgaduj != poprawnie and zgaduj != "":
	print ("Niestety, to nie to słowo.")
	zgaduj = input("Twoja odpowiedź: ")
if zgaduj == poprawnie:
	print ("Zgadza się! Zgadłeś!\n")
print ("Dziękuję za udział w grze.")
