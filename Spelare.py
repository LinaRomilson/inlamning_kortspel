class Spelarna:
    def __init__(self, namn):
        # Skapar attributen: namn och en lista för korten på handen
        self.namn = namn
        self.hand = []

    def dra_kort(self, kortlek):
        # Metod för att dra ett slumpmässigt kort från kortleken
        kort = kortlek.dra_kort()
        if kort != "Tom kortlek":
            self.hand.append(kort)
            return kort
        else:
            return "Tom kortlek"

    def räkna_poäng(self):
        # Räkna poängen på korten spelarna har i handen
        poäng = 0
        antal_ess = 0
        for kort in self.hand:
            värde = kort.split()[1]  # Hämtar kortets värde
            if värde in "K":
                poäng += 13
            elif värde in "D":
                poäng += 12
            elif värde in "J":
                poäng += 11
            elif värde == "A":
                poäng += 14  # Lägger till essets högsta värde till att börja med
                antal_ess += 1
            else:
                poäng += int(värde)

        # Om poängen överstiger 21 och det finns ess i handen ändras essets värde till 1
        while poäng > 21 and antal_ess > 0:
            poäng -= 13
            antal_ess -= 1

        return poäng
