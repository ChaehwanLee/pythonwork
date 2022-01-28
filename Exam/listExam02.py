list3 = list("python programming")
print(list3)

# 2. 'python programming' 문자열을 리스트로 변환한 후
# python programming 으로 출력
for i in list3:
    print(i, end="")
print("")
print("="*30)

for i in range(0, len(list3),1): #range(18) / 0에서 시작, end-1, 1씩 증가
    print("{}".format(list3[i]),end="")
print("")
print("="*30)

# gnimmargorp nohtyp의 형태로 출력 (mail)

for i in range(len(list3)-1,-1,-1): # 증가는 n-1 감소는 n+1
    print("{}".format(list3[i]),end="")
print("")
print("="*30)