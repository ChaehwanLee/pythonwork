# 사용자정의 패키지의 모듈 import하고 테스트
# testpkg에서 myproduct 모듈을 import하고 작업
# from 패키지명 import 모듈명
from testpkg import myproduct, moduleB

myproduct.test1()
moduleB.test5()