
'''
1.

2 * 1 = 2
...

2* 9 = 18

2.

2 * 1 = 2 2 * 2 = 4
...

9 * 1 = 9 9 * 2 = 18
'''

# gu = 0
# for i in range(1, 10):
#     for row in range(1, 10):
#         print("%d * %d = %d" % (i, row, i * row))
#

# 2단부터 9단까지 출력하기

# for dan in range(2, 10):
#     for i in range(1, 10):
#         print("%d * %d = %d" % (dan, i dan * i))
#     print("")

print("=" * 30)

for dan in range(2, 10):
    for i in range(1, 10):
        print("%d * %d = %d\t" % (dan, i, dan * i ), end="  ") #\t는 특수문자 \T 는 탭버을 누른것과 동일한 효과

    print(" ")

print("=" * 30)

for i in range(1, 10):
    for dan in range(2, 10):
        print("%d * %d = %d\t" % (dan, i, dan * i ), end="  ") #\t는 특수문자 \T 는 탭버을 누른것과 동일한 효과
    print(" ")