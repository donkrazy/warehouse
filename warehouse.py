class Warehouse():
    def __init__(self, info):
        self.count = 0
        self.orders_todo = []
        self.name = info['name']
        self.time_required = info['time_required']
        self.dron_schedule = [0] * info['num_drons']  # 드론 대기열 리스트

    def get_additional_time(self, order):
        # 창고의 드론 중 가장 추가 배송시간이 짧은 것의 배송시간을 가져온다
        address_key = order['address'][0]
        return min(self.dron_schedule) + self.time_required[address_key]

    def work(self, order):
        # 창고의 배송목록에 추가
        self.orders_todo.append(order)
        self.count += 1

        # 창고의 드론 중 가장 추가배송시간이 짧은 것에 할일을 추가한다
        # 즉 쉬는 드론이 있으면 그 드론에 배송 할당, 쉬는 드론이 없으면 가장 대기시간이 짧은 드론에 할당
        min_index, min_value = min(enumerate(self.dron_schedule), key=lambda p: p[1])
        address_key = order['address'][0]
        self.dron_schedule[min_index] += self.time_required[address_key]

        # [TEST] print marginal choice
        # print('{}, {}에 할당, schedule:{}{}'.format(order['address'], self.name, self.name, self.dron_schedule))

    def get_info(self):
        print()
        print('##### 창고 {} #####'.format(self.name))
        print('주문처리 건수 {}건'.format(self.count))
        print('예상 소요시간: {}분'.format(max(self.dron_schedule)))
        print('dron schedule:{}'.format(self.dron_schedule))
        print('처리대상')
        for order in self.orders_todo:
            print(order)

    def __str__(self):
        return '{}, {}'.format(self.name, self.time_required)
