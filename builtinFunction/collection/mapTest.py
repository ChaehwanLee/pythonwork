# map (function, 자료구조)
# => 두 번째 매개변수로 정의한 자료구조안의 모든 데이터를 꺼내서 첫 번째 매개변수에 정의한 function을 적용해서 리턴
#
list1 = [10.123, 34.56, 55.18, 99.789]
print(list1)

# 위의 리스트에 저장된 데이터를 int로 변환해서 저장할 수 있도록 처리하세요 - DM
# for index, value in enumerate(list1):
#     list1[index] = int(value)
# print(list1)

# list1 = [int for i in list1]
# print(list1)

# map함수 이용
list2 = list(map(int, list1)) # 사용자 정의 함수(내가 만든 함수)
print(list2)

list3 = ["test", "python programming", "list","tuple"]
# list3의 각요소의 문자열의 길이를 출력
print(tuple(map(len, list3)))

# 매개 변수에 무엇을 집어넣느냐를 이해하면 된다