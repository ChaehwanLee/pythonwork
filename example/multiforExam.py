'''
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