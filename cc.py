# print('나는 %d살 입니다' %29)
# print('나는 %s하고 싶어요' %'연애')
# print('Com은 %c로 시작해요' %'c')
# print('나는 %s와 %s를 하고 싶어요' %('연애','공부'))

# #방법2
# print('나는 {}살입니다'.format(29))
# print('나는 {}와 {}를 하고 싶어요' .format('연애','공부'))
# print('나는 {1}와 {0}를 하고 싶어요' .format('연애','공부'))

# #방법3
# print('나는 {age}살이며, {color}색을 좋아해요'.format(age=29,color='노랑'))

#방법4(v3.6~)
# age=20
# color='노랑'
# print(f'나는 {age}살이며, {color}색을 좋아해요')

#\줄바꿈
# print('그래 그래 \n니말이 다 맞다')
# print("나는'나는'")
# print('나는"나는"')
# print("나는\"나\"")
# print('C:\\Bitnami\\wampstack-8.1.12-0\\apache2\\htdocs\\syntax>')
# print('red apple\rpine')
# print('redd\bapple')
# print('red\tapple')  +count[name]+(naver[0:3])

url = 'http://naver.com'
name = url.replace('http://','')
print(name)
name = name[:name.index('.')]
print(name)
password = name[:3] + str(len(name)) +str(name.count('e'))+'!'
print('{0}의 비밀번호는 {1}입니다.'.format(url, password))
#1:22:34
