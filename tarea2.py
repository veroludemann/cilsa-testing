#Resolución de la función Test para determinarTriangulo. 
#Definición arbitraria de la función “determinarTriangulo”: devuelve 1 si es isósceles, 2 si es escaleno y 3 si es equilátero.
#La función test devuelve 1 si está OK, devuelve 0 si ERROR.

#isosceles (dos lados iguales)ladoA == ladoB or a == ladoC or ladoB == ladoC
#escaleno (todos los lados distintos) ladoA != ladoB and ladoA != ladoC and ladoB != ladoC
#equilatero  (todos los lados iguales) ladoA == ladoB == ladoC




def determinarTriangulo(ladoA, ladoB, ladoC):
    if ladoA == ladoB and ladoB == ladoC:
        return 3  # Equilatero
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        return 1  # Isosceles
    else:
        return 2  # Escaleno

def test():
    ok = 1

    # Equilatero
    if determinarTriangulo(3, 3, 3) != 3:
        print("Error en caso equilátero")
        ok = 0

    # Isosceles
    if determinarTriangulo(4, 4, 2) != 1:
        print("Error en caso isosceles (4,4,2)")
        ok = 0

    if determinarTriangulo(2, 5, 5) != 1:
        print("Error en caso ispsceles (2,5,5)")
        ok = 0

    if determinarTriangulo(6, 3, 6) != 1:
        print("Error en caso isosceles (6,3,6)")
        ok = 0

    # Escaleno
    if determinarTriangulo(3, 4, 5) != 2:
        print("Error en caso escaleno")
        ok = 0

    if ok == 1:
        print("Todos los tests pasaron correctamente.")
    else:
        print("Hay errores en la función determinarTriangulo.")

    return ok


test()
