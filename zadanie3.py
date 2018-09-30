cenaPodstawowa=int (input("Podstawowa cena samochodu: "))

podatek=cenaPodstawowa*0.05
print("Podatek wynosi 5%:  ", podatek)

oplataRejestracyjna= cenaPodstawowa*0.02
print("Opłata rejestracyjna 2%:  ", oplataRejestracyjna)

prowizjaPrzygotowawcza= 100
print ("prowizja przygotowawcza: ", prowizjaPrzygotowawcza)

doreczenie= 200
print ("doręczenie: ", doreczenie)

total = cenaPodstawowa + podatek + + oplataRejestracyjna + prowizjaPrzygotowawcza + doreczenie

print ("Faktyczna cena samochodu wynosi:  ", total)
