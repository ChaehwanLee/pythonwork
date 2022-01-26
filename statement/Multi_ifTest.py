ssn = int(input("주민번호:"))
if ssn == 1:
    print("남자")
else:
    print("여자")

# if elif를 이용해서 다중 평가 - 중첩도 가능
if ssn == 1:
    print("남자")
elif ssn == 2:
    print("여자")
elif ssn == 3:
    print("남자")
elif ssn == 4:
    print("여자")
else:
    print("기타")

# 논리연산자를 이용해서 작업

if ssn == 1 or ssn == 3:
    print("남자")
elif ssn == 2 or ssn == 4:
    print("여자")
else:
    print("기타")