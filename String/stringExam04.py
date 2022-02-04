# 구글입사문제 풀기
# - 1부터 10000까지의 숫자에서 8이라는 숫자가 총 몇 번 나오는지 체크하기
# - 8이 포함되어 있는 숫자의 갯수를 카운팅하는 것이 아니라 8이라는 숫자가 몇 번 나오는지 카운트
# - 예를 들어 8888은 4로 카운팅, 1288은 2로 카운팅
# - for 문을 중첩해서 사용 : 로직으로 구현하기
# - 로직으로 구현하는 것이 끝나면 함수로 구현해보기 : count 활용
# - 정답 : 4000

# data = 1000
# for i in str(data):
#     print(i, type(i))
# range 는 숫자라서 안되겠구나

# for i in range(1,10001):
#     print("i=", i)
#     for k in str(i):
#         print('K=',k)
#         if k == "8":
#             print(k,"8이다")

count = 0 # 8의 횟수를 저장할 변수 #숫자는 반복작업을 못해서 숫자를 문자열로 변환해서 한 문자씩 접근 후 비교작업 수행
for i in range(1,10001):
    for k in str(i):
        if k == "8":
            count = count + 1

print("8의 횟수=", count)

print("="*50)
mycount = 0
for i in range(1, 10001):
    mycount = mycount + str(i).count("8")
print("8의 횟수=", count)

