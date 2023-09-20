import random

class Spelare:
    def __init__(self,namn):
        # Skapar attributen: namn och en lista för korten på handen
        self.namn = namn
        self.hand = []

    def dra_kort(self,kortlek):
        # Metod för att dra ett slumpmässigt kort från kortleken
        if len(kortlek) > 0:
            index = random.randint(0, len(kortlek) - 1)         # -1 eftersom index börjar på 0 och inte 1 som antalen kort gör
            kort = kortlek.pop(index)
            self.hand.append(kort)
            return kort
        else:
            return "Tom kortlek"

