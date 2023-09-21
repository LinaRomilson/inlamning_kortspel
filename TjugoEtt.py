from Kortlek import Kortleken
from Spelare import Spelarna
import os
import time


def main():
    # Skapa en kortlek och blanda den
    kortlek = Kortleken()
    kortlek.blanda()

    # Skapa en spelare som användaren döper och en datorspelare
    spelare_namn = input("Vad heter du? ")
    spelare = Spelarna(spelare_namn)
    dator = Spelarna("datorn")

    # Skapa en evig loop så att spelet fortsätter efter första draget
    while True:
        # Rensa terminalen
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')

        # Spelarna drar ett varsitt kort
        spelare.dra_kort(kortlek)
        if dator.räkna_poäng() < 17:
            dator.dra_kort(kortlek)

        # Visa spelarnas händer, endast datorns första kort
        print(f"{spelare_namn}s hand: {', '.join(spelare.hand)} ({spelare.räkna_poäng()} poäng)")
        time.sleep(1)       # Väntar 1 sekund innan det går vidare
        print(f"Datorns hand: {', '.join(dator.hand[:1])} och {len(dator.hand) - 1} fler")
        time.sleep(2)       # Väntar 2 sekunder innan det går vidare
        # Kolla om någon har vunnit
        avslutat = avsluta_spelet(spelare_namn, spelare.räkna_poäng(), dator.räkna_poäng())
        # Om vinnaren är hittad ska spelet avslutas
        if avslutat:
            break

        spela_igen = input("Vill du dra ett kort till? (ja/nej) ")
        if spela_igen.lower() != "ja":
            # Om datorn har mindre än 17 poäng, fortsätt dra kort
            while dator.räkna_poäng() < 17:
                dator.dra_kort(kortlek)
                time.sleep(2)   # Väntar 2 sekunder innan det går vidare
                print(f"Datorns hand: {', '.join(dator.hand)} ({dator.räkna_poäng()} poäng)")

            # Kolla om någon har vunnit efter att datorn har dragit sina kort
            avslutat = avsluta_spelet(spelare_namn, spelare.räkna_poäng(), dator.räkna_poäng())
            # Avsluta om vinnaren är hittad
            if avslutat:
                break

            if spelare.räkna_poäng() < dator.räkna_poäng():
                print(f"Datorn vann! (Datorns poäng: {dator.räkna_poäng()} {spelare_namn}s poäng: {spelare.räkna_poäng()})")
                break
            elif dator.räkna_poäng() > spelare.räkna_poäng():
                print(f"{spelare_namn} vann! (Datorns poäng: {dator.räkna_poäng()} {spelare_namn}s poäng: {spelare.räkna_poäng()})")
                break

            # Avsluta loopen om spelaren inte vill dra fler kort
            #break
        else:
            print("-" * 10 + "Nästa omgång" + "-" * 10)


# Metod för att eventuellt avsluta spelet om någon spelare har vunnit
def avsluta_spelet(spelare_namn, spelare_poäng, dator_poäng):
    if spelare_poäng == 21 and dator_poäng == 21:
        print("Datorn vann! Nästa gång tar du det", spelare_namn)
        return True
    elif spelare_poäng == 21:
        print(f"{spelare_namn} vinner med exakt 21 poäng!")
        return True
    elif dator_poäng == 21:
        print("Datorn vinner med exakt 21 poäng!")
        return True
    elif spelare_poäng > 21 and dator_poäng > 21:
        print("Det blev lika (båda har över 21)!")
        return True
    elif spelare_poäng > 21:
        print(f"Datorn vann! ({spelare_namn} har över 21)")
        return True
    elif dator_poäng > 21:
        print(f"{spelare_namn} vinner! (Datorn har över 21)")
        return True
    return False


if __name__ == "__main__":
    main()
