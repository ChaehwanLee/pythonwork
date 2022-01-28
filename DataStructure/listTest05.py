# 리스트의 연산과 리스트의 값 변경하기
list1 = list(range(0, 101, 10))
print(list1)

list1[2] = 70 # 2번 index의 요소 (세 번째 요소) 값을 70으로 변경
print(list1)

# 2, 3번 요소의 값을 200과 300으로 변경
list1[2:4] = [200, 300]
print(list1)

# list1의 마지막 요소의 값을 리스트로 변경
list1[len(list1)-1] = [1000,2000]
print(list1)

print(list1[1])
print(list1[1][1])
# print(list1[len(list1)-1][1])

# 리스트의 요소를 삭제하기
del(list1[0])
print(list1)

# 리스트의 요소를 삭제 할때도 슬라이싱을 활용
del(list1[2:4])
print(list1)

list1[2:4] = [] # del(list1[2:4])와 동일한 결과
print(list1)

del(list1) #리스트를 삭제
print(list1)