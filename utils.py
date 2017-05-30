# TODO
def allocate_order():
    # 2. Parse data and make area
    area_1 = []
    area_2 = []
    area_3 = []
    area_4 = []
    area_5 = []

    for order in input_dict['orders']:
        if order['address'] == '1번지역':
            area_1.append(order)
        elif order['address'] == '2번지역':
            area_2.append(order)
        elif order['address'] == '3번지역':
            area_3.append(order)
        elif order['address'] == '4번지역':
            area_4.append(order)
        elif order['address'] == '5번지역':
            area_5.append(order)
        else:
            print('Parse error at {}'.format(order))
            exit()

    # print(area_1, len(area_1))
    # print(area_2, len(area_2))


def search(warehouse_list, order):
    # 가장 추가시간이 짧은 창고 찾기
    add_time_list = []
    for warehouse in warehouse_list:
        add_time = warehouse.get_additional_time(order)
        add_time_list.append(add_time)
    min_index, _ = min(enumerate(add_time_list), key=lambda p: p[1])
    return warehouse_list[min_index]
