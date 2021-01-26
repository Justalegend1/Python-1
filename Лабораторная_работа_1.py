while True:
    number = (input("Выберите номер задания: "))
    if not number.isnumeric():
        print ("Введите целое число")
    else:
        number = int(number)
        if ((number>3) or (number<=0)):
            print ("Ты не шути так, я человек нервный, а лучше выбери задание от 1 до 3")
        else:
            break
if (number == 1):
    x = float(input('Введите х: '))
    if (x>0):
        y = 2*x - 10
    if (x==0):
        y = 0
    if (x<0):
        y = 2*abs(x) - 1
    print ("y = ", y)
if (number == 2):
    while True:
        N = (input('Введите кол-во цифр/чисел: '))
        if not N.isnumeric():
            print("Мне кажется, ты что-то перепутал")
        else:
            N=int(N)
            break
    k = 0
    while (N>0):
        N-=1
        while True:
            a = input("Введите значение: ")
            if not a.isnumeric():
                print ("Вы ввели не целое число, попробуйте снова...")
            else:
                a=int(a)
                break
        if (a == 0):
            k+=1
    print ("Кол-во нулей в введенной последовательности равно: ", k)
if (number == 3):
    n = 0.0
    print("Сколько точек вы собираетесь вводить?")
    while True:
        toch = input()
        if not toch.isnumeric():
            print ("Введите целое число")
        else:
            toch = (float)(toch)
            break
    t = toch
    while (toch>0):
        toch-=1
        while True:
            print ("Введите координату х")
            x = input()
            try:
                x = float(x)
                break
            except:
                print("Введите число")
        while True:
            print ("Введите координату у")
            y = input()
            try:
                y = float(y)
                break
            except:
                print("Введите число")
                
        if ((x>=0) and (x<=8) and (y>=0) and (y<=8)):
            n+=1
    s = (float)((n*64.0)/t)
    print ("Площадь фигуры равна: ", s)


