import math

website_page_ranks=[3,39,61,91,57,22,75,89,9,90,63,78,28,73,20]
count =0
def Merge(A,p,q,r):
   global counter
   counter+=1
   n1=q-p+1
   n2=r-q
   Le = [0]*(n1+1)
   Ri = [0]*(n1+1)

   for i in range (0,n1):
       Le[i]=A[p+i]

   for j in range (0,n2):
       Ri[j]=A[q+j+1]

   Le[n1]=100 #Centinela
   Ri[n2]=100#Centinela
   i=0
   j=0
   for k in range(p,r+1):
       if Le[i] <= Ri[j]:
           A[k]=Le[i]
           i=i+1
       else:
           A[k] = Ri[j]
           j=j+1
   return A
counter=0

def MergeSort(A,p,r):
   global counter2
   counter2+=1
   if p<r:
       q=math.floor((p+r)/2)
       MergeSort(A,p,q)
       MergeSort(A,q+1,r)
       Merge(A,p,q,r)
counter2=0

def Mergesort(A):
   global counter3
   counter3+=1
   MergeSort(A,0,len(A)-1)
   A.reverse()
   return A
counter3=0

print("MergeSort website page ranks:{}".format(Mergesort(website_page_ranks)))

print("Numero de veces que se hizo recurción Merge: ", counter)
print("Numero de veces que se hizo recurción MergeSort: ", counter2)
print("Numero de veces que se hizo recurción Mergesort: ", counter3)
print("Total de numero de veces que se itero el programa: ",counter+counter2+counter3)

# Resultado: MergeSort website page ranks:[91, 90, 89, 78, 75, 73, 63, 61, 57, 39, 28, 22, 20, 9, 3]
