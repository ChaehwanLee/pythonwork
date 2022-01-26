'''
출력할 단을 입력받아 입력된 구구단을 출력할 수 있도록 작성
출력형태
단:9
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
...
9 * 9 = 81
'''

# dan = int(input("알고 싶은 단을 입력하세요 : "))
#
# for dan1 in range(1, 10, 1):
#     gop = dan * dan1
#     print("%d * %d = %d " % (dan, dan1, gop))
#

dan = int(input("단:"))
for i in range(1, 10):
    print("%d * %d = %d" %(dan, i, dan* i))