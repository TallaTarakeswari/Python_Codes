#Binary Search program that searches for a given key in a list, without changing the original indices. It also handles duplicate elements by returning the index of the first occurrence of the key.

def binary_search(a,n,low,high):
    if low>high:
        return -1
    
    mid=(high+low)//2
    
    if a[mid][0]==n:
        
        left_search=binary_search(a,n,low,mid-1)
        return a[mid][1] if left_search==-1 else left_search
    elif a[mid][0]>n:
        high=mid-1
        result= binary_search(a,n,low,high)
        return result
    else:
        low=mid+1
        result =binary_search(a,n,low,high)
        return result
        
def bine(arr,n):
    m=[(val,idx) for idx,val in enumerate(arr)]
    print(m)
    m.sort(key=lambda x: x[0])
    print(m)
    low=0
    high=len(m)-1
    
    return binary_search(m,n,low,high)
    
a=[4,6,9,3,0,8,22,1,2,2,2,1,2]
print(bine(a,1))
    
