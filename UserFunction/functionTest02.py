# 사용자 정의 함수 만들기 # 변수는 값만 저장, 함수는 여러 명령들을 저장한 것
# 함수를 정의
# 1. 매개변수가 없고 리턴값이 없는 함수의 정의
def printInfo():
    print("*" * 30)
    print("작업시간 : 40")
    print("20hr을 보충하셔야 합니다.")
    print("*" * 30)
    print("")

# 2. 매개변수가 있고 리턴값이 없는 함수의 정의
def printInfo2(name):
    print("*" * 30)
    print(name,"의 작업시간 : 40")
    print("20hr을 보충하셔야 합니다.")
    print("*" * 30)
    print("")

# 3. 매개변수가 여러 개이고 리턴값이 없는 함수의 정의
#    매개변수가 여러 개인 경우 ,(콤마)로 구분한다.
def printInfo3(name,time):
    print("*" * 30)
    print(name,"의 작업시간 :",time)
    print("{}hr을 보충하셔야 합니다.".format(60-time))
    print("*" * 30)
    print("")

# 4. 매개변수가 있고 return 값이 있는 함수의 정의
def printInfo4(name,time):
    print("*" * 30)
    print(name,"의 작업시간 :",time)
    # print("{}hr을 보충하셔야 합니다.".format(60-time))
    print("*" * 30)
    print("")
    # 함수를 실행하고 보충시간을 리턴 - 함수를 호출한 곳으로 값을 넘겨주기
    # 리턴값은 변수, 값, 함수호출문, 연산 등이 올 수 있다.
    return 60-time

# 함수를 정의만하고 호출하지 않으면 실행되지 않는다.
# 함수호출
# 4. 매개 변수가 있고 리턴값이 있는 함수의 호출
printInfo4("장동건",25)
result = printInfo4("이민호", 42) # 호출결과를 함수에 넣어라
if result>20:
    print("정상")
else:
    print("보충")
print("=======================>", printInfo4("장기용",18))

# 1. 매개변수 없고 리턴값이 없는 함수의 호출
printInfo()
printInfo()
printInfo()

# 2. 매개변수가 있고 리턴값이 없는 함수의 호출
printInfo2("장동건")
printInfo2("이민호")
printInfo2("장기용")

# 3. 매개변수가 여러 개 있고 리턴값이 없는 함수의 호출
# 함수를 호출할 때 매개변수에 전달할 값들을 콤마로 구분해서 정의 순서대로 앞에서 부터 매개변수에 값이 전달된다.
printInfo3("장동건",27)
printInfo3("이민호",40)
printInfo3("장기용",38)
 #함수 -> 모듈 -> 패키지