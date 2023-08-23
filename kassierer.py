from spieler import Spieler
from decimal import Decimal

class Kassierer(Spieler):

    def __init__(self, name: str, cakes_with_prices: tuple):
        super().__init__(name)
        self.cakes_with_prices = cakes_with_prices
        self.changeMoney = [Decimal(str(value)) for value in [50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]]

    def calculatePrice(self, kuchen: str, numberOfCoffee: int):
        price = 0
        for i in self.cakes_with_prices:
            if i[0] == kuchen:
                price += i[1]
        price += numberOfCoffee * 1.00
        print(f"Das macht dann {price}€, bitte.")
        return price

    def calculateChange(self, money: float, price: float):
        money_float = money
        price_float = price

        money_decimal = Decimal(str(money_float))
        price_decimal = Decimal(str(price_float))

        change = money_decimal - price_decimal
        # find the biggest coin or bill that is smaller than the change
        for i in self.changeMoney:
            if i <= change:
                # calculate how many of this coin or bill fit into the change
                numberOfCoins = int(change // i)
                # calculate the new change
                change -= numberOfCoins * i
                # print the change
                print(f"Hier sind {numberOfCoins} x {i}€")
        return change
