# 표준입력
num1 = int(input("숫자1:")) # input 함수의 실행결과가 int 함수의 또 다른 매개변수로 사용됨. 함수의 실행결과로 값이 있는 경우 중첩해서 사용하는 것이 가능
num2 = int(input("숫자2:"))


# 표준출력
print("입력숫자1:", num1) #문자열과 변수 num1의 입력된 값을 콘솔(출력창)로 출력하기
print("입력숫자2:", num2)

print(num1,num2)
print(num1,num2, sep=',')

print("%d / %d = %d" % (100, 5, 20)) # %d 정수가 온다
print("%d / %d = %d" % (num1, num2, num1/num2))
print("%d / %d = %f" % (num1, num2, num1/num2))