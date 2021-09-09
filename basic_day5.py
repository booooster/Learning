# if

weather = input("오늘 날씨는 어때요? ")
# if 조건 :
#     실행 명령문
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지" :
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 외출을 삼가하세요")
elif 10 <= temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 외출을 삼가하세요")

# for
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for waiting_no in range(1,6):
    print("대기번호 : {}".format(waiting_no))

hero = ["아이언맨", "토르", "그루트"]
for calling in hero:
    print("{}, 에게서 전화가왔습니다.".format(calling))

# while
customer = "토르"
index = 5
while index >= 1: #while 뒤의 조건이 False가 될때까지 반복, 무한루프가 될 수도 있음
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

# countinue와 break
absent = [2, 5]
no_book = [8]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}번은 교무실로 따라와!".format(student))
        break
    print("{0}번 책을 읽어봐".format(student))

# 한 줄 for문
# 출선번호가 1 2 3 4, 앞에 100을 붙이기로 함
students = list(range(1,6))
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "Black Widow"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Black Widow"]
students = [i.upper() for i in students]
print(students)