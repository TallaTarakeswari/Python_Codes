#chatgpt and best approch

arr = [0,1,0,3,12]

write =0

for read in range(len(arr)):
  if arr[read]!=0:
    arr[read],arr[write]=arr[write],arr[read]
    write+=1 
print(arr)




#My approch missed handling arr[left]!=0

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


  
  
