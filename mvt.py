mem=int(input())
req=list(map(int,input().split()))
sum=0
for i in range(len(req)):
    sum+=req[i]
    if sum>mem:
        sum-=req[i]
        print("cant fit")

    else:
        print(i,req[i])

    if sum>=mem:
        print("mem completed ")
        break

print(sum)
print(mem-sum)