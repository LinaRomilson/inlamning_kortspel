class Spelarna:
    def __init__(self, namn):
        # Skapar attributen: namn och en lista för korten på handen
        self.namn = namn
        self.hand = []

    def dra_kort(self, kortlek):
        # Metod för att dra ett slumpmässigt kort från kortleken
        kort = kortlek.dra_kort()
        if kort != "Tom kortlek":
            # Överstiger poängen 21 när 14 poäng läggs till ska A vara värt 1 poäng istället
            if kort.endswith("A") and self.räkna_poäng() + 14 > 21:
                kort = kort.replace("A", "1")
            self.hand.append(kort)
            return kort
        else:
            return "Tom kortlek"

    def räkna_poäng(self):
        # Räkna poängen på korten spelarna har i handen
        poäng = 0

        for kort in self.hand:
            värde = kort.split()[1]  # Hämtar kortets värde
            if värde in "K":
                poäng += 13
            elif värde in "D":
                poäng += 12
            elif värde in "J":
                poäng += 11
            else:
                poäng += int(värde)

        return poäng
