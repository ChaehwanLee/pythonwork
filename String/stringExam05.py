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

mystr = """
        Python is an easy to learn, powerful programming language. 
        It has efficient high-level data structures and a simple but 
        effective approach to object-oriented programming. 
        Python’s elegant syntax and dynamic typing, 
        together with its interpreted nature, make it an ideal language for 
        scripting and rapid application development in many areas on most platforms.
        """