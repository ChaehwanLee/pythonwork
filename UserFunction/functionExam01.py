# 3단을 출력하는 함수를 정의하고 호출해서 사용하세요
# 3*1 = 3
# ...
# 3*9 = 27
# 함수명 : printgugu, 매개변수 X, 리턴값 X

# def printgugu():
#     print('''
#             3*1 = 3
#             3*2 = 6
#             3*3 = 9
#             3*4 = 12
#             3*5 = 15
#             3*6 = 18
#             3*7 = 21
#             3*8 = 24
#             3*9 = 27
#         ''')

# 함수정의
def printgugu():
    # 3단을 출력하는 로직
    for i in range(1,10):
        print("3 * {} = {}".format(i,3*i))
# 1부터 100까지 더한 값을 출력할 수 있도록 함수를 정의하고 호출
# [출력]
# 1부터 100까지의 합 => 5050
# 함수명: printsum, 매개변수 x, 리턴값 x - dm
def printSum():
    sum = 0
    for i in range(1, 101):
        sum = sum + i
    print("1 부터 100까지의 합 =>", sum)

# 함수호출
printgugu()
print("")
printSum()