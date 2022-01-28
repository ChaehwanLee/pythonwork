# 리스트를 만들고 엑세스하는 방법
list1 = list(range(1, 20, 2)) # start, end-1, step
print(list1)

# 리스트에서 사용할 수 있는 기능
# reversed 함수를 이용해서 range로 생성한 리스트를 reverse 시킬 수 있다.
list2 = list(reversed(range(1, 20, 2)))
print(list2)

# 2. 문자열을 이용해서 리스트를 만들기
list3 = list("python programming")
print(list3)

# 리스트를 접근하는 일반적인 방법
for i in list3:
    print(i, end="")
print("="*20)

print(len(list3))
# 리스트를 range 로 접근하는 방법
for i in range(len(list3)): #range(18) / range(0, len(list3), 1):
    print("{}:{}".format(i,list3[i]),end=" ")
print("")
print("="*30)