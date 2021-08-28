arr=list(map(int,input().split()))
head=int(input())
prev=head
sum=0
for i in arr:
    if i>prev:
        sum+=i-prev
    elif i<prev:
        sum+=prev-i
    prev=i
    
print(sum)
print([head]+arr)