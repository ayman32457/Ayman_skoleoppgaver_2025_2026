import random
# Definer partiene og lagre stemmer for hver
partier = {"Ap": 0,"Høyre": 0,"FrP": 0,"SV": 0,"Venstre": 0}


# Manuell stemming
print("Skriv inn et parti å stemme på (Q for å avslutte).")
print("Tilgjengelige partier:")
for parti in partier:
    print(parti)
 
while True:
    valg = input("Stem på et parti: ")
    if valg.lower() == "q":# avslutt løkken hvis brukeren skriver Q
        break
    elif valg in partier:
        partier[valg] += 1 # legg til stemme for valgt parti
        print(f"Ditt stemme: {valg}!")
    else:
        print("Ikke et parti, prøv igjen.")
 
total_stemmer = sum(partier.values())
 
print(f"Totalt antall stemmer: {total_stemmer}")

# Funksjon som simulerer et valg med n tilfeldige stemmer
def simuler_valg(n):
    stemmer = {p: 0 for p in partier} # start med 0 stemmer for alle partier
    for _ in range(n):
        valgt = random.choice(list(partier.keys()))  # tilfeldig parti får en stemme
        stemmer[valgt] += 1

    total = sum(stemmer.values())
    prosent = {p: (stemmer[p] / total) * 100 for p in stemmer} # regn ut prosent

    vinner, koalisjon = beregn_vinner(stemmer) # finn vinner eller koalisjon

    print("\nResultat fra simulering:")
    for p in stemmer:
        print(f"{p}: {stemmer[p]} stemmer ({prosent[p]:.2f}%)")
    print(f"\nVinner: {vinner} ({', '.join(koalisjon)})")


    # Lagre til fil
    lagre_resultat("valgresultater.txt", stemmer, prosent, vinner, koalisjon)

def beregn_vinner(stemmer):
    total = sum(stemmer.values())
    # Sjekk om et parti har flertall (>50%)
    for p, s in stemmer.items():
        if s > total / 2:
            return p, [p]
    # Ellers koalisjon av to største partier
    sortert = sorted(stemmer.items(), key=lambda x: x[1], reverse=True)
    top2 = [sortert[0][0], sortert[1][0]]
    return "Koalisjon", top2

def lagre_resultat(filnavn, stemmer, prosent, vinner, koalisjon):
    with open(filnavn, "a", encoding="utf-8") as f:
        f.write("=== hver simmulering ===\n")
        for p in stemmer:
            f.write(f"{p}: {stemmer[p]} stemmer ({prosent[p]:.2f}%)\n")
        f.write(f"Vinner: {vinner}\n")
        f.write(f"Koalisjon: {', '.join(koalisjon)}\n\n")

# Eksempel: simuler 100 personer
simuler_valg(100)


  

  



    














