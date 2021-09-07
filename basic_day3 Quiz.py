# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남는 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예) 생성된 비빌번호 : nav51!
site = "http://naver.com"
site = site[7:] # site.replace("http://","") # 규칙1
site = site[:site.index(".")] # 규칙2
print("생성된 비밀번호 : " + str(site[:3]) + str(len(site)) + str(site.count("e")) + "!")
password = str(site[:3]) + str(len(site)) + str(site.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(site,password))