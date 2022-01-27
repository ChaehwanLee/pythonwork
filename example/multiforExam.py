'''
1.
2  2  2  2  2
2  2  2  2  2
2  2  너  2  2
2  2  2  2  2
2  2  2  2  2
'''

for row in range(1, 6):
    for i in range(1, 6):
        if row == 3 and i ==3 :
           print("너", end="  ")
        else:
           print("2", end="  ")
    print("")

print("="*30)

'''
2.
*  2  2  2  2
2  *  2  2  2
2  2  *  2  2
2  2  2  *  2
2  2  2  2  *
'''

for row in range(1, 6):
    for i in range(1, 6):
        if row == i :
           print("*", end="  ")
        else:
           print("2", end="  ")
    print("")

print("="*30)

'''
3
숫자로 정사각형 출력하기
1   2   3   4   5
...

12  22  23  24  25
'''
mynum = 1 #외부에서 변수가 필요하면 얼마든지 선언하고 사용할 수 있다
for row in range(1, 6):
    for i in range(1, 6):
        print(mynum, end="  ")
        mynum = mynum + 1
    print("")

print("="*30)

'''
4.
    *
    **
    ***
    ****
    *****
'''

for row in range(1, 6):
    for i in range(1, row+1):
        print("*", end="  ")
    print("")
print("=" * 30)