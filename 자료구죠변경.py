#자료구죠변경.py
# menu={"app","pep","cider"}
# print(menu,type(menu))
#
# menu=list(menu)
# print(menu,type(menu))
#
# menu=tuple(menu)
# print(menu,type(menu))
#
# menu=set(menu)
# print(menu,type(menu))

print('--당첨자발표--')
from random import *
lst=list(range(1,21))
# print(type(lst))
shuffle(lst)
당첨자=sample(lst,4)
# print(당첨자)
치킨당첨자=당첨자[0]
print('치킨당첨자:'+str(치킨당첨자))
커피당첨자=당첨자[1:]
print('커피당첨자:'+str(커피당첨자))
print('--축하포카--')

print("--당첨자발표--")
print("치킨당첨자: {0}".format(당첨자[0]))
print("커피당첨자: {0}".format(당첨자[1:]))
print('--축하포카--')
