import random
import json


def make():
    orders = []
    for i in range(100):
        orderNo = 1000 + i
        address = str(random.randint(1, 5)) + '번지역'
        order = {"orderNo": orderNo, "address": address}
        orders.append(order)

    with open('input.json', 'w') as f:
        f.write(json.dumps({'orders': orders}, indent=2))
    f.close()


def __main__():
    make()
