# 집합과 리스트의 차이점
# => 리스트는 중복이 가능하지만 집합은 중복이 불가능

set1 = {"java", "python", "C++", "kotlin", "kotlin"}
list1 = ["java", "python", "C++", "kotlin", "kotlin"]
print(list1)
print(set1)  # 집합의 특성 중복되는 데이터는 들어가지 않음, 집합은 순서가 없다

# 빈집합 생성
#set2 = {} {} 로 정의하면 딕셔너리로 인식
set2 = set()
print(type(set2))

# set의 데이터 수정
set2.add("javascript") # set에 데이터 추가
set2.add("html")
set2.add("css")
print(set2)

set1.remove("kotlin") #set의 데이터 삭제하기
print(set1)

set1.update(set2) #합집합의 기능
print(set1)




