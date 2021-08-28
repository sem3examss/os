n=int(input())
p=list(map(str,input().split()))
bt=list(map(int,input().split()))
pri=list(map(int,input().split()))
qno=list(map(int,input().split()))
#qno=0 priority ,qno 1: sjf
hold=[]
ct=[0]*n
tat=[0]*n
wt=[0]*n
val=0
gt=[]
for i in range(n):
    x=pri.index(min(pri))
    if(qno[x]!=min(qno)):
        hold.append(x)
    else:
        gt.append(p[x])
        ct[x]=bt[x]+val
        tat[x]=ct[x]
        wt[x]=tat[x]-bt[x]
        val+=bt[x]
        bt[x]=99999

    pri[x]=99999
for x in range(len(hold)):
    i=bt.index(min(bt))

    gt.append(p[i])
    ct[i]=bt[i]+val
    tat[i]=ct[i]
    wt[i]=tat[i]-bt[i]
    val+=bt[i]
    bt[i]=99999



print("completion time ",ct)
print("turn around time ",tat)
print("waiting time ",wt)

print("gant chart ",gt)
print("avg tat ",round(sum(tat)/n,3))
# print("avg bt ",(round(sum(bt)/n,3))) #optional
print("avg wt ",round(sum(wt)/n,3))






# Burst time:     4 9 7 4 6 
# Priority:       2 1 2 1 1      
# Queue Priority: 1 1 2 2 1


# Burst time: 4 9 4 7 6 
# Priority: 2 1 2 1 1      
# Queue Priority: 1 1 2 2 1