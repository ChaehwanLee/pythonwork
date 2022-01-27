#
# jumsu = int(input("점수를 입력하세요 : "))
#
# if jumsu >= 90:
#     print("수")
# elif jumsu >=80:
#     print("우")
# elif jumsu >=70:
#     print("미")
# elif jumsu >=60:
#     print("양")
# elif jumsu < 0 or jumsu > 100:
#     print("잘못입력")
# else:
#     print("가")

jumsu = int(input("점수를 입력하세요 : "))

if jumsu < 0 or jumsu > 100:
    print("잘못입력")
else:
    if jumsu>=90:
        print("수")
    elif jumsu>=80:
        print("우")
    elif jumsu>=70:
        print("미")
    elif jumsu>=60:
        print("양")
    else:
        print("가")