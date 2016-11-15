file = open('IntegerArray.txt', 'r')
alist = []
for i in file.readlines():
    alist.append(int(i))
inversions = 0

def mergeSort(alist):
    global inversions
    if len(alist)>1:
        mid = len(alist)//2
        leftlist = alist[:mid]
        rightlist = alist[mid:]
        #runs recursively on both sides to break them up into single elements
        mergeSort(leftlist)
        mergeSort(rightlist)
        

        
        i=0
        j=0
        k=0
        
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                alist[k] = leftlist[i]
                i += 1
            else:
                alist[k] = rightlist[j]
                j += 1
                inversions += len(leftlist) - i
            k += 1
            
        while i < len(leftlist):
            alist[k] = leftlist[i]
            i += 1
            k += 1
            
        while j < len(rightlist):
            alist[k] = rightlist[j]
            j += 1
            k += 1
    
    return alist
    
#alist = [1,5,3,2,6,4]
mergeSort(alist)
print(alist)
print(inversions)

