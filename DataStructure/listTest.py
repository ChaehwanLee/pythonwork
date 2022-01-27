# 데이터를 효율적으로 관리하기 위한 그릇

# num1 = 100
# num2 = 95
# num3 = 50
# num4 = 100
# num5 = 98
#
# subject1 = "python"
# subject2 = "javascript"
# subject1 = "android"
# subject2 = "raspberryPI"
# subject1 = "mqtt"

# 이런 방법 대신에 리스트를 사용한다

# 정수 데이터 5개를 저장하는 리스트
jumsu_list = [100, 95, 50, 100, 98]
subject_list = ["python", "javascript","android","raspberryPI","mqtt"]
subject_list2 = ['python', 'javascript','android','raspberryPI','mqtt']
mylist = [123, "python"]
print(jumsu_list)
print(subject_list)
print(subject_list2)
print(mylist)

# 리스트에 저장된 데이터(요소) 엑세스
print(jumsu_list[0])
print(jumsu_list[1])

# 사용자정의 리스트의 타입을 확인
print("타입=", type(jumsu_list))
print("타입=", type(subject_list))
print("타입=", type(subject_list2))
print("타입=", type(mylist))

# 리스트에 저장된 모든 요소를 엑세스
# for 문이 실행될 때마다 리스트에 저장된 요소가 i에 저장된다.
for i in jumsu_list:
    print(i, end="  ")
