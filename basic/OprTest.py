# 산술연산자
print(2+3)
print(2-3)
print(2*3) #곱하기
print(2**3) #제곱
print(11/2) #나누기(소숫점 이하도 출력)
print(11%2) #나머지구하기
print(11//2) #나누기(소숫점 이하 버리기)

#비교연산자(True나 False를 결과로 Return)
print(5>3)
print(5<3)
print(5==3) #같다
print(5>=3)
print(5<=3)
print(5!=3) #같지 않다=다르다

#논리연산자
num1 = 100
num2 = 50

#And 연산 모든 조건이 True면 True를 Return
if num1 >= 90 and num2 >= 90:
    print("통과")
else:
    print("다시작업")

#Or 연산 모든 조건 중 한 개 이상 True면 True를 Return
if num1 >= 90 or num2 >= 90:
    print("통과")
else:
    print("다시작업")
