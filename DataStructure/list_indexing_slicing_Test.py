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
print(list1[2:]) # 2부터 끝까지
print(list1[:]) # 처음부터 끝까지
print(list1[::2]) # 처음부터 끝까지 2 step 으로
print(list1[::-2]) # 뒤에서 부터 끝까지 2 step 으로

list3 = list("python programming")
print(list3)
# 슬라이싱을 적용해서 list3의 값을 뒤에서 부터 출력하세요

# for i in range(len(list3)):
#     print(list3[::-1])

for i in list3[::-1]:
    print(i, end="")
print("")