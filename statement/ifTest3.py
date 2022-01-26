# 들여쓰기로 블럭을 표현할 수 있다.
num = 75

#if의 블럭에 해당하는 명령문은 print("만족1")
if num > 50 :
    print("만족1")
    if num%2==1 :
        print("홀수")
    else :
        print("짝수")
        print("마무리")
else:
    print("불만족1")