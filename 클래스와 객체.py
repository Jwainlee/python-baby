# 클래스와 객체
class person :
    name = None
    age = 0
    spouse = None

    def __init__(self, name, age, spouse) :
        self.name = name
        self.age = age
        self.spouse = spouse

    def display(self) :
        print('나 %s쓰 %d살인디 %s 내 거다' %(self.name, self.age, self.spouse))
        
p1 = person('재인', 24, '정세운')
p1.display()

# 응용 - 성별에 따라 호칭 바꾸기
class person1 :
    name = None
    age = 0
    gender = None                   # M / F
    spouse = None
    title = None

    def __init__(self, name, age, gender, spouse) :
        self.name = name
        self.age = age
        self.gender = gender
        self.spouse = spouse
        title = '와이프다' if self.gender == 'F' else '남편이다'
        self.title = title

    def display(self) :
        print('나 %s쓰 %d살이고 %s %s' %(self.name, self.age, self.spouse, self.title))
        
p1 = person1('재인', 24, 'F', '정세운')
p1.display()       
        

# 생성자 사용
class mul :
    x = 0
    y = 0

    def __init__(self, x, y) :                  # 생성자: 객체 생성 + 초기화
        self.x = x
        self.y = y

    def m(self) :
        return self.x * self.y

obj = mul(10, 20)
print('곱 = ', obj.m())

        
# 생성자 없음
class mul1 :
    x = y = 0

    def data(self, x, y) :                      # 생성자 대신 메서드 사용
        self.x = x
        self.y = y

    def m(self) :
        return self.x * self.y

obj1 = mul1()                           # 1단계
obj1.data(10, 30)                      # 2단계
print('곱 = ', obj1.m())


# 속성, 생성자 없음
class mul2 :
    def data(self, x, y) :
        self.x = x
        self.y = y

    def m(self) :
        result = self.x * self.y
        self.display(result)

    def display(self, result) :
        print('곱 = %d' %result)

obj2 = mul2()
obj2.data(10, 40)
obj2.m()                        # 이미 메서드 안에 print()가 있어서 print(obj2.m())을 하면 안 됨



