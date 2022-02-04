# 함수가 왜 필요할까? 함수를 사용하는 이유
# 아래의 코드처럼 동일한 코드가 중복되는 경우 함수를 정의해서 사용하면 편하다.

print("*"*30)
print("작업시간 : 40")
print("20hr을 보충하셔야 합니다.")
print("*"*30)
print("")

print("*"*30)
print("작업시간 : 40")
print("20hr을 보충하셔야 합니다.")
print("*"*30)
print("")

print("*"*30)
print("작업시간 : 40")
print("20hr을 보충하셔야 합니다.")
print("*"*30)
print("")

# 사용자 정의 함수 만들기 # 변수는 값만 저장, 함수는 여러 명령들을 저장한 것
def printInfo():
    print("*" * 30)
    print("작업시간 : 40")
    print("20hr을 보충하셔야 합니다.")
    print("*" * 30)
    print("")