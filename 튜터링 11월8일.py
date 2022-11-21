# 1. 비어있는 사람(Human) 클래스를 정의하시오.
# 2. 사람 (Human) 클래스의 인스턴스를 생성하고, 본인의 이름 변수(ex.seyeon)로 바인딩하시오.
# 3. 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하시오.
# 4. 사람(Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하시오.
# 5. 사람(Human) 클래스에 (이름, 나이, 성별)을 출력할 수 있는 printName(), printAge(), printSex() 함수를 추가하시오.
# 6. (2)에서 생성한 인스턴스를 통해 (5)에서 만든 함수에 접근해 각각 이름, 나이, 성별을 출력하시오.
# 드래그 + ctrl +/ 슬래시 : 주석처리

#init : 초기화하다
class Human:
    def __init__(self,name,age,sex): # def 뒤에 한칸띄우고 __init__ !! 주ㅇ이이
        self.ahyoungname = name
        self.ahyounhage = age
        self.ahyoungsex = sex 
        print("응애응애")

ahyoung = Human('ahyoung','24','female')
print('이름:',Human.name) 
print('나이:',Human.age)
print('주소:',Human.sex) 

# 1. 원을 나타내는 Circle이라는 클래스를 생성하시오.
# 2. 원(Circle) 클래스의 인스턴스를 생성하고, circle이라는 변수에 바인딩하시오.
# 3. 원(Circle) 클래스에 반지름(radius), 중심좌표(x, y)를 입력받는 생성자를 추가하시오.
# 4. 원(Circle) 클래스에 원의 넓이를 반환하는 getArea() 함수를 추가하시오.
# -> hint. pi는 math library를 import 하여 사용하시오!
# 5. 원(Circle) 클래스에 원의 중심을 반환하는 getCenter() 함수를 추가하시오.
# 6. (2)에서 생성한 인스턴스에 각각 반지름과 중심좌표를 입력해주는데, 이는 사용자에게 직접 입력 받도록 하시오.
# 7. (4), (5)에서 생성한 함수를 이용해 원의 중심과 중심좌표를 출력하시오.

import math

class circle : #붕어빵만들기
    def __init__(self,radius,xpoint,ypoint):
        self.radius = radius
        self.xpoint = xpoint
        self.ypoint = ypoint
    def getArea(self): #class내에 함수를 호출할 때는 꼭 자기자신self가 호출되어야함.
        return self.radius * self.radius * math.pi  # return값으로 반지름*반지름*3.14(pi) 넓이를 구함. 값을 돌려줌
    def getCenter(self):
        return self.xpoint, self.ypoint
    
circle_xpoint = int(input("x좌표입력:"))
circle_ypoint = int(input("y좌표입력:"))
circle_radius = int(input("반지름입력:"))
원완성 = circle(circle_radius,circle_xpoint,circle_ypoint) #붕어빵찍기 #"원완성" -> 객체로 지정하기
print(원완성.getArea()) #함수호출시 꼭 괄호 getarea뒤에 괄호!!
print(원완성.getCenter())

# 1. 기차(Train) 클래스를 생성하시오.
# 2.기차(Train) 클래스의 인스턴스를 생성하시오.
# 3.기차(Train) 클래스에 기차 종류, 탑승 요금, 출발지, 도착지를 입력받는 생성자를 추가하시오.
# 4. Train 클래스에 기차를 움직이는 move() 라는 함수를 추가하시오.
# -> 출발지와 도착지를 출력하고, 출발지를 도착지로 변경
# 5. Train 클래스에 탑승 요금을 출력하는 getOn() 함수를 추가하시오.
# 6. Train 클래스에 출발지를 출력하는 getOff() 함수를 추가하시오.
# 7. Train 클래스에 기차의 정보를 출력하는 print() 함수를 추가하시오.
# -> 기차 종류, 출발지, 도착지, 탑승 요금을 출력

