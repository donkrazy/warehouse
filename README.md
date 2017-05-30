# 풀이 idea
##1. 주문을 순서대로 처리
매 주문이 들어올때 마다 추가(marginal) 배송시간을 최소화 하는 결정
단 주문 순서에 따라 총 배송시간이 달라짐
##2. 주문을 한꺼번에 100개 처리
utils.allocate_order()
실제로는 한꺼번에 100개씩 묶어서 창고 별 배송의 효율적인 할당 후을 먼저 한다
주문 순서에 무관하게 최적 결정


# 소스코드 실행 
python3 main.py

# 예제 input 생성
python3 make_input.py