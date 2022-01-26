'''
1 부터 100까지의 숫자의 총합, 홀수합, 짝수합을 출력하기
총합 : _
홀수합 : _
짝수합 : _
'''

# hap = list(range(1, 101, 1))
# print(hap)
#
# total = 0
#
# for total in range(1, 101, 1)
#     sum(total)
# print("총합 : " % total)
#
# print("홀수합 : " % hol)
# print("짝수합 : " % jjak)

# 0은 정수형 변수에서 주로 초기화할 때 할당하는 값, "" 문자열형 변수를 초기화할 때 할당하는 값
totalVal = 0 # 총합이 저장되는 변수
oddVal = 0 # 홀수의 합이 저장되는 변수
evenVal = 0 # 짝수의 합이 저장되는 변수

# 변수를 명령문 한 줄로 초기화하는 방법(한 번에 묶기) - 처음하는 사람은 축약보다는 한 줄 한 줄 풀어서 쓰는 것을 추천함
num1, num2 = 0, 0
for i in range(1, 101, 1):
    totalVal = totalVal + i
    if i % 2 == 0:
        evenVal = evenVal + i
    else:
        oddVal = oddVal + i
print("총합 : %d"% totalVal)
print("홀수합 : %d" % oddVal)
print("짝수합 : %d" % evenVal)

