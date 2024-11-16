
first=input("введите число ")
second=input("введите число ")
third=input("введите число ")

if first==second and second==third:  # проверка равенства всех
    print(3)
elif first == second or second==third or third == first: # проверка равенства двух
    print(2)
else:                   # равных нет
    print(0)
    