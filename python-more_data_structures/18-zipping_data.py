#!/usr/bin/python3

def zipping_data(list1, list2):
    for a, b in zip(list1, list2):
        print('{}: R$ {}.'.format(a, b))


if __name__ == "__main__":
    products = ['Shirt', 'Pants', 'Sneakers', 'Cap']
    prices = [50.00, 80.00, 120.00, 25.00]
    products_prices = zipping_data(products, prices)
