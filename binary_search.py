def binary_search(L,k):
    #lets shrink the loop using while loop
    begin=0
    end=len(L)-1
    while(end-begin>1):
        #we will handle the case when the number of elements is less than or equal to 1
        mid=(begin+end)//2
        if L[mid]==k:
            return 1
        if (L[mid]>k):
            end = mid - 1
        if (L[mid]<k):
            begin = mid + 1
    if L[begin]==k or L[end]==k:
        return 1
    else:
        return 0
    
print(binary_search(list(range(100)),10))    