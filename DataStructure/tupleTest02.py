# 튜플은 수정이 불가능
tuple1 = (10, 20, 30)
print(tuple1)

# 튜플은 데이터를 수정할 수 없으므로 튜플의 요소를 추가하거나, 수정하거나, 삭제할 수 없다.
# tuple1.append(100) # 리스트와 다르게 안 됨 'tuple' object has no attribute 'append'

print(tuple1[0]) # 하나의 요소에 접근을 할 때는 대괄호 사용
# tuple1[0] = 100 오류!(값을 수정할 수 없다) 'tuple' object does not support item assignment

# 튜플 전체를 삭제하는 것은 가능
del(tuple1)
print(tuple1)
