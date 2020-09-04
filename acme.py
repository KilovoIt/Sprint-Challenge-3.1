import random


class Product:
    def __init__(self, name, price=10, weight=20,
                 flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        """instantiation"""
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = int(identifier)

    def stealability(self):
        """calculating stealability"""
        st = self.price/self.weight
        if st < 0.5:
            return 'Not So Stealable'
        if ((st >= 0.5) and (st < 1.0)):
            return 'Kinda Stealable'
        else:
            return 'Very Stealable!'

    def explode(self):
        """calculating explosiveness"""
        exp = self.flammability * self.weight
        if exp < 10:
            return '...fizzle.'
        if ((exp >= 10) and (exp < 50)):
            return '...boom!'
        else:
            return '...BABOOM!'


class BoxingGlove(Product):
    """adding and inherited class"""
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        """replacing an existing definition fo the explode method"""
        return "..it's a glove."

    def punch(self):
        """adding a new method"""
        if self.weight < 5:
            return 'That tickles.'

        if ((self.weight >= 5) and (self.weight < 15)):
            return 'You hit like a girl.'

        else:
            return "You wanna piece of me? You and me, let's roll!"
