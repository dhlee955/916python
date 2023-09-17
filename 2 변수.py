# 변수 선언과 사용
# 변수명 = 값
a=1
b='hello'
c=3.3
print('a:',a)
print('b:',b)
print('c:',c)

# 주소 확인 : id()
print('a의 주소:',id(a))
print('b의 주소:',id(b))
print('c의 주소:',id(c))

# 동시에 변수 선언
x,y,z=1,3,5
print('x:',x)
print('y:',y)
print('z:',z)
print('x의 주소:',id(x))
print('y의 주소:',id(y))
print('z의 주소:',id(z))

# 변수명 작성시 키워드 사용 x
# 키워드 확인
from keyword import kwlist
print(kwlist)