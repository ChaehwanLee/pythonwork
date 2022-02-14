# 3. 입력받은 문자열 대신 오른쪽으로 3칸 뒤에 있는 문자의 조합으로 출력하기
#   입력데이터 : abc
#   출력데이터 : def
# ===> 모두 for 문을 이용해서 작업하세요(이메일)

# inputstr = input("입력데이터:")
# print("출력데이터:", end="")
# for i in inputstr:
#     # x,y,z => a,b,c
#     print(chr(ord(i)+3), end="")

# 다른 방법
print(ord('z')-23)
inputstr = input("입력데이터:")
print("출력데이터:", end="")
for i in inputstr:
    # x,y,z => a,b,c
    print(chr(ord(i)+3), end="")