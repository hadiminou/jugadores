from jugadores import*

def muestra_iterable(iterable):
    for elem in iterable:
        print(elem)

def test_lee_jugadores(datos:list[Jugador]):
    print("\n1.test_lee_jugadores")
    print(f"registros leidos: {len(datos)}")
    print(f"los dos primeros: ")
    muestra_iterable(datos[:2])

def test_mejores_jugadores(datos:list[Jugador]):
    print("\n2.test_mejores_jugadores")
    ano = 1969
    n = 4
    print(f"los {n} mejores jugadores nacidos en el {ano} son: {mejores_jugadores(datos, ano, n)}")

def test_jugadores_por_golpes(datos:list[Jugador]):
    print("\n3.test_jugadores_por_golpes")
    muestra_iterable(jugadores_por_golpes(datos))

def test_promedio_ultimos_resultados(datos:list[Jugador]):
    print("\n4.test_promedio_ultimos_resultados")
    f1 = datetime.strptime("1/3/2020", "%d/%m/%Y").date()
    f2 = datetime.strptime("31/5/2020", "%d/%m/%Y").date()
    muestra_iterable(promedio_ultimos_resultados(datos, f1, f2))

def test_jugador_menor_handicap_por_federacion(datos:list[Jugador]):
    print("\n5.test_jugador_menor_handicap_por_federacion")
    muestra_iterable(jugador_menor_handicap_por_federacion(datos))

def test_comparativa_de_mejores_resultados_segun_handicap(datos:list[Jugador]):
    print("\n6.test_comparativa_de_mejores_resultados_segun_handicap")
    print(comparativa_de_mejores_resultados_segun_handicap(datos))

if __name__ == "__main__":
    datos = lee_jugadores("data\Datos para el ejercicio de Python")
    test_lee_jugadores(datos)
    test_mejores_jugadores(datos)
    test_jugadores_por_golpes(datos)
    test_promedio_ultimos_resultados(datos)
    test_jugador_menor_handicap_por_federacion(datos)
    test_comparativa_de_mejores_resultados_segun_handicap(datos)