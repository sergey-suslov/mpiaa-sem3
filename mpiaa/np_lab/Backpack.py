from .funcs import custom_sum


class Backpack:

    def __init__(self, avalible_weight, items=[]):
        self.avalible_weight = avalible_weight
        self.items = items
        self.current_weight = 0
        self.full_price = custom_sum(items, lambda item: item.price)

    def insert(self, item):
        if item.weight + self.current_weight <= self.avalible_weight:
            self.items.append(item)
            self.current_weight += item.weight
            self.full_price += item.price
        else:
            return None
