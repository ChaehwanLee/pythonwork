# 딕셔너리 생성
dict1 = {1: "python", 2:"C", 3 :"android", 4:"arduino"}
print(dict1)
print(type(dict1))

dict2 = {"key1":10000, "key2":20000, "key3":40000, "key4":500000}
print(dict2)
print(type(dict2))

# 딕셔너리의 각 요소 액세스
print(dict1[1]) # 1번 키로 저장된 value를 추출
print(dict2["key1"])

subject = dict1[1]
price = dict2["key1"]
print("{} = {}".format(subject,price))

subject = dict1.get(2)
price = dict2.get("key2")
print("{} = {}".format(subject,price))

subject = dict1.get(7) # 키가 없는 경우 에러를 발생시키지 않고 None
# price = dict2["key7"] # 키가 없는 경우 에러 발생
print("{} = {}".format(subject,price))