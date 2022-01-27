
totalVal = 0 # 총합이 저장되는 변수
oddVal = 0 # 홀수의 합이 저장되는 변수
evenVal = 0 # 짝수의 합이 저장되는 변수
i = 1
while i <= 100:
    totalVal = totalVal + i
    if i % 2 == 0:
        evenVal = evenVal + i
    else:
        oddVal = oddVal + i
    i = i + 1

print("총합 : %d"% totalVal)
print("홀수합 : %d" % oddVal)
print("짝수합 : %d" % evenVal)
