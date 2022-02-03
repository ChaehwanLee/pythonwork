# 예제3
mydata = {"python":'pycharm', "web":'django', "arduino":'led', "raspberryPI":'camera', "android":'android studio'}

# mysubject = input("알고 싶은 과목은?"+str(list(mydata.keys())))

while True: #무한루프
    mysubject = input("알고 싶은 과목은?"+str(list(mydata.keys()))+"\n")
    if mysubject == "q":
        print("프로그램을 종료합니다.")
        break
    elif mysubject in mydata:
        print("필요장비 및 프로그램:{} -> {}".format(mysubject,mydata.get(mysubject)))
    else:
        print("그런 과목은 없습니다. 다시 입력해주세요")