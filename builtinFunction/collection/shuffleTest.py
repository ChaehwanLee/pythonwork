# random라이브러리에서 제공되는 함수
# 여러 데이터를 집계 정리하는 개념, hadoop etc -> 파이썬을 잘 해놓으면 bigdata에도 가능
import random

list1 = [10, 20, 30, 40, 50]
print(list1)

print(random.shuffle(list1)) #none, 결과를 출력할게 없다 (로직을 이용하는 것도 있으나 shuffle을 사용함)
print(list1)
