unsorted_array = [5,10,15,32,55,21,40,2,3,76,89,28,9,7]

def QuickSort(unsorted_array):
   QuickSortBrain(unsorted_array,0,len(unsorted_array)-1)

def QuickSortBrain(unsorted_array,first,last):
   if first<last:

       splitpoint = partition(unsorted_array,first,last)

       QuickSortBrain(unsorted_array,first,splitpoint-1)
       QuickSortBrain(unsorted_array,splitpoint+1,last)


def partition(unsorted_array,first,last):
   pivotvalue = unsorted_array[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and unsorted_array[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while unsorted_array[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = unsorted_array[leftmark]
           unsorted_array[leftmark] = unsorted_array[rightmark]
           unsorted_array[rightmark] = temp

   temp = unsorted_array[first]
   unsorted_array[first] = unsorted_array[rightmark]
   unsorted_array[rightmark] = temp


   return rightmark

QuickSort(unsorted_array)
print(unsorted_array)
