from jug import TaskGenerator
# Yo utilice Jug, que es una herramienta que usa programación distribuida para realizar los task.
#Para mas información: https://jug.readthedocs.io/en/latest/tutorial.html#

print('\n -------------------------- Empieza el programa -------------------------- \n')

def MergeSort(file):

    print("Splitting ==>",file,"<==")
    if len(file)>1:
        mid = len(file)//2
        lefthalf = file[:mid]
        righthalf = file[mid:]

        MergeSort(lefthalf)
        MergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                file[k]=lefthalf[i]
                i=i+1
            else:
                file[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            file[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            file[k]=righthalf[j]
            j=j+1
            k=k+1

    print("Merging ==>",file,"<==")

    return file


@TaskGenerator
def escribirArchivo(archivo):
    file = open(archivo, "r")
    cont = file.readlines()
    resultado = MergeSort(cont)
    print('\n -------------------------- Fin del Merge y DP del documento -------------------------- \n')
    print('\n -------------------------- Empieza el guardado del documento -------------------------- \n')
    file2 = open("save.txt", "w")           #Nombre del archivo para salvar
    for line in resultado:
        file2.write(line)

escribirArchivo("file.txt")     #Nombre del archivo para cargar

#Para ejecutar el programa se debe de correr primero normalmente, y luego ingresar en la terminal las siguientes instrucciones:
#jug status file.py (file siendo el nombre del archivo de python)
#jug execute file.py (file siendo el nombre del archivo de python)