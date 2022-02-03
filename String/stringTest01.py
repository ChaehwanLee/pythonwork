# 문자열 작성하기
str1 = "python"
str2 = 'python'
str3 = '''
        python 
        programming
       '''
str4 = """
        python
        programming
       """

print(str1, type(str1))
print(str2, type(str2))
print(str3)
print(str4)

# 문자열 +, *연산자
str5 = "python programming"
str6 = "재밌다."
print(str5+str6) # 문자열에서 +는 연결연산자
print(str6*2)

# 문자열을 구성하는 문자는 내부적으로 숫자값을 가지고 있다. -> ASCII 코드
# 문자를 ASCII로 변환
ch = "a" # 소문자 a = 97 z = 122
ch2 = "A" # 대문자 A = 65 Z = 90
print(ch)
print(ch2)

# 문자-> ASCII로 변경하는 함수
print(ord(ch))
print(ord(ch2))

data = 100

# chr : ASCII -> 문자
print(chr(ord(ch)+3)) # a의 ASCII 값 + 3 한 값을 다시 문자로 변경