# 문자열의 구성을 체크하는 함수 : isXXXX (True or False를 리턴)

str1 = "12345"
str2 = "12345ffdds"
str3 = "test"
str4 = "테스트"
str5 = "test123"
str6 = "TEST"
print(str1.isdigit()) # "12345" 숫자?
print(str2.isdigit()) # "12345ffdds" 숫자?
print(str3.isalpha()) # "test" 문자?
print(str4.isalpha()) # "테스트" 문자?
print(str5.isalnum()) # "test123" 숫자문자?
print(str6.isupper()) # "TEST" 대문자?
print(str3.islower()) # "test" 소문자?
print(" ".isspace()) # 공백?