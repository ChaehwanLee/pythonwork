# 딕셔너리의 내장함수
dict1 = {1: "python", 2:"C", 3 :"android", 4:"arduino"}
dict2 = {"key1":10000, "key2":20000, "key3":40000, "key4":500000}

print(dict)
print("key=",dict1.keys()) # 딕셔너리에서 키만 추출
print("key=",list(dict1.keys()))

print("value=",dict1.values()) # 딕셔너리에 저장된 valuse만 추출
print("value=",list(dict1.values()))

print(dict1.items()) #key, value 한 쌍을 모두 추출

print(1 in dict1) # 1이라는 키가 dict1이라는 딕셔너리에 존재하면 True를 리턴
print('1' in dict1)
print(type('1'))
print(type(1))

