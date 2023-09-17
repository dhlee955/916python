# # 산술 연산자
# # **: 거듭제곱, //: 몫, %: 나머지
print(10**10)
print(5 // 3)
print(5 % 3)
print(divmod(5, 3))

# # 복합 대입 연산자
# # +=,  -=, ...
cnt = 0
cnt += 1  # cnt=cnt+1
print(cnt)
num = 570
num %= 100  # num=num%100
print(num)

#############################
# 10~99 사이의 정수 입력: 55
# 십자리: 5
# 일자리: 5
#############################
number = int(input('10~99 사이의 정수 입력:'))
unit_10 = number // 10
unit_1 = number % 10
print('십자리:', unit_10)
print('일자리:', unit_1)


# # 관계 연산자
# # == : 같다, != : 같지 않다
print(5 == 5)
print(5 != 6)
# 입력받은 숫자가 짝수인지 확인
number = int(input('enter a number: '))
print(number % 2 == 0)

# 논리 연산자
# and, or,not
kor_score = int(input('국어 점수 입력: '))
eng_score = int(input('영어 점수 입력: '))
mat_score = int(input('수학 점수 입력: '))
print(kor_score >= 95 and eng_score >= 95 and mat_score >= 95)

##################################
# 윤년 체크 프로그램
##################################
year = int(input('판별할 연도 입력: '))
leafyear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(f'{year}년은 {leafyear}')
