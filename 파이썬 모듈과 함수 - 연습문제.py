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
        print ('현재 계좌 잔액은 %d원 입니다' %self.balance)

    def deposit(self) :
        money1 = int(input('입금액을 입력하세요 : '))
        self.money1 = money1
        self.balance += self.money1
        print ('입금 후 잔액은 %d원 입니다' %self.balance)

    def withdraw(self) :
        money2 = int(input('출금액을 입력하세요 : '))
        self.money2 = money2
        if self.balance < self.money2 :
            print('잔액이 부족합니다')
        else :
            self.balance -= self.money2
            print('출금 후 잔액은 %d원 입니다' %self.balance)

        





















