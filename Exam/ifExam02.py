'''
ifExam02.py
1. 숫자를 입력받아 양수, 음수 , 0을 출력할 수 있도록 작성 %d를 활용하기

a = int(input("숫자를 입력하세요 :"))

if a == 0:
    print("제로")
elif a >= 0:
    print("양수")
else:
    print("음수")
'''


num = int(input("숫자1: "))
# result = "" # 변수의 초기화
if num > 0:
    result = "양수"
elif num < 0:
    result = "음수"
else:
    result = "제로"

print("입력한 숫자는 %d 이며 %s 입니다." %(num, result))

# 중복되는 코드는 최대한 작게