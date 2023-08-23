from spieler import Spieler

class Berater(Spieler):

    def __init__(self, name: str):
        super().__init__(name)
        self.cakes_with_prices = (
        ("Chocolate Cake", 4.50),
        ("Vanilla Cake", 3.00),
        ("Strawberry Cake", 4.00),
        ("Red Velvet Cake", 3.20),
        ("Carrot Cake", 2.50)
    )
    def getCakes(self):
        return self.cakes_with_prices

    def beraten(self):
        for i in self.cakes_with_prices:
            print(f"{self.cakes_with_prices.index(i)}. {i[0]}")

    def getKuchen(self, kuchen: int):
        print(f"{self.name} serviert {self.cakes_with_prices[kuchen][0]}")
        return self.cakes_with_prices[kuchen][0]
