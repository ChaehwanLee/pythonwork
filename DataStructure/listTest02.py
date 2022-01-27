# 요소가 저장되어 있지 않은 빈 리스트를 만들기
mylist1 = []
mylist2 = list()
print(mylist1)
print(mylist2)
print(len(mylist1))
print(len(mylist2))

# range를 이용해서 리스트를 작성
mylist3 = list(range(100))
print(mylist3)

mylist3 = list(range(0, 10))
print(mylist3)

mylist3 = list(range(10, 0, -1))
print(mylist3)

# 문자열을 리스트로 변환하기
strlist = list('python')
print(strlist)

# 리스트의 index
# 앞에서부터 엑세스 : 0 1 2 3 4 5
# 뒤에서부터 엑세스 : -6 -5 -4 -3 -2 -1
print(strlist[5])
print(strlist[-5])
