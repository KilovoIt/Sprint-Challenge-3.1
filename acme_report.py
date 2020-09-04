import random
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Oppressor_MKII']


def generate_products(num_products=30):
    """Creating four lists here for each computated parameter"""
    products = []
    weights = []
    price = []
    flammability = []
    counter = 0
    summary = []
    while counter < 30:
        """Cycle that randomizes each"""
        a = ADJECTIVES[random.randint(0, (len(ADJECTIVES)-1))] + " " +
        NOUNS[random.randint(0, (len(NOUNS)-1))]
        price_prod = random.randint(5, 100)
        weight_prod = random.randint(5, 100)
        flammability_prod = random.uniform(0.0, 2.5)
        products.append(str(a))
        weights.append(weight_prod)
        price.append(price_prod)
        flammability.append(flammability_prod)
        counter += 1
    """use summary list to pass randomized variables to the next stage"""
    summary = [products, weights, price, flammability]
    return summary


def inventory_report(summary):
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    """counting how many unique values do I have in names"""
    a_set = set(summary[0])
    unique = len(a_set)
    print('Unique product names: ', unique)
    """calculating average, output"""
    print('Average weight: ', sum(summary[1])/len(summary[1]))
    print('Average price: ', sum(summary[2])/len(summary[2]))
    print('Average flammability: ', sum(map(float, summary[3])) /
          len(summary[3]))

if __name__ == '__main__':
    inventory_report(generate_products())
