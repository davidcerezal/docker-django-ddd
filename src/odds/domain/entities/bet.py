class Bet(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def get_price(self):
        return self.price
