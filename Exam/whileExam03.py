# 랜덤수를 이용해서 주사위를 굴리고 3이 나오면 프로그램을 종료할 수 있도록 적성
#       =>while문을 이용해서 3이 나오기 전까지 주사위를 계속 굴릴 수 있도록 작성하자

import random
randomNum = 0 #랜덤수를 저장하기 위한 변수
count = 0 #실행횟수를 저장하기 위한 변
while randomNum != 3:
    count = count + 1
    randomNum = random.randint(1, 6) # 지정값 사이의 랜덤 수 발생 - 1과 6사이의 값
    print(randomNum)

print("="*20)
print("실행횟수:{}".format(count))
print("end")
