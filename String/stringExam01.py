# 1. 문자열을 입력 받아 거꾸로 출력될 수 있도록 작성하기
#   입력데이터 : python
#   출력데이터 : nohtyp

inputstr = input("문자열입력: ")
print(inputstr)
# print(inputstr[0])
# inputstr[0] = "t" 문자열은 변경할 수 없다
for i in range(len(inputstr)-1,-1,-1):
    print(inputstr[i],end="")
print("")
print("="*50)

outputstr=""
size = len(inputstr)
for i in range(size):
    outputstr = outputstr + inputstr[size-(i+1)]
print(outputstr)

# for index, value in enumerate(inputstr):
#     print(inputstr[index],end="")


# 2. 입력받은 문자열 중 소문자 a 가 있으면 대문자 A로 변경해서 출력하기
#   입력데이터 : python programming
#   출력데이터 : python progrAmming

# inputstr = input("문자열 입력:")
# print(inputstr)
# for i in inputstr:
#     print("{}".format(i),end="")
#     if i =="a":
#         print("A",end="")



# 3. 입력받은 문자열 대신 오른쪽으로 3칸 뒤에 있는 문자의 조합으로 출력하기
#   입력데이터 : abc
#   출력데이터 : def
# ===> 모두 for 문을 이용해서 작업하세요(이메일)

# str1 = print(str(input("문자를 입력하세요: ")))
# for i in len(str1):
#     print(key, ":",str1[key])
#
# str2 = print(str(input("문자를 입력하세요: ")))
# for i in len(str2):
#     print(chr(ord(str2)))
#
# str3 = print(str(input("문자를 입력하세요: ")))
# for i in len(str3):
#     print(chr(ord(str3)+3))

