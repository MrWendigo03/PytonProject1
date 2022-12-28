from __init__ import dlina, tipe1

def ploshad_i_perimetr(chislo):
    ploshad = (3 ** 0.5 * chislo ** 2) / 4
    perimetr = chislo * 3
    print("Площадь треугольника:", ploshad, "Периметр треуголника:", perimetr)
    return ploshad, perimetr
