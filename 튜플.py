menu = ("돈가스","치즈가스")
print(menu[0])
print(menu[1])

# name="이승민"
# age=30
# hobby="loa"
# print(name,age,hobby)

(name,age,hobby)=("이승민",30,"로아")
print(name,age,hobby)

#집합 set 중복 안됨 순서없음
myset={1,2,3,4,4,4}
print(myset)
java={"돌고래","달팽이","콧구멍"}
un={"돌고래","엉덩이"}

#교집합
print(java&un)
print(java.intersection(un))

#합집합
print(java|un)
print(java.union(un))

#차집합
print(java-un)
print(java.difference(un))

#un 할 수 있는사람이 늘어남
un.add("콧구멍")
print(un)

#빼기
java.remove("달팽이")
print(java)
