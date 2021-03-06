# 문자열관련함수 - 변환
# upper, lower는 대소문자

str1 = "Python P"
print(str1.upper())
print(str1.lower())
print(str1.swapcase())
print('test',title())

# 문자열은 함수를 적용해도 원본이 변경되지 않는다

# str1변수에 함수를 적용한 값이 재할당되도록 설정
print(str1.replace('Py','sy'))
print(str1)

str2 = "    data    data    data    "
# 데이터를 정제하는 과정에서 replace를 사용한다.
result2 = str2.replace(" ","")
print("replace적용결과 => ", result2)

str3 = "    data    da\nta     da\nta"
result3 = str3.replace(" ", "").replace("\n","")
print("replace적용결과 =>", result3)

str4 = "                python              "
print(str4,len(str4))
print(str4.lstrip(),len(str4.lstrip()))
print(str4.rstrip(),len(str4.lstrip()))
print(str4.strip(),len(str4.lstrip()))

print("test"+str(1234))