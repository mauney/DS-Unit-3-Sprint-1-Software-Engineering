#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # Generate and add random products.
    for _ in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        prod = Product(name=name, price=price, weight=weight,
                       flammability=flammability)
        products.append(prod)

    return products


def inventory_report(products):
    # Loop over the products to calculate the report.
    names = []
    prices = []
    weights = []
    flammabilities = []

    for product in generate_products():
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)

    num_unique_names = len(set(names))
    avg_price = sum(prices) / len(prices)
    avg_weight = sum(weights) / len(weights)
    avg_flammability = sum(flammabilities) / len(flammabilities)

    print('\nACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {num_unique_names}')
    print(f'Average price: {avg_price:.2f}')
    print(f'Average weight: {avg_weight:.2f}')
    print(f'Average flammability: {avg_flammability:.4f}\n')

if __name__ == '__main__':
    inventory_report(generate_products())
