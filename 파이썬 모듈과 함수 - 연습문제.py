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


# 2
def bank_account(bal) :
    balance = bal
    
    def getBalance() :
        return balance
    
    def deposit(money) :
        global balance
        balance += money
        
    def withdraw(money) :
        global balance
        if balance < money :
            print('잔액이 부족합니다.')
        else :
            balance -= money
              
    return getBalance, deposit, withdraw

b, d, w = bank_account()




