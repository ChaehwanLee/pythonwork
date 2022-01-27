# num1 = int(input("숫자1:"))
# num2 = int(input("숫자2:"))
# print("num1:{} , num2:{}".format(num1, num2))
# print("{} + {} = {}".format(num1, num2, (num1/num2)))

print("{},{},{}".format(123, 456, 789)) # 아무것도 지정해주지 않으면 앞에서 부터 0, 1, 2
print("{0},{2},{1}".format(123, 456, 789)) # 연속된 데이터들에 순서를 줄 수 있다 / 인덱싱
print("{0:5d}, {2:5.1f},{1:15d}".format(123,456, 789.12345))
# 공간을 주고나서 채움
# 값을 지정해주지 않으면 시작은 0