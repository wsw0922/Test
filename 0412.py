# 자료형 - 리스트[item], 튜플(item), 딕셔너리{key : value}, 집합

# 빈 리스트를 만들어 하나씩 원소 추가
lst = []
print(type(lst)) # <class'list'>
lst.append("김밥")
lst.append("햄버거")
lst.append("감자튀김")
print(lst)  # ['김밥', '햄버거', '감자튀김']
lst.insert(0, "붕어빵") # 0번 인덱스에 "붕어빵" 들어감
lst.insert(0, "크림빵")
# 리스트 출력
print(lst) # ['크림빵', '붕어빵', '김밥', '햄버거', '감자튀김']
print("list 3th index : ", lst[2]) # 김밥
for i in range(len(lst)) : 
    print(lst[i]) # 크림빵 붕어빵 김밥 햄버거 감자튀김
for item in lst : 
    print(item) # 크림빵 붕어빵 김밥 햄버거 감자튀김
# list count(리스트의 감자튀김 개수), index(몇 번째 인덱스에 처음 나오는지)
lst.append("감자튀김")
lst.append("감자튀김")
print('count 감자튀김, index 감자튀김', lst.count("감자튀김"), lst.index('감자튀김'))
# slicing --> lst[start : end : step]
# lst = [크림빵, 붕어빵, 김밥, 햄버거, 감자튀김, 감자튀김, 감자튀김] --> 7
print(lst[::]) # 전체 출력
print(lst[:len(lst):1]) # 25번째 줄이랑 출력 같음
print(lst[0:7:2]) # 크림빵 김밥 감자튀김 감자튀김
print(lst[3:5:1]) # 햄버거 감자튀김
print(lst[::-1]) # 리스트 역순 출력
print(lst[:4:3]) # 크림빵 햄버거

# list remove
lst.remove("붕어빵")
lst.remove('감자튀김') # 3개 있음. 앞에 있는 것이 우선적으로 사라짐
print(lst)
item1 = "커피"
if item1 in lst : # valueError 예방. item1이 lst안에 있으면 삭제
    lst.remove(item1)
    print("커피 존재함", lst)
else :
    print("커피 존재 안 함", lst)
# pop
print(lst)
print('lst.pop() : ', lst.pop()) # 맨 마지막 원소값 뺌
print(lst) # 감자튀김 삭제됨
print('lst.pop() : ', lst.pop(0)) # 0번째 pop
print(lst) # 크림빵 삭제됨

# list끼리의 합침
dessert = ['케이크', '커피', '우유', '와플']
print(dessert)
lst.extend(dessert) # lst에 dessert 추가됨
print(lst) # 김밥 햄버거 감자튀김 케이크 커피 우유 와플

# 원본이 바뀌는 않는 경우 == 내장함수는 바뀌지 않음, 단지 return만 해줌
l1 = ['orange', 'apple', 'mango', 'kiwi', 'banana']
print(sorted(l1)) # apple banana kiwi mango orange
print(l1) # orange apple mango kiwi banana

# 원본이 바뀌는 경우 == .remove , .sort 등
l1.sort()
print(l1) # apple banana kiwi mango orange

# reverse
l1.reverse()
print(l1) # orange mango kiwi banana apple

# clear
l1.clear()
print(l1) # 전체 삭제, 출력 값 없음 : []

# 리스트 컴프리핸션 = 리스트를 선언할 때 짧고 간결하게 하고 싶다
# 1. 그냥 선언 l2 = [0,1,2,3,4,5,6,7,8,9,10]
# 2. for, append 사용 
l2 =[]
for i in range(11) :
    l2.append(i)
print(l2)
# 3. @@ 리스트 컴프리핸션 @@
cList1 = [ i for i in range(11)]
print('리스트컴프리핸션 : ', cList1)

# 0~10 까지 숫자의 제곱을 리스트에 넣어라
cList2 = [i**2 for i in range(11)]
print(cList2) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 0~10까지의 숫자의 3배수를 리스트에 넣어라
cList3 = [i*3 for i in range(11)]
print(cList3)

# hello를 10번 넣어라
cList4 = ["hello" for i in range(11)]
print(cList4)

# 0~10까지 짝수들의 제곱을 리스트에 넣으세요
# cList5 = [(i*2)**2 for i in range(6)]
cList5 = [i**2 for i in range(11) if i % 2 == 0]
print(cList5)

# 0~10까지 6배수 제곱을 리스트에 넣으세요
cList6 = [i**2 for i in range(11) if i % 2 == 0 if i % 3 == 0]
print(cList6)

# list 복사
a = [0, 4, 16, 36, 64, 100]
b = a
a.pop()
print('a : ', a) # 100이 빠짐
print('b : ', b) # b도 a의 주소를 갖고 있기 때문에 100이 빠짐
# a is b : a와 b가 같은 메모리를 갖고 있는지(True -> shallow copy / False)
print(a is b) # true
b.append(333)
print(a)
print(b)
print(a is b) # true , shallow copy
# a와 값은 같지만 다르게 동작하길 원함 -> c = a[:]
c = a[:]
print(a)
print(c)
a.remove(333)
c.append(555)
print(a) # 333이 지워진 값 출력
print(c) # 0 4 16 36 64 333 555 --> a의 변동사항과 연결되어 있지 않음
print(a is c) # False , deep copy

# 시험 : 리스트, 튜플, 딕셔너리셋까지 나옴 챕터 6까지 범위 + git
