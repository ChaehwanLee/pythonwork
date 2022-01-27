# for i in range(1,6):
#     print("파이썬 프로그래밍")
#
# print("*"*20)
# for i in range(5, 0, -1):
#     print("파이썬 프로그래밍")

# 1 부터 100까지의 합에서 3의 배수의 합 구하기 - for문 (DM)

# saebae = 0
# for i in range(1, 101, 3):
#     if i % 3 == 0:
#         saebae += i
# print("3의 배수의 합 : %d" % saebae)


hap = 0
num = 0
for i in range(0, 11, 3):
    # hap = hap + i
    # 대입연산자 +=, -=, *=, /= ...
    print(i)
    hap += i
    num = num + i ** 2
print("합:{}".format(hap))
print(num)
