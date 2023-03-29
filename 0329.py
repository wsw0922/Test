# a, b = 100, 10
# a *= b
# print("a : ", a)

# a, b = 100, 10
# a /= b
# print("a : ", b)

# a, b = 100, 10
# a -= b
# print("a : ", a)

# name = input("이름이 뭔가요?")
# print("제 이름은 ", name, "입니다.")
# age = input("나이는?")
# print("나이는 ", age, "입니다.")

# planet = input("원하는 행성은?")
# strRadius = input(planet + " 반지름은?")
# radius = int(strRadius)

# length = 2 * 3.14 * radius
# print(planet, " 반지름 : ", radius)
# print(planet, " 둘레길이 : ", length)

# school = "동양미래대"

# print("school[:] : ", school[:])
# print("school[0:3] : ", school[0:3])
# print("school[1:4] : ", school[1:4])
# print("school[2:4] : ", school[2:4])
# print("school[1:] : ", school[1:])

# school = "동양미래대학교-컴퓨터소프트웨어공학과"

# print("school[::] : ", school[::])
# print("school[0:len(school):2] : ", school[0:len(school):2])
# print("school[8:len(school):2] : ", school[8:len(school):2])
# print("school[8:len(school)] : ", school[8:len(school)])
# print("school[:15:4] : ", school[0:15:4])

num = input("6자리 실수 입력")
num = num.replace(".","")
int(num[0])
for i in len(num):
    print("sum : ", num[i], "+")