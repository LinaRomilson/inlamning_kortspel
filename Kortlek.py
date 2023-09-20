import random


class Kortlek:
    # Skapa kortleken
    def __init__(self):
        # Skapa en tom lista att placera korten i
        self.kort = []
        # Skapa en separat lista för färger & en separat lista för värdena
        färger = ["Hjärter", "Ruter", "Klöver", "Spader"]
        värden = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K", "A"]

        # Skapa varje enskilt kort med en nestlad for-loop
        for färg in färger:
            for värde in värden:
                self.kort.append(f"{färg} {värde}")

    def blanda(self):
        random.shuffle(self.kort)
