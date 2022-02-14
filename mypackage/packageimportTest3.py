# testpkg 패키지의 모든 모듈을 import하기
# import 패키지명
# -> 전체 패키지의 모든 모듈을 한번에 import해서 쓸 수 있다.
# import하려는 패키지의 __init__.py 파일에 등록을 해야한다.
import testpkg

testpkg.moduleA.test2()
testpkg.moduleB.test5()

# testpkg에서 myproduct모듈을 등록하지 않아서 사용할 수 없습니다.
# testpkg.myproduct().test1()