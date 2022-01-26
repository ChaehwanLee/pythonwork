# range를 이용해서 for 문을 처리

mydata = list(range(1,50,2))
print(mydata)

for i in range(1, 5, 1):
    print("%d : 지금은 python 기본을 학습하는 중" % i)

print("---"*20)
for i in range(1,3): #시작값, 종료값 -1
    print("%d : 지금은 python 기본을 학습하는 중" % i)

print("---"*20)
for i in range(10):
    print("%d : 지금은 python 기본을 학습하는 중" % i)

# 1부터 10까지의 합을 출력하기
mynum = 0
hap = 0
for mynum in range(1, 11, 1):
    hap = hap+mynum # 누적을 하려면 변수에 넣어줘야 한다.
print("1부터 10까지의 합은: %d" % hap)

