# 딕셔너리에 저장된 데이터 수정
dict1 = {1: "python", 2:"C", 3 :"android", 4:"arduino"}
dict2 = {"key1":10000, "key2":20000, "key3":40000, "key4":500000}
print(dict1)
print(dict2)

# 기존의 없는 키를 추가하는 경우 -> 새롭게 추가된다
dict1[5] = "raspberry PI"
dict2["key5"] = 1000000
print(dict1)
print(dict2)

# 기존의 데이터에서 있는 키를 가지고 작업하는 경우 - 키는 중복이 불가능하므로 수정된다.
dict1[5] = "raspberry PI와 IoT플랫폼 구축"
dict2["key5"] = 12000000
print(dict1)
print(dict2)

# 딕셔너리의 요소 삭제
del(dict1[5])
del(dict2["key5"])
print(dict1)
print(dict2)
