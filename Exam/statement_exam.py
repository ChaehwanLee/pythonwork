'''
- 랜덤수를 생성해서 사용자가 입력한 수와 일치하는지 확인하고 결과를 출력
[출력결과]
숫자를 입력하세요 : ____
    1) 정답인 경우 : 와 정답입니다.!!!
    2) 사용자가 입력한 숫자가 랜덤수보다 큰 경우 : 생각하신 숫자가 컴퓨터가 발생시킨 숫자보다 큽니다. 다시 입력하세요
    3) 사용자가 입력한 숫자가 랜덤수보다 작은 경우 : 생각하신 숫자가 컴퓨터가 발생시킨 숫자보다 작습니다. 다시 입력하세요

    랜덤값 :___, 사용자가 입력한 숫자 : ___, 실행횟수 : ____ # 마지막에 한 번만 출력
'''
# import random
#
# ann = int(input("숫자를 입력하세요 : "))
# pc = random.randint(1, 100)
#
# while True:
#     for ann in range(1, 100):
#         if ann > pc :
#             print("생각하신 숫자가 컴퓨터가 발생시킨 숫자보다 큽니다. 다시 입력하세요")
#             break
#     else:
#         ann = int(input("숫자를 입력하세요 : "))
#     while True:
#             if ann <= pc :
#                 print("생각하신 숫자가 컴퓨터가 발생시킨 숫자보다 작습니다. 다시 입력하세요")
#             continue
#
#     print("와 정답입니다.!!!")
#
# print("랜덤값 :", pc)
# print("사용자가 입력한 숫자 : ", ann)
# print("실행횟수 :", )

import random

randomNum = random.randint(1, 100)
count = 0 #실행횟수
while True:
    count = count + 1
    userNum = int(input("숫자를 입력하세요 : "))
    if userNum == randomNum:
        print("와 정답입니다.!!!")
        break
    elif userNum > randomNum:
        print("생각하신 숫자가 컴퓨터가 발생시킨 숫자보다 큽니다. 다시 입력하세요")
    else:
        print("생각하신 숫자가 컴퓨터가 발생시킨 숫자보다 작습니다. 다시 입력하세요")

print("랜덤수:{}, 사용자가 입력한 숫자:{}, 실행횟수:{}".format(randomNum, userNum, count))