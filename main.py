print("Velkommen til valget 2025 stortinget") #skriver ut til brukeren
start = input("Trykk enter for å fortsette") # viser teksten og venter at brukeren skal trykke 
if start == "": #sjekker om brukeren har trykket enter
    print("Velkommen til valget 2025 stortinget")
    print("Her er en liste over partiene du kan stemme på:") 
    print("Ap, FrP, Vp, SV, H, KrF, Sp, MDG")
# alt her kommer up etter enter er trykk
partier = ["Ap", "FrP", "Vp", "SV", "H", "KrF", "Sp", "MDG"] # her er en liste over parti
valg = input("Hvilket parti vil du stemme på?") #venter på at jeg velger også valg er variblen som lagrer svaret


# gjør til små bokstaver slik at input ikke feiler
valg = valg.lower()  # her ser man at jeg gjør svaret til små bokstaver fordi valg kan vere ap,Ap 
partier = [p.lower() for p in partier] # her gjør at alt blir små bokstaver i listen

if valg in partier: # sjekker om valg er i listen partier og if er en betingelse og in er for å sjekke om noe er i noe
    print(f"Du har valgt å stemme på {valg.upper()}. Takk for din stemme!") # her skrev jeg at den skal skrive ut en mld, valg.upper gjør at det blir stor bukstav, f er for å ik bruke + eller str 
    if valg == partier[0]:
        print("Du har stemt på Ap.")
    
    elif valg == partier[1]:
        print("Du har stemt på FrP.")
    elif valg == partier[2]:
        print("Du har stemt på Vp.")
    elif valg == partier[3]:
        print("Du har stemt på SV.")
    elif valg == partier[4]:
        print("Du har stemt på H.")
    elif valg == partier[5]:
        print("Du har stemt på KrF.")
    elif valg == partier[6]:
        print("Du har stemt på Sp.")
    elif valg == partier[7]:
        print("Du har stemt på MDG.") 
        # her er elif som betyr else if og det er for å sjekke flere betingelser
else:
    print("feil svar, prøv igjen")
# her er det en som skriver ut hvis jeg har skrevet feil

# Legg til enkel telling av stemmer
stemmer = [0] * len(partier) # her putter vi en tom liste med 0 som at alle starter med 0 stemmer
if valg in partier: # sjekker om hvis vlegeren har valgt et eksisterend oartj 
    indeks = partier.index(valg) #finner hvilke plass i listen som har blitt valgt
    stemmer[indeks] += 1 #kegger tik en stemme til det partiet
    print("\nStemmetelling:")#\n betyr ny linje 
    for i in range(len(partier)): #går gjennom alle partiene en etter en 
        print(f"{partier[i].upper()}: {stemmer[i]}") #skriver ut partiet og hvor mange stemmer de har fått og (upper)gjør at den blir stor bokstav


#her skal jeg legge til % til stemmene
total_stemmer = sum(stemmer) # legger sammen alle stemer 
print("\nProsentandel per parti:") # ny linje
for i in range(len(partier)): #lager løkke også tar vi en variable også lager vi range som går gjennom alle partiene imens len=lengde 
    if total_stemmer > 0:  # unngå å dele på 0
        prosent = (stemmer[i] / total_stemmer) * 100 # regner ut prosentandelen
    else:
        prosent = 0 #hvis ingen stemmer da er prosent 0 
    print(f"{partier[i].upper()}: {prosent:.2f}%") # skriver ut partiet og prosentandelen med 2 desimaler

#her skal jeg lage del 3 
import random # her henter vi inn random fra py biblio 

# Legg til mulighet for å velge antall velgere i simuleringen
antall_velgere = int(input("\nHvor mange personer skal stemme i simuleringen? ")) # ingput er for at brukeren skal skrive inn nie #int er for å gjøre svaret til et tall 
partier = ["Ap", "FrP", "Vp", "SV", "H", "KrF", "Sp", "MDG"] #dette er en liste 
stemmer = [0] * len(partier) # len er antall antall partier i listen, [0] x * 8 lager en liste mred 8 nuller

for _ in range(antall_velgere):  #for løkke som går gjennom velgere, for range() lager tall fra 0 til antall velgere, _ er en variabel som vi ikke bruker
    valg = random.choice(partier) # velger en random parti fra listen vi har laget 
    indeks = partier.index(valg) # finner plassnumber til partiene i listen, som sier hvis frp er 2 plass i listen da er indeks 2
    stemmer[indeks] += 1 # øker stemmer til det partiet som har blit valg 

print("\nStemmetelling etter simulering:") # skriver en overskrift 
for i in range(len(partier)): # her er løkke som skal gå gjennom alle partiene 
    print(f"{partier[i]}: {stemmer[i]} stemmer") #skriver ut hvormange stemmer hvert parti har fptt, f er at jeg trenger ikke å bruke + eller str()

# prosentandel
total_stemmer = sum(stemmer) # legger sammen alle stemmer 
print("\nProsentandel per parti:") # ny linje
for i in range(len(partier)): # lager løke som går gjenom alle partiene
    prosent = (stemmer[i] / total_stemmer) * 100 # regner ut prosentandelen
    print(f"{partier[i]}: {prosent:.2f}%") # skriver ut navnet på partiet (partier[i]) og prosentandelen (prosent), .2f betyr at du skal få 2 desimaler 

# finne vinner enkelt
maks_stemmer = max(stemmer) #max() finner det høyeste tallet i listen (variablen stemmer)
vinner_index = stemmer.index(maks_stemmer) # finner hvike parti som har fått flest stemer 
print(f"\nVinner av det simulerte valget: {partier[vinner_index]} med {maks_stemmer} stemmer") # skriver ut hvem som vant, partier[vinner_index] finner navn på hvem som vant, maks_stemmer er hvor mange stemmer de fikk

# lagre resultater i en fil
fil_navn = "results.txt" # lagrer navnet på filen vi skal skrive til 

with open(fil_navn, "w") as fil: # "w" åpmer en fil for skring 
    fil.write("Stemmetelling etter simulering:\n") # ny linje og skriver stemmetelling 
    for i in range(len(partier)): # løkke som går gjennom alle igjen
        fil.write(f"{partier[i]}: {stemmer[i]} stemmer\n") # skriver partinavn og antall stemmer inn i filen

    fil.write("\nProsentandel per parti:\n") #skriver overskrift i filen
    for i in range(len(partier)): #løkke som går gjennom alle partiene
        prosent = (stemmer[i] / total_stemmer) * 100 #regner prosent igen 
        fil.write(f"{partier[i]}: {prosent:.2f}%\n") #skriver prosent til filen med 2 desimaler 

    fil.write(f"\nVinner av det simulerte valget: {partier[vinner_index]} med {maks_stemmer} stemmer\n") # skriver til filen hvem som vant 
    print(f"\nResultatene er lagret i filen '{fil_navn}'") # skriver ut en melding til brukeren at filen er lagret
