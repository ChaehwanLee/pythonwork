# 주어진 문자열에서 알파벳의 각 갯수를 딕셔너리에 넣어서 출력하세요 (https://docs.python.org/3/tutorial/index.html)
# [조건]
# - 문자열인 경우만 체크하기
# - 빈 딕셔너리를 만들어서 값 저장하기
# - 대소문자가 같이 있는 경우 (소문자나 대문자로 변경해서 체크)
# - 영문자가 key로 반복횟수가 value로 저장
# - for 문을 이용하고 for 문 안에서 딕셔너리를 검색해서 키가 존재하는지 확인하면서 작업하기
# - 키가 있으면 value를 꺼내서 1을 더하고 다시 저장(딕셔너리 value를 변경)
# - 키가 없으면 새로 추가(새로운 요소를 딕셔너리에 추가)
# [출력형태]
# {'p':16, 'y':50, ... } (mail)

'''
[step]
    1. for문으로 문자를 출력하기
        p
        y
        t
        ...
    2. 공백을 빼고 문자만 출력하기
    3. for 문 밖에서 count 변수 선언하고 for 문이 실행될 때마다 count 변수에 1씩 더해서
       for문이 종료된 후 count 변수 값 출력하기
       count 값: _____
    4. for 문 위에서 빈딕셔너리 추가하기
    5. for 문 안에서 문자를 키로 1을 딕셔너리에 저장하기
       count변수에 저장된 숫자만큼 딕셔너리에 값이 저장
'''



mystr = """
        Python is an easy to learn, powerful programming language. 
        It has efficient high-level data structures and a simple but 
        effective approach to object-oriented programming. 
        Python’s elegant syntax and dynamic typing, 
        together with its interpreted nature, make it an ideal language for 
        scripting and rapid application development in many areas on most platforms.
        """

# print(not "a".isalpha())
dict1 = {1:"a",2:"b"}
print(1 in dict1) # 1이라는 키가 dic1 이라는 딕셔너리의 키가 맞아?
print(not 1 in dict1) # 1이라는 키가 없는 거 맞지? 1 in dic1 연산결과를 invert


alphabetdic = dict()
for c in mystr:
    if c.isalpha(): # 문자인 경우만 체크하기 위해 if로 조건 적용
        print(c)
        c = c.lower() # 대소문자 구분없이 작업하기 위해 변경
        # 키가 없는 경우는 딕셔너리에 추가하고 키가 있으면 키를 꺼내서 1을 더하기
        if c in alphabetdic: # 딕셔너리에 키가 있는지 체크
            alphabetdic[c] = alphabetdic[c] +1 # 수정
        else:
            alphabetdic[c] = 1 # 추가
    # else:
    #     # print("공백")
    #     pass # 아무런 실행을 원하지 않을 때 정의하는 명령문 : if, for, while

print(alphabetdic)