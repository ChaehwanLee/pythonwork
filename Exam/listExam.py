# 88, 99, 77, 100, 99의 점수를 저장할 수 있는 리스트를 작성한 후 점수의 총합과 평균을 계산해서 출력하세요
# [출력형태]
# 점수총합 : ____
# 평균 : ____

# jumsuList = [88, 99, 77, 100, 99]
# result = 0
#
# print(jumsuList)
#
# for val in jumsuList:
#     result = jumsuList[0] + jumsuList[1] + jumsuList[2] + jumsuList[3] + jumsuList[4]
#
#     print("점수총합: ", result)
#     print("점수평균 : ", result / 5)
#

# jumsu_list = [88, 99, 77, 100, 99, 100]
# hap = 0
# # 리스트의 길이(요소의 갯수) - len함수
# print(len(jumsu_list))
# print(len('test'))
# for i in jumsu_list:
#     hap = hap + i
#
# print("점수총합:{}".format(hap))
# print("평균:{}".format(hap/len(jumsu_list)))

# 2. 'python programming' 문자열을 리스트로 변환한 후
# python programming 으로 출력
# gnimmargorp nohtyp의 형태로 출력 (mail)

p_list = list('python programming')
print(p_list)
print(len(p_list))

for str in p_list:
    print(str, end="")

print("-"*20)

for str in p_list:
    str = p_list
    print(str, end="")

