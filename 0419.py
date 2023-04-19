# 6단원까지 + 깃. 책에서 많이 나옴, 객관식 절반, 주관식(코딩 + 서술형)
# tuple 수정, 삭제 불가능
t1 = (1,2,2,2,2,2,2,3,4,5)
t2 = 10,20,30,40,50 # 소괄호 안 해도 투플로 인식됨.
print(t1)
print(t2) # (10,20,30,40,50)
print(t1.count(2)) # 6 출력
print(t1.index(2)) # 1 출력

t3 = 10,
print(type(t3)) # <class 'tuple'>
print(t3) # (10,)

# 커피숍 프로그램(투플을 수정하기 위한 방법)
menu = ("아메", "라떼", "유자차")
# 아이스티 추가
menu1 = list(menu) # 리스트로 변경
print(menu1)
menu1.append("아이스티") # 리스트 menu1에 아이스티 입력
print(menu1)
menu = tuple(menu1) # tuple 로 변경
print(menu) # ('아메', '라떼', '유자차', '아이스티')

# list.sort = 원본이 바뀜 / sorted() = 원본이 바뀌지 않음
t2 = 1074, 205, 3, 40, 50
print(sorted(t2)) # sorted된 값 출력 : [3, 40, 50, 205, 1074]
print(t2) # 원본은 바뀌지 않음 : (1074, 205, 3, 40, 50)

t10 = 1, 2, 3, 4, 5
for i in 1, 2, 3, 4, 5 : # in 다음이 투플 사용
    print(i)


# dictionary : key, value
# d1 = { k1:v1, k2:v2, k3:v3, k4:v1} # key는 중복 불가임
student = {}
d2 = dict()

# 사전에 값을 추가
# 추가 방법 1 : 선언
student[101] = '홍'
student[102] = '김'
student[103] = '박'
print(student) # {101: '홍', 102: '김', 103: '박'}
print(student[101]) # key 값을 집어넣어 그에 대응하는 value를 가져올 수 있음. 출력 : 홍

lec = {}
lec['강좌명'] = '파이썬'
lec['개설년도'] = 2023
lec['수강생'] = ['홍', '김', '박', '고']
lec['인원'] = 35
print(lec)
lec['인원'] = 20 # 재정의
print(lec)
# 추가 방법 2 : update
lec.update({'인원' : 10}) # dictionary.update({key : value}), 인원:10으로 바뀜
print(lec)
lec.update({'강의실': 213, '교수': '이희진'}) # 새로운 키가 들어오면 추가된다.
print(lec)

# month
month = {'k1':'1월', 'k2':'2월', 'k3':'3월', 'k4':'4월', 'k5':'5월', 'k6':'6월', 'k7':'7월', 'k8':'8월', 'k9':'9월', 'k10':'10월', 'k11':'11월', 'k12':'12월'}
# for i in range(1,13) :
    # print(month[i])
# mIn = int(input("숫자를 입력하세요 : "))
# print(month[mIn])

print(month.keys()) # 키 출력
print(month.values()) # value 출력
print(month.items()) # key, value 출력

for i in month.keys() :
    print(month[i]) # 1월 ~ 12월 출력
for i in month.values() : 
    print(i) # 1월 ~ 12월 출력
for i in month.items():
    print(i) #(key, value) 출력(1~12)

for i in month.items() : # (key, value)와 같이 출력되기 때문에 투플임. 따라서 인덱스 번호를 사용한 출력이 가능함
    print("key : ", i[0]) # 인덱스 0번
    print("value : ", i[1]) # 인덱스 1번

for i in month :
    print(i) # 키 값만 출력됨

print(month.get('k1')) # 1월
print(month.get('key100')) # None
print(month['k1']) # 1월
# print(month['key100'])

# 삭제
print(month)
print(month.pop('k1')) # key 값을 주어야 함. 
print(month) # 2월부터 출력됨
month.popitem() # 맨 마지막 삭제
print(month) # 2월 ~ 11월 출력

# zip(), enumerate()
l1 =['한식', '중식', '일식']
l2 = ['전주식당', '전가복', '동명']
l3 = ['제육', '탕수육', '연어덮밥']

z = zip(l1, l2, l3)
print(type(z)) # <class 'zip'>
print(z) # <zip object at 0x000002903702F3C0>
print(list(z)) # [('한식', '전주식당', '제육'), ('중식', '전가복', '탕수육'), ('일식', '동명', '연어덮밥')]
# l2 = key, l3 = value
z1 = zip(l2, l3) # dict는 무조건 2개여야 함, 아닌 경우 에러 
print(dict(z1)) # {'전주식당': '제육', '전가복': '탕수육', '동명': '연어덮밥'}
# 중첩 사용 
z2 = zip(l1, zip(l2, l3))
print(dict(z2)) # {'한식': ('전주식당', '제육'), '중식': ('전가복', '탕수육'), '일식': ('동명', '연어덮밥')}

l4 = ['제육', '탕수육', '연어덮밥']
print(enumerate(l4)) # 메모리 형태
print(list(enumerate(l4))) # [(0, '제육'), (1, '탕수육'), (2, '연어덮밥')]
print(dict(enumerate(l4))) # {0: '제육', 1: '탕수육', 2: '연어덮밥'}

# 문제
# 과목을 주면 강의실을 알려주는 시스템
subject = ['파이썬','자바','c++','AI','알고리즘']
classroom = [101,102,103,104,105]
# 1. dict으로 변환해 사용
systemD = dict(zip(subject, classroom))
# 2. 무한루프로 강의실을 알림
# 3. quit 단어-> 시스템 종료
# 4. 다른 과목 -> "몰라요"
# 5. continue, break 사용
agin = True
while(agin) : 
    c = input("과목을 입력하세요 : ")
    if c == 'quit' :
        print("시스템을 종료합니다.")
        break
    if c in systemD.keys() : 
        print("강의실은 ", systemD[c], "호입니다.")
    else : 
        print("몰라요")
        # continue // 뒤에 코드가 더 있다면 생략 한다
    
    
