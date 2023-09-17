# sep 옵션: 출력값이 여러 개일 때 기본 공백으로 대신 다른 값을 지정할 수 있다.
print(1,2,3,sep='/')
print(1,2,3,sep=':')

# end 옵션: 인쇄후 기본 줄바꿈(\n)되는데 줄바꿈 대신 다른 값을 지정할 수 있다.
print(10,end='')
print(20,end='/')
print(30)

# multi line : 행의 마지막에 오는 \는 줄바꿈을 하지 말라는 뜻
print('''\
파이썬
	파이썬
 		파이썬\
''')

# escape character
print('안녕하세요!\n한국에 \t살고 있습니다.')

# raw string
file_path=r'c:\test\cat.png'
print(file_path)

# 크리스마스 트리 만들기
print('''
	*
   ***
  *****
 *******
''')
