# dict1 = {1: "삼성전자", 2: "LG전자"}
# dict2 = {"key1":82000, "key2":152000}
# print(dict1)
# print(dict2)
# print("="*30)
#
# sam = {"key1":81000, "key2": 825000, "key3":90800, "key4":89300, "key5":90000}
# lg = {"key1":150000, "key2": 149000, "key3":151000, "key4":144000, "key5":152500}
# print("="*30)
#
# print("sam=",list(sam.items()))
# print("lg=",tuple(lg.items()))
# print("="*30)
#
# for key, value in sam.items():
#     print("{}={}".format(key, value))
# print("="*30)
# for key, value in lg.items():
#     print("{}={}".format(key, value))
#
# dict3 = {"python":'pycharm', "web":'django', "arduino":'led', "raspberryPI":'camera', "android":'android studio'}
#
# dict3 = key, value
# print(dict3)
#
# while key in dict3:
#     print("알고싶은 과목은?", value)
#
# print("="*100)

# 예제 1
dict1 = {"삼성전자":82000, "lg전자":152000}
print(dict1)
for key, value in dict1.items():
    print("{}의 가격은 {} 입니다.".format(key,value))
