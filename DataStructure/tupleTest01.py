# 튜플의 생성방법
tuple1 = (10, 20, 30)
print(tuple1)
print(type(tuple1))

list1 = [1,2,3,4]
print(tuple1)
print(list1, ":",type(list1))
print(tuple(list1), ":", type(tuple(list1)))

tuple2 = 40, 50, 60
print(tuple2)
print(type(tuple2))

#튜플의 저장될 요소가 한 개인 경우 아래와 같이 사용하면 int형 데이터로 인식, 튜플로 인식하도록 선언하려면 뒤에 ,(콤마)를 추가
tuple3 = (10) # 하나일 때는 , 를 찍어준다
print(tuple3)
print(type(tuple3))

tuple4 = (10,) # 하나일 때는 , 를 찍어준다
print(tuple4)
print(type(tuple4))

# 빈 튜플의 만드는 방법
tuple5 = ()
print(tuple5)
print(type(tuple5))

tuple6 = tuple()
print(tuple6)
print(type(tuple6))

# 튜플도 range 함수를 이용해서 만들 수 있다.
tuple7 = tuple(range(10))
print(tuple7)
print(type(tuple7))