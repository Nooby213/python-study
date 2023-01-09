#리스트 []
#지하철 칸별로 10명 20명 30명
#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = ["유재석","콩순","이승민"]
print(subway)

#x가 몇 번째 칸에 타고 있는가
print(subway.index("이승민")+1)

#정민이가 탔다
subway.append("정민")
print(subway)

#엄마를 유재석과 콩순이 사이에
subway.insert(1,"엄마")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
'''print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)'''
'''subway.append("엄마")
print(subway)
print(subway.count("엄마"))
print(subway.index("엄마"))'''
#정령
num_list = [5,7,2,6,1,9]
num_list.sort()
print(num_list)
#뒤집기
num_list.reverse()
print(num_list)
#num_list.clear()
#print(num_list)
mil=["고무마",1, True]
print(num_list)
