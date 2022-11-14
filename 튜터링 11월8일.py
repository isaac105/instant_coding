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



