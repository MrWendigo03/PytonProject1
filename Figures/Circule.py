from __init__ import dlina, type2

def ploshad_i_perimetr(chislo):
    ploshad = 3.14 * chislo ** 2
    perimetr = 2 * chislo * 3.14
    print("Площадь круга:", ploshad, "Длина окружности:", perimetr)
    return ploshad, perimetr
