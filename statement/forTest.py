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
