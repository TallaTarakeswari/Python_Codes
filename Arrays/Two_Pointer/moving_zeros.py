#My approch

arr = [0,1,0,3,12]

left=0
right=0
while right<len(arr):
  if arr[left]==0 and arr[right]!=0:
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp
    right +=1 
    left +=1 
  elif arr[left]==0 and arr[right]==0:
    right +=1
  print(arr)
  
  
