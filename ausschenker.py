from spieler import Spieler

class Ausschenker(Spieler):
    CANS = 5

    def __init__(self, name: str):
        super().__init__(name)
        self.__numberOfCans = self.CANS

    def getNumberofCans(self):
        return self.__numberOfCans

    def setNumberOfCans(self, numberOfCans: int):
        self.__numberOfCans = numberOfCans

    def getCoffee(self, coffee: int):
        currentNumberofCans = self.getNumberofCans()
        if currentNumberofCans <= coffee:
            self.cookCoffee(currentNumberofCans)
        self.setNumberOfCans(self.getNumberofCans() - coffee)
        print(f"{self.name} schenkt {coffee} Kaffee aus.")
        print(f"Jetzt sind {self.getNumberofCans()} Kaffee da.")

    def cookCoffee(self, currentNumberofCans: int):
        print(f"{self.name} kocht Kaffee.")
        self.setNumberOfCans(currentNumberofCans + self.CANS)
        print(f"Jetzt sind {self.getNumberofCans()} Kaffee da.")
