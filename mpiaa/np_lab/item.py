class Item:
    def __init__(self, name, weight, price, number):
        self.weight = weight
        self.name = name
        self.price = price
        self.number = number
        self.price_cooficient = self.weight / self.price