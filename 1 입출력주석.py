'''
학습 내용: print()
문자열은 따옴표 안에 넣기
문자열+문자열은 연결
값들은 공백으로 구분
'''

print(10)
print('hi~')
print(1+2+3-4*3/2)
print('life '+'is too short')
print()
print(10,20,30)
print('a','c','e')

"""
학습 내용: input()
입력값을 무조건 문자열로 저장
수치 연산에 사용하려면 숫자형으로 변환
    int(), float()
문자와 숫자 연산 x, 타입(종류)가 같아야 연산 가능함
"""
name=input('enter your name: ')
print(name+'님 안녕하세요!')

age=int(input('enter your age: '))
print(age-1)

'''
프로그램 기능 : 간단한 사칙연산기
'''
num1=int(input('enter first number: '))
num2=int(input('enter second number: '))
print(num1,'+',num2,'=',num1+num2)
print(num1,'-',num2,'=',num1-num2)
print(num1,'*',num2,'=',num1*num2)
print(num1,'/',num2,'=',num1/num2)