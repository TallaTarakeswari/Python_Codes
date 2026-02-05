arr=[3,5,2,4,9,62,63]
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if arr[j]<arr[j+1]:
            k=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=k
print(arr)
