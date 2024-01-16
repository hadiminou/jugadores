from collections import namedtuple, defaultdict
from datetime import datetime, date, time
from typing import*
import csv

Jugador = namedtuple('Jugador', 'ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act,\
 senior, resultados')

def booleano(cadena:str)->bool:
    res = None
    if cadena.upper() == "S":
        res = True
    elif cadena.upper() == "N":
        res = False
    return res

def parser(cadena:str)->list[int]:
    return [int(punto.strip()) for punto in cadena.split(",")]

def lee_jugadores(fichero:str)->list[Jugador]:
    res = []
    with open(fichero, 'rt', encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act, senior, resultados in lector:
            fecha_ncto = datetime.strptime(fecha_ncto, "%d/%m/%Y").date()
            handicap = float(handicap)
            fec_hor_act = datetime.strptime(fec_hor_act, "%d/%m/%Y %H:%M:%S")
            senior = booleano(senior)
            resultados = parser(resultados)
            res.append(Jugador(ape_nom, licencia, fecha_ncto, federacion, handicap, fec_hor_act,\
                senior, resultados))
        return res

def mejores_jugadores(jugadores:list[Jugador], ano:int, n:int)->list[str, str, float]:
    return sorted([(i.licencia, i.ape_nom, i.handicap) for i in jugadores if i.fecha_ncto.year == ano],\
         key = lambda e:e[2])[:n]

def jugadores_por_golpes(jugadores:list[Jugador])->list[tuple[int, set]]:
    aux = defaultdict(set)
    res = []
    for i in jugadores:
        for j in i.resultados:
            aux[j].add(i.licencia)
    res = sorted(aux.items(), key = lambda e:e[0], reverse = True)
    return res

def promedio_ultimos_resultados(jugadores:list[Jugador], f1:date=None, f2:date=None)->list[tuple[str, float]]:
    aux = defaultdict(list)
    for i in jugadores:
        if (f1 == None or i.fec_hor_act.date() >= f1) and (f2 == None or i.fec_hor_act.date() <= f2) \
            and i.senior:
            for j in i.resultados:
                aux[i.licencia].append(j)
    return [(c, sum(v) / len(v)) for c,v in aux.items()]

def jugador_menor_handicap_por_federacion(jugadores:list[Jugador])->dict[str, tuple[str, float]]:
    aux = defaultdict(list)
    for i in jugadores:
        aux[i.federacion].append((i.ape_nom, i.handicap))
    return [(c, min(v, key = lambda e:e[1])) for c,v in aux.items()]

def comparativa_de_mejores_resultados_segun_handicap(jugadores:list[Jugador])->list[tuple[float, float, float]]:
    aux = defaultdict(list)
    aux2 = defaultdict(float)
    lista = []
    for i in jugadores:
        aux[i.handicap].append(min(i.resultados))
    aux2 = {c: sum(v) / len(v) for c,v in aux.items()}
    lista = sorted(aux2.items(), key = lambda e:e[0])
    return [(f"{tupla1[0]} vs {tupla2[0]}", tupla1[1] - tupla2[1]) for tupla1, tupla2 in zip(lista, lista[1:])]