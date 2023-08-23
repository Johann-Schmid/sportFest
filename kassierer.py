from spieler import Spieler

class Kassierer(Spieler):

    def __init__(self, name: str, cakes_with_prices: tuple):
        super().__init__(name)
        self.cakes_with_prices = cakes_with_prices
        self.changeMoney_float = [50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

    def calculatePrice(self, kuchen: str, numberOfCoffee: int):
        price = 0
        for i in self.cakes_with_prices:
            if i[0] == kuchen:
                price += i[1]
        price += numberOfCoffee * 1.00
        print(f"Das macht dann {price}€, bitte.")
        return price

    def calculateChangeMoney(self, money: float, price: float):
        change = money - price
        print(f"Hier ist ihr Wechselgeld von {round(change,2)}€, bitte.")

    def calculateChange(self, money: float, price: float):
        change = money - price
        # find the biggest coin or bill that is smaller than the change
        for i in self.changeMoney_float:
            if i <= change:
                # calculate how many of this coin or bill fit into the change
                numberOfCoins = int(change // i)
                # calculate the new change
                change = round(change - numberOfCoins * i, 2)
                # print the change
                print (change)
                print(f"Hier sind {numberOfCoins} x {i}€")
        return change
