arr=list(map(int,input().split()))
head=int(input())
prev=head
dir=input()
max1=max(arr)
min1=min(arr)
right=[]
left=[]
for i in arr:
    if i>head:
        right.append(i)
    else:
        left.append(i)
sum=0
left.sort(reverse=True)
right.sort()

if dir=='left':
    sum+=head-0
    sum+=max1-0
    print([head]+left+right)

elif dir=='right':
    sum+=199-head
    sum+=199-min1
    print([head]+right+left)
print(sum)

