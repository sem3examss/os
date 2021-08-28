n=int(input())
p=list(map(str,input().split()))
pri=list(map(int,input().split()))
at=list(map(int,input().split()))
bt=list(map(int,input().split()))
ct=[0]*n
wt=[0]*n
tat=[0]*n
val=0
flag=0
gc=[]
x=at.index(min(at))
for i in range(n):
    if at[x]>val:
        x1=x
        x2=min(pri)
        pri[x1]=99999
        flag=1
        x=pri.index(min(pri))

    gc.append(p[x])
    ct[x]=bt[x]+val
    tat[x]=ct[x]-at[x]
    wt[x]=ct[x]-bt[x]
    val+=bt[x]
    at[x]=99999
    pri[x]=99999
    x=pri.index(min(pri))
    if flag==1:
        flag=0
        x=x1
        pri[x1]=x2






print("completion time ",ct)
print("turn around time ",tat)
print("waiting time ",wt)

print("gant chart ",gc)
print("avg tat ",round(sum(tat)/n,3))
print("avg bt ",(round(sum(bt)/n,3))) #optional
print("avg wt ",round(sum(wt)/n,3))

'''
5
p1 p2 p3 p4 p5
2 0 3 1 4
0 5 12 2 9
11 28 2 10 16

'''
# 7
# process p1 p2 p3 p4 p5 p6 p7
# 3 4 4 5 2 6 1
# 0 1 3 4 5 6 10
# 8 2 4 1 6 5 1