# 문장을 5번 출력하기
i = 1
while i <= 5:
    print("%d : 지금은 python 기본을 학습하는 중" % i)
    i = i + 1

print("==="*20)
# Python의 while문은 else문과 함께 사용할 수 있다.
num = 1
while num<=9:
    print("test: %d" % num)
    num = num + 1
else: # while문의 조건이 만족하지 않는 경우
    print("종료")
print("루프종료")