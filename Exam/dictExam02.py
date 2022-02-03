# 예제 2
dict1 = {
        "삼성전자":[81000, 825000, 90800, 89300, 90000],
        "LG전자":(150000, 149000, 151000, 144000, 152500)
        }

# for key, value in dict1.items():
#         print("{}:{}".format(key,value))
#         for data in value:
#                 print(data)

for key, value in dict1.items(): # dictionary에서 key 와 value를 추출하기
        print("{}:{}".format(key),end=":") # 키만 출력
        for data in value: # 추출한 value가 list or tuple 이므로 각 요소의 값을 for 로 엑세스 - 딕셔너리의 value안에 저장된 요소를 접근하는 for
                print(data, end="")
        print("")