# break는 선언된 반복문 블럭이 종료된다

for dan in range(2, 10):
    for i in range(1, 10):
        if dan == 5:
            break
        for i in range(1, 10):
            print("%d * %d = %d\t" % (dan, i, dan * i), end="")

        print("")

print("="*30)

# continue
for dan in range(2, 10):
    for i in range(1, 10):
        if dan == 5:
            continue
        for i in range(1, 10):
            print("%d * %d = %d\t" % (dan, i, dan * i), end="")

        print("")

print("="*30)