class Train :
    def __init__(self,sort,fee,start,stop):
        self.sort = sort
        self.fee = fee
        self.start = start
        self.stop = stop
    def move(self):
        print("출발지:",self.start)
        print("도착지:",self.stop)
        self.stop=self.start
    def geton(self):
        print("탑승요금:",self.fee)
    def getoff(self):
        print("출발지:",self.start)
    def print(self):
        print("기차종류:",self.sort,"출발지:",self.start,"도착지:",self.stop,"탑승요금:",self.fee)

mytrain = Train("ktx",25000,"서울역","이수역")
mytrain.geton()
mytrain.getoff()
mytrain.move()
mytrain.print()

# 1. 돈(Money) 클래스를 정의하시오.
# 2. 돈(Money) 클래스의 인스턴스를 생성하고, 본인의 이름 변수(ex.seyeon)로 바인딩하시오.
# 3. 돈(Money) 클래스에 money라는 클래스 변수를 생성한 뒤, 10000으로 초기화하는 생성자를 추가하시오.
# -> 반드시 10,000원이 아니여도 됨!! 본인이 원하는 초기값으로 셋팅.
# 4. 돈(Money) 클래스에 물건을 구매하는 buy_something() 함수를 추가하시오.
# -> 물건을 구매시, money가 차감되어야 함.
# 5. 돈(Money) 클래스에 돈을 적립할 수 있는 save_money() 함수를 추가하시오.
# 6. 돈(Money) 클래스에 현재 보유 현금을 출력하는 print_my_money() 함수를 추가하시오.
# 7. (2)에서 생성한 인스턴스를 통해 (4), (5)에서 만든 함수를 각각 사용해보고, (6) 함수를 통해 현재 보유 현금을 출력하시오.

class Money :
    def __init__(self) :
        self.money = 10000
    def buy_something(self,price) :
        if price > self.money : 
            print("보유금액이부족합니다.")
        else :
            self.money = self.money - price
    def save_money(self,point) :
        self.money = self.money + point
    def print_my_money(self) :
        print("현재보유현금은",self.money,"원입니다.")
ahyoung = Money()
ahyoung.self.buy_something(5000)
ahyoung.self.save_money(2000)
ahyoung.print_my_money()

# 1. 계좌(Account)라는 클래스를 생성하시오.
# 2. 계좌(Account) 클래스의 인스턴스를 생성하시오.
# 3. 계좌(Account) 클래스에 아래와 같은 생성자를 추가하시오.
# 1. 은행 이름, 예금주, 계좌번호, 잔액을 초기화 하시오.
# 2. 생성자에서는 예금주와 초기 잔액만 입력 받으시오.
# 3. 은행 이름은 "신한은행"으로 하시오.
# 4. 계좌 번호는 3자리-2자리-6자리로 랜덤하게 생성되도록 하시오. (random 함수 사용, zfill 함수 사용)
# 4. 계좌(Account) 클래스에 입금을 위한 deposite() 함수를 추가하시오.
# -> 입금은 최소 1원 이상부터 가능
# 5. 계좌(Account) 클래스에 출금을 위한 withdraw() 함수를 추가하시오.
# -> 계좌잔고가 부족할 경우 출력이 불가능하다는 메시지 표시
# 6. Account 인스턴스에 저장된 정보를 출력하는 display_info() 함수를 추가하시오. (은행이름, 예금주, 계좌번호, 잔고 출력)
# -> 잔고는 3자리마다 쉼표를 출력하시오. (ex. 10,000)
# 7. 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 (4)의 함수를 변경하시오

#print("3".zfill(3)) 문자열 앞0으로 채우기 -> 003
class Acoount :
    def __init__(self,name,money):
        self.bank = "신한은행"
        self.name = name
        self.money = money
        a= ("random.randint(1,999)".zfill(3))
        b= ("random.randint(1,99)".zfill(2))
        c= ("random.randint(1,999999)".zfill(6))
        self.account = a+"-"+b+"-"+c
    def deposite(self,deposite_money):
        deposite_money = deposite_money + money



