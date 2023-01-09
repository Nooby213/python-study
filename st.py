# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = '파이선 어려워요'
# print(sentence2)
# sentence3 = """
# 뭐라는거야
# """
# print(sentence3)
#
# jumin = '940809-1106110'
# print('성별:'+jumin[7])
# print('연:'+jumin[0:2]) #0~2 직전까지
# print('월:'+jumin[2:4])
# print('일:'+jumin[4:6])
# print('생년월일:'+jumin[:6])
# print('뒷자리:'+jumin[7:])
# print('뒤에서:'+jumin[-7:])
python = 'Tellephon is Coming'
print(python.lower())
print(python[-6].isupper())
print(len(python))
print(python.replace('is','was'))
index=python.index('e')
print(index)
index=python.index('e', index+1)
print(index)
print(python.count('e'))
