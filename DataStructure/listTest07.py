# 리스트를 제어할 수 있는 함수 사용하기
list1 = list(range(0, 51, 5))
list1.append(20)
print(list1)
print(list1.count(20)) # 20 이라는 값이 몇 번 나오는지 횟수를 리턴

print(list1.index(20)) # 45가 위치한 요소의 index

myelement = list1.pop()
print(myelement)
print(list1)

list1.insert(2, 77) # 2번 index의 위치에 요소가 새롭게 추가
print(list1)

list1.append(20)
list1.remove(20) # 중복된 값이 있는 경우 모두 처음 만나는 요소만 제거
print(list1)

# 정렬 -> sort는 원본 리스트를 변경하므로 리턴값이 없다.
#        sorted는 새롭게 sort된 리스트를 만들어서 리턴.

print("="*30)
print(list1.sort())
print(sorted(list1))
list1.sort() # 기본은 오름차순 정렬 = 작은값(ㄱ, 1, A) ~~~~~ 큰 값(ㅎ,10,z)
print(list1)

list1.sort(reverse=True) # reverse 매개변수를 True 정의하면 내림차순 정렬이 적용
print(list1)
print(sorted(list1,reverse=True))

##########

