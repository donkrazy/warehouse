class Warehouse():
    count = 0
    orders_todo = []

    def __init__(self, info):
        self.name = info['name']
        self.time_list = info['time_required']
        # 드론 대기열 리스트
        self.dron_time_list = [0] * info['num_drons']

    def get_additional_time(self, order):
        # 창고의 드론 중 가장 추가 배송시간이 짧은 것의 배송시간을 가져온다
        address_index = int(order['address'][0]) - 1
        return min(self.dron_time_list) + self.time_list[address_index]

    def work(self, order):
        # 창고의 배송목록에 추가
        self.orders_todo.append(order)
        self.count += 1

        # 창고의 드론 중 가장 추가배송시간이 짧은 것에 할일을 추가한다
        # 즉 쉬는 드론이 있으면 그 드론에 배송 할당, 쉬는 드론이 없으면 가장 대기시간이 짧은 드론에 할당
        min_index, min_value = min(enumerate(self.dron_time_list), key=lambda p: p[1])
        self.dron_time_list[min_index] += self.get_additional_time(order)

    def get_info(self):
        print('{}창고'.format(self.name))
        print('주문처리 건수 {}건'.format(self.count))
        print('예상 소요시간: {}분'.format(max(self.dron_time_list)))
        for order in self.orders_todo:
            print(order['address'])

    def __str__(self):
        return '{}, {}'.format(self.name, self.time_list)
