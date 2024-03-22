환율 = {"달러" : 1320, "엔" : 950, "위안" : 182}
print(환율)
money = [13, 200, 13]
print(money)

a = 환율["달러"] * money[0]
b = 환율["엔"] * money[1]
c = 환율["위안"] * money[2]
print(a+b+c)

d = "철수가 가지고 있는 원화의 가치는"
e = a + b + c
f = "원입니다."
print(d, e, f)



