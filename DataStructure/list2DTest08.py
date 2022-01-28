# 이차원리스트의 생성과 사용방법
# 중첩된 것과 동일한 개념이므로 이중 for문을 이용해서 작업
# list1 = [
#             [1,2],
#             [3,4,5],
#             [6,7,8,9]
#         ]
#
# print(list1[0])
# print(list1[2][3])
#
# for row in list1:
#     for i in row:
#         print(i, end=" ")
#     print("")
#
# print("="*30)

'''
a b c d e
f g h i j
k l m n o
p q r s t 
u v w x y
'''

al_list = list("abcdefghijklmnopqrstuvwxy")
print(al_list)

for i in al_list[0:5]:
    for j in al_list:
        if j == i:
            print("*", end=" ")
        else:
            print("")
