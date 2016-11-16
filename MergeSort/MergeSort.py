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
        # i is used to keep track of the number of elements added to the 
        # sorted alist from leftlist while j keeps track of the elements add
        # from rightlist on each iteration
        # k keeps tracks the total number of elements added after each iteration
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

def main():
    file = open('IntegerArray.txt')
    alist = [int(line) for line in file]
    return mergeSort(alist)

    
if __name__ == '__main__':
    print(main())
    print(inversions)

