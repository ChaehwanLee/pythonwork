
# studentlist = ['장동건','김범룡','장기용','이민호','RM','정국','지민','홉']
# print(studentlist)
#
# studentlist.append(['슈가','진','뷔'])
# print(studentlist)
#
# studentlist.insert(7,'제이홉')
# print(studentlist)
#
# print(studentlist[:])
# print(studentlist[::-1])
#
# studentlist.reverse()
# print(studentlist[::3])
#
# studentlist.append(['정우성','장기용'])
# print(studentlist)
#
# studentlist.insert(8,[100,90,80])
# studentlist.insert(7,[88,77])
# print(studentlist)
#
# print(studentlist)
# studentlist.insert(0,100)
# print(studentlist)
#
# studentlist.index[::0]

# 1.
studentlist = ['장동건','김범룡','장기용','이민호','RM','정국','지민','홉']
print(studentlist)

# 2.
studentlist.append("슈가")
studentlist.append("진")
studentlist.append("뷔")
# studentlist + ["슈가","진","뷔"]
print(studentlist)

# 3.
print(studentlist)

# 4.
# studentlist[7] = "제이홉"
studentlist[studentlist.index("홉")] = "제이홉"
print(studentlist)

# 5.
for i in studentlist:
    print(i, end="  ")
print("")

for i in studentlist[::-1]:
    print(i, end="  ")
print("")

#

studentlist.sort(reverse=True)
print(studentlist)

# 5번 부터 모든 요소를 출력 - 슬라이싱
# 3번부터 모든 요소를 출력 - 슬라이싱
for i in studentlist[3:]:
    print(i, end="")
print("")

# 정우성을 장기용 오른쪽에 추가하세요
studentlist.insert(studentlist.index("장기용")+1, "정우성")
print(studentlist)

'''
슈가와 제이홉의 점수를 추가하세요 (슈가와 제이홉이 저장된 요소에 수정되어 추가되는 것이므로 슈가값과 제이홉의 값은 지워집니다.)
슈가 : [100, 90, 80]
제이홉 : [88, 77]
'''

studentlist[studentlist.index("슈가")] = [100,90,80]
studentlist[studentlist.index("제이홉")] = [88, 77]
print(studentlist)

# 슈가의 2번 요소의 점수를 100으로 변경

studentlist[8][2] = 100
print(studentlist)

# 슈가의 모든 점수를 슬라이싱해서 출력
print(studentlist[8:9])
for i in studentlist[8:9]:
    print(i)

print(studentlist[8][0:2])
print(studentlist[8][:])

# for 구문을 두 개 사용 2차원 리스트


