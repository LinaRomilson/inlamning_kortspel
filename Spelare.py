import random


class Spelare:
    def __init__(self, namn):
        # Skapar attributen: namn och en lista för korten på handen
        self.namn = namn
        self.hand = []

    def dra_kort(self, kortlek):
        # Metod för att dra ett slumpmässigt kort från kortleken
        if len(kortlek) > 0:
            index = random.randint(0, len(kortlek) - 1)  # -1 eftersom index börjar på 0 och inte 1 som antalen kort gör
            kort = kortlek.pop(index)

            # Överstiger poängen 21 när 14 poäng läggs till A istället vara värt 1 poäng
            if kort.endswith("A") and self.räkna_poäng() + 11 > 21:
                kort = kort.replace("A", "1")

            # Vid A ska spelaren kunna välja värdet på kortet
            """
            if kort.ends_with("A"):
                val = input("Välj värdet på Ess:et (1/14): ")
                while val not in ("1", "14"):
                    val = input("Felaktigt val: Välj värdet på Ess:et (1/14): ")
                kort = kort.replace("A", val)
                """
            self.hand.append(kort)
            return kort
        else:
            return "Tom kortlek"

    def räkna_poäng(self):
        # Räkna poängen på korten spelarna har i handen
        poäng = 0

        for kort in self.hand:
            värde = kort.split()[0]     # Hämtar kortets värde
            if värde in "K":
                poäng += 13
            elif värde in "D":
                poäng += 12
            elif värde in "J":
                poäng += 11
            else:
                poäng += int(värde)

        return poäng
