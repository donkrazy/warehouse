import json
from utils import allocate_order, search
from Warehouse import Warehouse


# 1. Get input data
f = open('input.json')
input_dict = json.loads(f.read())

# 2. Allocate order efficiently
# allocate_order(input_dict)


# 3. 창고 정보로 창고 생성
warehouse_info_list = [
    {'name': 'A', 'time_required': [10, 25, 30, 50, 60], 'num_drons': 20},
    {'name': 'B', 'time_required': [20, 10, 20, 40, 55], 'num_drons': 25},
    {'name': 'C', 'time_required': [60, 40, 25, 15, 20], 'num_drons': 15},
]
warehouse_list = []
for warehouse_info in warehouse_info_list:
    warehouse = Warehouse(warehouse_info)
    warehouse_list.append(warehouse)
    print('CREATED: ', warehouse)


# 4. 각 창고에 최적의 주문 할당
for order in input_dict['orders']:
    # 세 창고 중 추가 배송시간(marginal)이 적게 걸리는 최적의 창고 검색
    warehouse = search(warehouse_list, order)
    # 창고에 주문 할당
    warehouse.work(order)

# 5. 결과 print
for warehouse in warehouse_list:
    warehouse.get_info()
