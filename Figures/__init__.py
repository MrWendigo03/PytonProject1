def funkciyavvoda(dlina, type):

    return dlina

type = input("Введите тип фигуры: "
             "\ntriangle: \tТреугольник"
             "\ncircle: \tКруг"
             "\nsquire: \tКвадрат\n")
if type == "triangle":
    tipe1 = type
elif type == "circle":
    type2 = type
elif type == "squire":
    type3 = type
else:
    print("Такого типа нет!!!")
dlina = int(input("Введите длину стороны правильной фигуры: "))
funkciyavvoda(dlina)