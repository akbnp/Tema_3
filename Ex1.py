import random
import string

liste_cuvinte = ["Alex", "jucarie", "Victorie"]

def alegere_cuvant(liste_cuvinte):
    cuvant = random.choice(liste_cuvinte)
    return cuvant.upper()

def spanzuratoarea():
    cuvant = alegere_cuvant(liste_cuvinte)
    litere_din_cuvant = set(cuvant)
    alfabet = set(string.ascii_uppercase)
    litere_folosite = set()
    incercari = 8

    while len(litere_din_cuvant) > 0 and incercari > 0:
        print("Mai aveti", incercari, "incercari si ati folosit pana acum: ", " ".join(litere_folosite))
        cuvant_lista = [litere if litere in litere_folosite else "_" for litere in cuvant]
        print("Cuvant: ", " ".join(cuvant_lista))

        litera_alesa = input("Alegeti o litera: ").upper()
        if litera_alesa in alfabet - litere_folosite:
            litere_folosite.add(litera_alesa)
            if litera_alesa in litere_din_cuvant:
                litere_din_cuvant.remove(litera_alesa)
                print("")
            else:
                incercari = incercari - 1
                print("\nLitera", litera_alesa, "nu apartine cuvantului!")
        elif litera_alesa in litere_folosite:
            incercari = incercari - 1
            print("\nAti introdus deja aceasta litera!")
        else:
            print("\nAlegeti doar litere!")

    if incercari == 0:
        print("Haha, ati murit! Cuvantul era", cuvant)
    else:
        print("Felicitari, ati ghicit cuvantul", cuvant, "!")

spanzuratoarea()
