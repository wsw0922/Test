def addthree(num):
    return num + 3
result = addthree(100)
print(addthree(100))
print(result)

def printaddthree(num):
    print(num+3)
printaddthree(100)

def printName(name1, name2):
    print("hello ", name1, ", hello ", name2)
name1 = input("이름을 입력하세요 : ")
name2 = input("이름을 입력하세요 : ")
printName(name1, name2)

def sum(num1, num2):
    return num1+num2
num1 = int(input("숫자를 입력하세요"))
num2 = int(input("숫자를 입력하세요"))
print(sum(num1, num2))

print((lambda n1, n2 : n1*n2)(3,5)) # 15 출력

# map(function, list)
# map(function, [1,2,3,4,5])
# [function(1),function(2),fu1nction(3),function(4),function(5)]

# map(addthree, [10,20,30,40,50])
# [addthree(10),addthree(20),addthree(30),addthree(40),addthree(50),]

print(list(map(addthree, [10,20,30,40,50]))) # [13, 23, 33, 43, 53]
print(list(map((lambda x : x + 3), [10,20,30,40,50]))) # [13, 23, 33, 43, 53]

lst = [1,2,3,4,5,6]
def f1(n):
    return n * 5 + 10
print(list(map(f1, lst))) # [15, 20, 25, 30, 35, 40]
print(list(map((lambda x : 5 * x + 10), lst))) # [15, 20, 25, 30, 35, 40]

lst10=[10,20,30,40,50]
lst11=[1,2,3,4,5]
def f2(n1, n2):
    return n1+n2
print(list(map(f2, lst10, lst11))) # [11, 22, 33, 44, 55]
print(list(map((lambda x, y : x+y), lst10, lst11))) # [11, 22, 33, 44, 55]


# map(function, list)
# filter(function, list)

def positive(x):
    if x > 0 :
        return True
    else:
        return False
print(list(filter(positive, [10, -3, -5, 2, 0, 1]))) # [10, 2, 1]

def positive2(x):
    return x > 0
print(list(filter(lambda x :x > 0, [10, -3, -5, 2, 0, 1]))) # [10, 2, 1]


def is_even(x):
    if x%2 ==0:
        return True
    return False
arr1 =[]
for val in range(1,11):
    if is_even(val):
        arr1.append(val)
print(f"arr function : {arr1}") # arr function : [2, 4, 6, 8, 10]

arr2 = list(filter(is_even, range(1,11)))
print(f'arr filter : {arr2}') # arr filter : [2, 4, 6, 8, 10]
