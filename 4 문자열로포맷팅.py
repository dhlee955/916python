name='손우주'
age=20
print(name+'의 나이는 '+str(age)+'세입니다.')
# format()
print('{}의 나이는 {}세입니다.'.format(name,age))
# f-strings
print(f'{name}의 나이는 {age}세입니다.')
# %타입기호
print('%s의 나이는 %d세입니다.' % (name,age))

# 너비와 정렬 지정
print('{:10}'.format(name))
print('{:<10}'.format(name))
print('{:>10}'.format(name))
print('{:^10}'.format(name))

# 소수 자릿수 지정
num=3.141
print(num)
print('{:.1f}'.format(num))
print('{:5.1f}'.format(num))
print('{:5.2f}'.format(num))
print('{:05.2f}'.format(num))

# 10진수를 2, 8, 16진수로 변환
number=int(input('10진수 입력:'))
print('2진수:{:08b}'.format(number))