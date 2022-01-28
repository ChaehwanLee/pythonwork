# mail

list1 = [
        ['A','B','C','D','E'],
        ['F','G','H','I','J'],
        ['K','L','M','N','O'],
        ['P','Q','R','S','T'],
        ['U','V','W','X','Y']
        ]

print("원본배열")
print("="*22)

#이차원리스트 원본 출력하기
for row in list1:
    for i in row:
        print(i, end=" ")
    print("")

#이차원리스트 요소를 변경

for idx in range(len(list1)):
    list1[idx][idx] = "*"
print(list1)

# 원본이 변경된 이차원리스트 출력하기
print("수정된리스트")
print("="*22)
for row in list1:
    for i in row:
        print(i, end="   ")
    print("")

print("수정된 리스트")
print("="*22)
#이차원리스트 원본 출력하기
for row in range(len(list1)):
    for i in range(len(list1[row])):
        if row == i:
            print("*", end="  ")
        else:
            print(list1[row][i], end="  ")
    print("")