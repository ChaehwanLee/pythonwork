# zip함수 - 길이가 같은 리스트등의 자료구조를 하나로 묶어줄 수 있다.

list1 = ["python", "raspberry PI", "IoT", "MQTT"]
list2 = ["basic", "라즈베리파이의 사용방법", "IoT플랫폼구축", "통신"]
list3 = (80, 40, 40, 40) # 자료의 형태는 괄호로 구분 [ ], ( ), { }

for subject, info, time in zip(list1, list2, list3):
    print("{}:{}:{}".format(subject,info,time))

