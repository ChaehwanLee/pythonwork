# 문자열 검색관련 함수 - count, index, find
str1 = "Python P"
result = str1.count("P")
print(result, "개의 문자가 반복 출력됨")

# index() vs find()
# 문자열내에 지정된 문자가 존재하는 경우 동일한 결과
print(str1.index("y"),"번 위치")
print(str1.find("y"),"번 위치")

# 문자열내에 지정한 문자가 존재하지 않는 경우
print(str1.find("j"), "번 위치") # 찾는 문자가 없는 경우 -1 리턴
# print(str1.index("j"), "번 위치") # 찾는 문자가 없는 경우 에러가 발생

# 해당 문자열로 시작, 종료하는지 확인(True or False return)
str2 = "python programming"
if str2.startswith("py"):
    print("OK")
else:
    print("Fail")
    
if str2.endswith("ing"):
    print("OK")
else:
    print("Fail")
