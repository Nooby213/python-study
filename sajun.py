# cabinet = {3:"lee", 7:"mom"}
# print(cabinet[7])
# print(cabinet.get(3))
# print(cabinet.get(6,"usable"))
# print(3 in cabinet)
# print(8 in cabinet)
cabinet = {"a-3":"com","a-0":"omo"}
print(cabinet.get("a-3"))
print(cabinet.get("a-7","usable"))

#new customer
print(cabinet)
cabinet["a-3"]="gonna"
cabinet["b-7"]="mmmoo"
print(cabinet)

#손님 갔다
del cabinet["b-7"]
print(cabinet)
#key 들만출력,value , 둘다
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
#문닫음
cabinet.clear()
print(cabinet)
