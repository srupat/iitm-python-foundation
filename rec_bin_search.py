#binary search recursion way
def rbinarysearch(L,k,begin,end):
    #this will recursively compute binary search
    if (begin==end):
        if (L(begin)==k):
            return 1
        else:
            return 0
    #if begin and end are consecutive    
    if (end-begin==1):
        if (L[begin]==k) or (L[end]==k):
            return 1
        else:
            return 0

    if (end-begin>1):
        mid=(begin+end)//2
        if (L[mid]==k):
            return 1
        if (L[mid]>k):
            #discard right,retain left
            end=mid-1
        if (L[mid]<k):
            #discard left,retain right
            begin=mid+1     
    if (end-begin<0):
        return 0
    return rbinarysearch(L,k,begin,end)        

print(rbinarysearch([1,7,32,95,108],95,0,4))