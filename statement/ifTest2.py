'''여러 줄 주석문 사용하기
    if문 안에서
    if문을 중첩해서서사용하기
    점수와 시험횟수 파악하기
    점수가 60점 이상이고 시험횟수가 3이하면 합격격
'''

jumsu= 87 #변수에 값 저장
examcout = 2 #변수에 값 저장
if jumsu>=60: #변수가 60점 이상
    if examcout<=3: # 위의 조건을 만족하는 데이터중 examcount가 3이하 데이터는 합격처리
        print("합격")
    else: # 점수가 60점 이상이지만 examcount 가 3보 크면 불합격으로 처리
        print("불합격")
else:
    print("불합격")