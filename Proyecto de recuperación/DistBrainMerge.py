from jug import TaskGenerator
import math

"""Yo utilice Jug, que es una herramienta que usa programación distribuida para realizar los task.
#Para mas información: https://jug.readthedocs.io/en/latest/tutorial.html

Pueden agarrar mi archivo y solo actualiza la data para que se ordenada, o bien, ustedes crear un archivo y corrrerlo,
abajo se encuentra la función que lo lee y guarda el archivo."""

print('\n -------------------------- Empieza el programa -------------------------- \n')

@TaskGenerator                              #Al ejecutarlo con Jug, da conflicto, al igual con la otra función de implemtación de Merge Sort.
def Merge_AllSpark(lefthalf, righthalf):

    rh = 0
    lh = 0
    AllSpark = []

    while lh < len(lefthalf) and rh < len(righthalf):
        if lefthalf[lh] < righthalf[rh]:
            AllSpark.append(lefthalf[lh])
            lh += 1
        else:
            AllSpark.append(righthalf[rh])
            rh += 1

    AllSpark += lefthalf[lh:]
    AllSpark += righthalf[rh:]
    return AllSpark

@TaskGenerator
def Merge_Brain(matrix):

    if len(matrix) <= 1:
        return matrix

    half = len(matrix) // 2
    left = Merge_Brain(matrix[:half])
    right = Merge_Brain(matrix[half:])
    return Merge_AllSpark(left, right)

@TaskGenerator                                          #Con este Task Generator si funciona.
def File_Prime(file):
    file = open(file, "r")
    cont = file.readlines()
    brain = Merge_Brain(cont)
    print('\n -------------------------- Fin del Merge y DP del documento -------------------------- \n')
    print('\n -------------------------- Empieza el guardado del documento -------------------------- \n')
    file2 = open("saves.txt", "w")  # Nombre del archivo para salvar
    for line in brain:
        file2.write(line)

"""Para ejecutar el programa se debe de correr primero normalmente, y luego ingresar en la terminal las siguientes instrucciones:
#jug status file.py (file siendo el nombre del archivo de python)
#jug execute file.py (file siendo el nombre del archivo de python)"""

#Es importante que tengan los archivos en la misma carpeta en donde se encuentra ej ejecutable del pro
