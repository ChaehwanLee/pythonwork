# 1. 88, 99, 100 점을 튜플로 정의하고 합계와 평균을 구해 출력하기 - DM

# tuple1 = (88, 99, 100)
# hap = 0
#
# for i in tuple1:
#     hap = hap + i
# print("합계 : ", hap)
# print("평균 : ", hap/len(tuple1))

jumsu_list = (88,99,100)
hap = 0
for i in jumsu_list:
    hap = hap + i

print("점수총합:{}".format(hap))
print("평균:{}".format(hap/len(jumsu_list)))