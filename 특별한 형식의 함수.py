# 몬테카를로 복습
import random
def coin(n) :
    result = []
    for i in range(n) :
        r = random.randint(0, 1)
        result.append(r)
    return(result)

def mont(n) :
    cnt = 0
    for i in range(n) :
        cnt += coin(1)[0]
    result = cnt / n
    return(result)

print(coin(10))
print(mont(10))



# 람다함수
adder = lambda x, y : x + y
print('adder = ', adder(5, 2))

print('adder = ', (lambda x, y : x + y)(5, 2))



# 함수 장식자 ; 래퍼함수
def wrap(func) :
    def decorated() :
        print('반가웠습니다')
        func()
        print('안녕히가세요')
    return decorated

@wrap
def name() :
    print('이재인 고객님')

name()

# 이름 입력받아보기 - 1차시
@wrap
def custom_name() :
    n = str(input('이름을 입력하세요: '))
    print('%s 고객님' %n)

custom_name()                            # 문제 ; 반가웠습니다 이름을 입력하세요: 안녕히가세요 순으로 나옴

# 이름 입력받아보기 - 2차시
n = str(input('이름을 입력하세요: '))
@wrap
def custom_name() :
    print('%s 고객님' %n)

custom_name()                            # 성공~



# 재귀함수
def count(n) :
    if n == 0 :
        return 0
    else :
        count(n-1)
        print(n, end = ' ')

count(10)                                       # 스택은 역순 호출이라 1부터 나옴

# 응용1 - 10부터 나오게 하고 싶으면?
def count(n) :
    if n == 0 :
        return 0
    else :
        print(n, end = ' ')                    # 마지막 2줄의 위치 바꾸기
        count(n-1)

# 응용2 - 누적합
def cum(n) :
    if n == 1 :
        return 1
    else :
        result = n + cum(n-1)
        print(n, end = ' ')
        return result
    
print('\n합: ', cum(100))
