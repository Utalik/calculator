a = int(input("Введите цифру:"))
znak = input("Введите знак +,-,*,**,/ :")
b = int(input("Введите цифру:"))
if znak == "+" or znak == "-" or znak == "*":
    print("================================")
    print("Ваш ответ:", (a + b) or (a - b) or (a * b))
    print("================================")
elif znak == "/":
    if b == 0:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("На ноль делить нельзя!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("================================")
        print("Ваш ответ:", (a / b))
        print("================================")
else:
    print("Неверная операция")