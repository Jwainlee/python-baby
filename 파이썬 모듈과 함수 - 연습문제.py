# 연습문제

# 1
def StarCount(height) :
    cnt = 0

    for i in range(height) :
        if height == 0 :
            break
        else :
            print('*' * (i + 1), '\n')
            cnt += (i + 1)

    return cnt

height = int(input('height : '))
print('star 개수 : %d' %StarCount(height))



""" # 2 뭐가 문젠지 나중에 확인하기
def bank_account() :
    balance = int(input('최초계좌의 잔액을 입력하세요. : '))
    

    def getBalance() :
        print('현재 계좌 잔액은 %d원 입니다.' %balance)
    
    def deposit(money) :
        global balance
        money = int(input('입금액을 입력하세요. : '))
        balance += money
        print('%d원 입금 후 잔액은 %d원 입니다.' %(money, balance))
        
    def withdraw(money) :
        global balance
        money = int(input('출금액을 입력하세요 : '))
        if balance < money :
            print('잔액이 부족합니다.')
        else :
            balance -= money

        print('%d원 출금 후 잔액은 %d원 입니다.' %(money, balance))

    return getBalance, deposit, withdraw 
"""


# 2
class bank :
    balance = 0
    money1 = 0
    money2 = 0

    def getBalance(self) :
        balance = int(input('최초 계좌의 잔액을 입력하세요 : '))
        self.balance = balance
        result = self.balance
        print('현재 계좌 잔액은 %d원 입니다' %result)
        self.deposit(result)

    def deposit(self, result) :
        money1 = int(input('입금액을 입력하세요 : '))
        self.money1 = money1
        result += self.money1
        print('%d원 입금 후 잔액은 %d원 입니다' %(self.money1, result))
        self.withdraw(result)

    def withdraw(self, result) :
        money2 = int(input('출금액을 입력하세요 : '))
        self.money2 = money2
        if result < self.money2 :
            print('잔액이 부족합니다')
        else :
            result -= self.money2
            print('출금 후 잔액은 %d원 입니다' %result)
            
jaein = bank()
jaein.getBalance()



# 3
def fact(n) :
    if n == 1 :
        return 1
    else :
        result = n * fact(n-1)

    return result

result_fact = fact(5)
print('팩토리얼 결과: ', result_fact)



# 4
class Rectangle :
    width = 0
    height = 0

    def __init__(self, width, height) :
        self.width = width
        self.height = height

    def area_calc(self) :
        return self.width * self.height

    def circum_calc(self) :
        return (self.width + self.height) * 2

print('사각형의 넓이와 둘레를 계산합니다.')
w = int(input('사각형의 가로 입력: '))
h = int(input('사각형의 세로 입력: '))

print('-' * 30)
rec = Rectangle(w, h)
area = rec.area_calc()
circum = rec.circum_calc()
print('사각형의 넓이: ', area)
print('사각형의 둘레: ', circum)
print('-' * 30)




        









