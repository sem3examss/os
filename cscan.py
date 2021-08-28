arr=list(map(int,input().split()))
head=int(input())
prev=head
dir=input()
right=[]
left=[]
for i in arr:
    if i>head:
        right.append(i)
    else:
        left.append(i)

sum=199
if dir=='right':
    sum+=199-head
    sum+=max(left)-0
    right.sort()
    left.sort()
    print([head]+right+left)

if dir=='left':
    sum+=head-0
    sum+=199-min(right)
    right.sort(reverse=True)
    left.sort(reverse=True)
    print([head]+left+right)
print(sum)