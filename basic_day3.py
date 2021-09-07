# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전까지 (0,1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
print("뒤 7자리 : " + jumin[7:]) # 7번째 부터 끝까지
print("뒤 7자리 (뒤에서 부터): " + jumin[-7:]) # 맨 뒤에서 7번째 부터 끝까지

# 문장열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 모두 소문자로 출력
print(python.upper()) # 모두 대문자로 출력
print(python[0].isupper()) # 해당 번째의 문자가 대문자인지?
print(len(python)) # 문자열의 길이 출력
print(python.replace("Python", "Java"))

index = python.index("n")
print(index) # 괄호안의 문자가 문자열의 몇번째에 있는지 출력
index = python.index("n", index + 1)
print(index) # 앞에 찾은 문자 이후에 나오는 같은 문자가 문자열의 몇번째에 있는지 출력

print(python.find("Java")) # 괄호안의 문자가 문자열에 없을 시 -1을 출력 다음코드 또한 계속 진행
# print(python.index("Java")) 
# find와는 달리 괄호안의 문자가 문자열에 없을시 에러가 발생하며 실행종료 다음 코드는 실행 안된 체로 멈춤

print(python.count("n")) # 괄호안의 문자가 문자열에서 몇번나오는지 출력

# 문자열 포맷

# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살 입니다." % 20) # %d 정수
print("나는 %s를 좋아해요." % "파이썬") # %s 정수, 문자열, 문자 상관없이 출력
print("Apple은 %c로 시작해요" % "A") # %c 문자 

# %s
print("나는 %s살입니다" % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4
age = 20
color = "삘긴"
print(f"나는 {age}살이며, {color}색을 좋아해요.") 

# 탈출문자

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\\IDEAPAD\\Desktop\\coding\\python>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

#\b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")