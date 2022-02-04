# 2. 입력받은 문자열 중 소문자 a 가 있으면 대문자 A로 변경해서 출력하기
#   입력데이터 : python programming
#   출력데이터 : python progrAmming

inputstr = input("문자열 입력:")
print("출력데이터:", end="")
for i in inputstr:
    if i =="a":
        print("A",end="")
    else:
        print("{}".format(i), end="")