#!/usr/bin/env python3

if __name__ == "__main__":

    total = 12
    delivery_fee = 2.5

    try:
        pizzas = int(input('How manny pizzas ordered? '))
    except ValueError:
        pizzas = int(input('Enter a valid positive number. '))
    total = (total * pizzas)

    try:
        tuesday = str(input('Is it Tuesday? '))
    except TypeError:
        tuesday = str(input('Please enter y or n '))
    if tuesday == 'y':
        total = total * 0.5

    try:
        app = str(input('Was pizza ordered using app? '))
    except TypeError:
        app = str(input('Please answer y or n'))
    if app == 'y':
        total = total * 0.75

    if pizzas >= 5:
        delivery_fee = 0

    try:
        delivery = str(input('Is delivery required? '))
    except TypeError:
        delivery = str(input('Please answer with y or n. '))
    if delivery == 'y':
        total = (total + delivery_fee)

    print(f'The total will be {total}. ')
