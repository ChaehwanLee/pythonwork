# 표준입력
num1 = int(input("숫자1:")) # input 함수의 실행결과가 int 함수의 또 다른 매개변수로 사용됨. 함수의 실행결과로 값이 있는 경우 중첩해서 사용하는 것이 가능
num2 = int(input("숫자2:"))

# 표준출력
print("입력숫자1:", num1) #문자열과 변수 num1의 입력된 값을 콘솔(출력창)로 출력하기
print("입력숫자2:", num2)

print("==="*20)

# 기본출력
print(num1,num2)

# 구분자를 추가해서 출력
print(num1,num2, sep=',') # 구분자를 포함해서 출력

# 서식문자를 활용해서 출력
print("%d / %d = %d" % (100, 5, 20)) # %d 정수가 온다
print("%d / %d = %d" % (num1, num2, num1/num2))
print("%d / %d = %f" % (num1, num2, num1/num2))

# 한 줄에 여러 개의 값을 출력하기
# -> 여러 print문을 한 줄로 출력할 때 사용하고 각각 출력되는 문자열의 끝에 end에 정의하는 값을 추가한다.
# seperator 랑 비슷하지만 다름, sep 하나의 변수에 주는 것, end는 여러개
# end 에 할당하는 값이 여러 값
print("test1") # test+공백
print("test2")
print("")
print("test3")

print("test1", end="*****")
print("test2", end="*****")
print("test3")
