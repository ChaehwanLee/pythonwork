# 두 사람이 주사위를 던져서 큰수가 나오면 이기도록 프로그램을 작성하세요
# - 랜덤수를 입력 받아서 작업하기(두 개)
# [출력형태]
# A의 주사위 숫자:___
# B의 주사위 숫자:___
# 결과:(A가 이겼습니다. or B가 이겼습니다. or A와 B가 비겼습니다.

# *** 내장함수, 표현하기 위해 만들어진 기능들 print, int, input

# if ~ elif ~ else를 이용해서 작업하기
# 채팅창에 제출 - DM으로 제출하기

# import random
#
# a = random.randrange(1, 7)
# b = random.randrange(1, 7)
# print("A의 주사위 숫자 : ", a)
# print("B의 주사위 숫자 : ", b)
#
# if a>b:
#     print("A가 이겼습니다")
# elif a == b:
#     print("A와 B가 비겼습니다")
# else:
#     print("B가 이겼습니다")
#

import random

myrandomNum_A = random.randrange(1, 7)
myrandomNum_B = random.randrange(1, 7)
print("A의 주사위 숫자: {}".format(myrandomNum_A))
print("B의 주사위 숫자: %d" % myrandomNum_B)

if myrandomNum_A > myrandomNum_B :
    print("A가 이겼습니다.")
elif myrandomNum_A < myrandomNum_B :
    print("A가 이겼습니다.")
else:
    print("A와 B가 비겼습니다.")