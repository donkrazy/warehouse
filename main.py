import json
from objects import Warehouse
from make_input import make

# 1. Get input data
try:
    f = open('input.json')
except FileNotFoundError:
    make()
    f = open('input.json')

input_dict = json.loads(f.read())

# 2. 창고 정보로 창고 생성
warehouse_info_list = [
    {'name': 'A', 'time_required': {'1': 10, '2': 25, '3': 30, '4': 50, '5': 60}, 'num_drons': 20},
    {'name': 'B', 'time_required': {'1': 20, '2': 10, '3': 20, '4': 40, '5': 55}, 'num_drons': 25},
    {'name': 'C', 'time_required': {'1': 60, '2': 40, '3': 25, '4': 15, '5': 20}, 'num_drons': 15},
]
warehouse_list = []
for warehouse_info in warehouse_info_list:
    warehouse = Warehouse(warehouse_info)
    warehouse_list.append(warehouse)
    print('CREATED: ', warehouse)

# 3. 각 창고에 최적의 주문 할당(greedy)
for order in input_dict['orders']:
    # 세 창고 중 추가 배송시간(marginal)이 적게 걸리는 최적의 창고 검색
    min_index, min_value = min(enumerate(warehouse_list), key=lambda p: p[1].get_additional_time(order))
    warehouse = warehouse_list[min_index]
    # 창고에 주문 할당
    warehouse.work(order)

# 4. reverse_jenga
    '''
    [TODO]
    generate_dron_list
    while
        find swappable dron
        if not swappable, break
    '''

# 5. 결과 print
for warehouse in warehouse_list:
    warehouse.get_info()
