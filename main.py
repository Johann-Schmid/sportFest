from berater import Berater
from ausschenker import Ausschenker
from kassierer import Kassierer
from exception import NotEnoughMoney

def orderKuchen(Berater):
    while True:
        try:
            userInput = int(input("Welchen Kuchen möchtest du? "))
            if userInput < 0 or userInput > 4:
                raise IndexError
            cake = Berater.getKuchen(userInput)
            break
        except ValueError:
            print("Bitte gib eine Zahl ein!")
        except IndexError:
            print("Bitte gib eine Zahl zwischen 0 und 4 ein!")
    return cake

def orderCoffee(Ausschenker):
    while True:
        try:
            userInput = int(input("Welchen Kaffee möchtest du? "))
            if userInput < 1 or userInput > 10:
                raise IndexError
            Ausschenker.getCoffee(userInput)
            break
        except ValueError:
            print("Bitte gib eine Zahl ein!")
        except IndexError:
            print("Bitte gib eine Zahl zwischen 1 und 9 ein!")
    return userInput

def giveMoney(Kassierer, price: float):
    while True:
        try:
            userInput_str = input("Wie viel Geld gibst du? ")
            parts = userInput_str.split(".")
            if len(parts) > 2:
                raise ValueError
            if len(parts) == 2:
                if len(parts[1]) > 2:
                    raise ValueError
            userInput = float(userInput_str)
            if userInput < price:
                raise NotEnoughMoney
            Kassierer.calculateChange(userInput, price)
            break
        except ValueError:
            print("Bitte gib eine Zahl ein!")
        except NotEnoughMoney:
            print("Das ist zu wenig Geld!")
    return userInput

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    john = Berater("John")
    peter = Ausschenker("Peter")
    toni = Kassierer("Toni", john.getCakes())
    john.beraten()
    kuchen = orderKuchen(john)
    numberOfCoffee = orderCoffee(peter)
    price = toni.calculatePrice(kuchen, numberOfCoffee)
    giveMoney(toni, price)

