#
# a = int(input("숫자를 입력하세요 :"))
#
# if a == 0:
#     print("제로")
# elif a >= 0:
#     print("양수")
# else:
#     print("음수")

num = int(input("숫자1: "))
result = ""
if num > 0:
    result = "양수"
elif num < 0:
    result = "음수"
else:
    result = "제로"

print("입력한 숫자는 %d 이며 %s 입니다." %(num, result))
