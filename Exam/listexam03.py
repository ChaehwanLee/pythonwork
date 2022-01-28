'''
1. 리스트에 요소의 갯수를 입력받고 각 요소에 저장될 값들을 입력
    리스트의 요소를 몇 개 만들까요? ______5받아 리스트를 작성하세요
    리스트에 추가될 값을 입력하세요 : ______
    리스트에 추가될 값을 입력하세요 : ______
    리스트에 추가될 값을 입력하세요 : ______
    리스트에 추가될 값을 입력하세요 : ______
    리스트에 추가될 값을 입력하세요 : ______
    ...

2. 1번에서 작성된 리스트의 요소를 0번부터 출력, n-1 번부터 출력
    range를 활용해서 작업하기
    10, 20, 30, 40, 50
    50, 40, 30, 20, 10

3. 모든 요소의 합과 평균을 출력하기
   요소의 합:
   요소의 평균:
'''

#
# mlist = []
# mlist = print(int(input("리스트의 요소를 몇 개 만들까요?:")))
# print(mlist)
# mlist.append(mlist)
# print(mlist)
# print(len(mlist))

# 1
list1 = []
count = int(input("리스트의 요소를 몇 개 만들까요?"))
# list에 요소를 추가하기 위한 for
for i in range(count): # 0 ~ count-1
    list1.append(int(input("리스트에 추가될 값을 입력하세요: ")))

for i in list1:
    print(i)

# 2
# list에 요소를 추가하기 위한 for
for i in range(0, len(list1),1): # range(18)
    print("{}".format(list1[i]), end=" ")
print("")
print("="*30)

for i in range(len(list1)-1,-1,-1):
    print("{}".format(list1[i],end=" "))
print("")
print("="*30)

# 3
hap = 0
for i in list1:
    hap = hap + i

print("요소의 합:{}".format(hap))
print("요소의 평균:{}".format(hap/count,end=""))
