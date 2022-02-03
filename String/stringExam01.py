# 1. 문자열을 입력 받아 거꾸로 출력될 수 있도록 작성하기
#   입력데이터 : python
#   출력데이터 : nohtyp
# 2. 입력받은 문자열 중 소문자 a 가 있으면 대문자 A로 변경해서 출력하기
#   입력데이터 : python programming
#   출력데이터 : python progrAmming
# 3. 입력받은 문자열 대신 오른쪽으로 3칸 뒤에 있는 문자의 조합으로 출력하기
#   입력데이터 : abc
#   출력데이터 : def
# ===> 모두 for 문을 이용해서 작업하세요(이메일)

str1 = print(str(input("문자를 입력하세요: ")))
for i in str1:
    print(len(str1[-1:]))