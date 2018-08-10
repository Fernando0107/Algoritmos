
possible_heap= [16,14,10,8,7,9,3,2,4,1]

def heap(possible_heap):                                                                                                                #Running Time:
    for head in range(0, len(possible_heap)):                                                                                           #n
        c1 = head * 2 + 1
        c2 = head * 2 + 2
        if c1 < len(possible_heap) and possible_heap[head] < possible_heap[c1]: #Si el hijo izquierdo es mas grande, return false       #n
            return False                                                                                                                #n
        if c2 < len(possible_heap) and possible_heap[head] < possible_heap[c2]: #Si el hijo derecho es mas grande, return false         #n
            return False                                                                                                                #n
    return True                                                                                                                         #n

if heap(possible_heap)==True:
    print("El arreglo dado es un Heap")
else:
    print("El arreglo dado no es un Heap")

#Running time: O(n)


