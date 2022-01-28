# list_indexing_slicing_test.py
# 리스트의 인덱싱
list1 = list(range(10,101,10))
print(list)

print(list1[1])
print(list1[5])
print(list1[9])
print(list1[-1])
print(list1[-5])

# 리스트의 슬라이싱 # 범위는 n-1
print(list1[4:10:1]) # 4번 ~ 10-1번 index를 가진 요소를 추출 - step 1을 적용
print(list1[4:10:2]) # 4번 ~ 10-1번 index를 가진 요소를 추출 - step 2을 적용
print(list1[4:10])
print(list1[:2]) # 0, 1 index의 요소가 리턴
print(list1[2:])