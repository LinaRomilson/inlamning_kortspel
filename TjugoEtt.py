from Kortlek import Kortleken
from Spelare import Spelarna
import os
import time


# Anpassad exception för tom input
class TomInputException(Exception):
    pass


# Funktion för att kontrollera om input är tom
def kontrollera_input(data):
    if not data:
        # Är input tom skapas undantag
        raise TomInputException('FEL: Input får inte vara tom.')


def main(spelare_namnet):
    # Skapa en frame
    ui_width = 40
    print("--- TjugoEtt ---".center(ui_width))
    print("-" * ui_width)
    print("Försök komma så nära 21 som möjligt.")
    print("Akta så att du inte får mer än 21 bara!")
    print("-" * ui_width)

    # Skapa en kortlek och blanda den
    kortlek = Kortleken()
    kortlek.blanda()

    while True:  # Om exception sker ska denna del upprepas
        # Namnge spelaren om den inte redan har ett namn
        if spelare_namnet is None:
            try:
                spelare_namnet = input("Vad heter du? ")
                # Rensa mellanslag för att kontrollera att text finns i inputen
                spelare_namn_utan_mellanslag = spelare_namnet.replace(" ", "")
                kontrollera_input(spelare_namn_utan_mellanslag)
                break  # Avsluta evighetsloopen om input inte är tom

            except TomInputException as e:
                print(e)

    # Skapa spelarna
    spelare = Spelarna(spelare_namnet)
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
        print(f"{spelare_namnet}s hand: {', '.join(spelare.hand)} ({spelare.räkna_poäng()} poäng)")
        time.sleep(1)  # Väntar 1 sekund innan det går vidare
        print(f"Datorns hand: {', '.join(dator.hand[:1])} och {len(dator.hand) - 1} fler")
        time.sleep(2)  # Väntar 2 sekunder innan det går vidare
        # Kolla om någon har vunnit
        avslutat = avsluta_spelet(spelare_namnet, spelare.räkna_poäng(), dator.räkna_poäng())
        # Om vinnaren är hittad ska spelet avslutas
        if avslutat:
            break
        while True:  # Om exception sker ska denna del upprepas
            try:
                spela_igen = input("Vill du dra ett kort till? (ja/nej) ")
                # Rensa mellanslag för att kontrollera att text finns i inputen
                spela_igen_utan_mellanslag = spela_igen.replace(" ", "")
                kontrollera_input(spela_igen_utan_mellanslag)
                break  # Avsluta evighetsloopen om input inte är tom

            except TomInputException as e:
                print(e)

        if spela_igen.lower() != "ja":
            # Om datorn har mindre än 17 poäng, fortsätt dra kort
            while dator.räkna_poäng() < 17:
                dator.dra_kort(kortlek)
                time.sleep(1)  # Väntar 1 sekunder innan det går vidare
            # print(f"Datorns hand: {', '.join(dator.hand)} ({dator.räkna_poäng()} poäng)")

            # Kolla om någon har vunnit efter att datorn har dragit sina kort
            avslutat = avsluta_spelet(spelare_namnet, spelare.räkna_poäng(), dator.räkna_poäng())

            # Avsluta om vinnaren är hittad
            if avslutat:
                break

            if spelare.räkna_poäng() < dator.räkna_poäng():
                print(
                    f"Datorn vann! (Datorns poäng: {dator.räkna_poäng()} {spelare_namnet}s poäng: {spelare.räkna_poäng()})")
                break
            elif dator.räkna_poäng() > spelare.räkna_poäng():
                print(
                    f"{spelare_namnet} vann! (Datorns poäng: {dator.räkna_poäng()} {spelare_namnet}s poäng: {spelare.räkna_poäng()})")
                break

        else:
            print("-" * 10 + "Nästa omgång" + "-" * 10)
    return spelare_namnet


# Metod för att eventuellt avsluta spelet om någon spelare har vunnit
def avsluta_spelet(spelare_namnet, spelare_poäng, dator_poäng):
    if spelare_poäng == 21 and dator_poäng == 21:
        print("Datorn vann! Nästa gång tar du det", spelare_namnet)
        return True
    elif spelare_poäng == 21:
        print(f"{spelare_namnet} vann med exakt 21 poäng!")
        return True
    elif dator_poäng == 21:
        print("Datorn vann med exakt 21 poäng!")
        return True
    elif spelare_poäng > 21 and dator_poäng > 21:
        print("Det blev lika (båda har över 21)!")
        return True
    elif spelare_poäng > 21:
        print(f"Datorn vann med {dator_poäng} poäng! ({spelare_namnet} har över 21)")
        return True
    elif dator_poäng > 21:
        print(f"{spelare_namnet} vann med {spelare_poäng} poäng! (Datorn har över 21)")
        return True
    return False


if __name__ == "__main__":
    # Startvärde på spelarens namn, för att det ska gå att spela igen utan att ange sitt namn igen
    spelare_namn = None
    while True:
        main(spelare_namn)
        # Fråga om spelaren vill spela igen
        SpelaIgen = input("Vill du spela igen? (ja/nej) ")
        # Om svaret är nej ska programmet avslutas
        if SpelaIgen.lower() == "nej":
            break
