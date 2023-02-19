var1 = 100
print(id(var1))
print(type(var1))


# 실수-> 정수
a = int(10.5)
b = int(20.42)
add = a + b
print('add = ', add)

a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)

a ** 2


#여러 줄 문자열
multiline = """ Hi
my name is
Jae In """
print(multiline)


multiline2="Hi\nmy name is\nJae In"
print(multiline2)


#문자열 색인
string = "PYTHON"
print(string[0])

print(string[1])

print(string[-5])


#문자열 연산
print("I am " + str(24) + "years old")


print("가지마" * 20)


#나머지 계산
div1 = 10 % 3
print(div1)


# 몫 계산
div2 = 10//3
print(div2)

10.3%2.5


# 논리연산자
result1 = 30 > 50
print(result1)

result2 = 30 > 50 or 70 > 50
print(result2)


# 대입연산자
i = tot = 10
i += 1
tot += i
print(i, tot)


# 두 변수의 값 교체
v1, v2 = 100, 200
v2, v1 = v1, v2
print(v1, v2)
v3, v1 = v1, v2
print(v1,v2,v3)

# 패킹 할당 연산자
lst = [1,2,3,4,5]
v1, *v2 = lst
print(v1, v2)       # 1 [2, 3, 4, 5]
*v1, v2 = lst
print(v1, v2)       # [1, 2, 3, 4] 5


# 조건문 - 단일 조건문
var = 10
if var >= 5 :
    print('var = ', var)
    print('var는 5보다 크다.')
    print('조건 만족')

print('항상 실행')
    

# 100~85: 우수, 84~70: 보통, 69이하: 저조
score = int(input('점수 입력: '))

if score >= 85 and score <= 100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
    else :
        print('저조')



# 중립조건문
if score >= 85 and score <= 100 :
    grade = 'A'
elif score >= 70 :
    grade = 'B'
else :
    grade = 'C'
print ('당신의 점수는 %d이고, 등급은 %s' %(score, grade))



# 한 줄 조건문
n = 9

if n >= 5 :
    result = n * 2
else : 
    result = n + 2
print('result: ', result)
print('결과는 %d' %result)

result2 = n * 2 if n >= 5 else n + 2
