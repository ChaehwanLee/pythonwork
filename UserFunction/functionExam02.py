# functinoExam01.py 파일에서 정의한 printgugu()와 printSum()을 copy해서 작업하기
# - printgugu는 매개변수로 단을 입력받을 수 있도록 처리하고 호출해서 결과가 출력될 수 있도록 수정
# - printSum은 1 부터 매개변수로 입력된 숫자까지의 합을 출력할 수 있도록 수정

# def printgugu(dan):
#     for i in range(1,10):
#         print(str(dan),"* {} = {}".format(i,dan*i))
#
# def printSum(hap):
#     sum = 0
#     for i in range(1,int(hap)):
#         sum = sum + i
#     print("1 부터 100까지의 합 => {}".format(sum + hap))

def printgugu(dan):
    for i in range(1,10):
        print(str(dan),"* {} = {}".format(i,dan*i))

def printSum(num):
    sum = 0
    for i in range(1,num+1):
        sum = sum + i
    print("1 부터 {}까지의 합 => {}".format(num,sum))

# 함수호출 - dm
dan = int(input("출력 단을 입력: "))
printgugu(dan)

printSum(10)
printSum(100)
printSum(1000)