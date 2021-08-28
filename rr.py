n=int(input())
p=list(map(str,input().split()))
at=list(map(int,input().split()))
bt=list(map(int,input().split()))
tq=int(input())
val1=val2=i=flag=0
gc=[]
rq=[]
ct=[0]*n
wt=[0]*n
tat=[0]*n
rt=[0]*n
s=sum(bt)
at1=sorted(at)
bt1=bt.copy()
while(s!=max(ct)):
    while(i<len(at1) and val1>=at1[i]):
        rq.append(at1[i])
        i+=1
    if flag==1:
        rq.append(at[x])
    
    x=at.index(rq[0])
    
    if p[x] not in gc:
        rt[x]=val2-at[x]

    gc.append(p[x])
    rq.remove(at[x])

    if( bt[x]<=tq and bt[x]!=0):
        ct[x]=bt[x]+val1
        tat[x]=ct[x]-at[x]
        wt[x]=tat[x]-bt1[x]
        val1+=bt[x]
        val2+=bt[x]
        bt[x]=0
        flag=0

    else:
        bt[x]-=tq
        val1+=tq
        val2+=tq
        flag=1


print("completion time ",ct)
print("turn around time ",tat)
print("waiting time ",wt)
print("response time ",rt)

print("gant chart ",gc)
print("avg tat ",round(sum(tat)/n,3))
print("avg bt ",(round(sum(bt1)/n,3))) #optional
print("avg wt ",round(sum(wt)/n,3))


'''
4
p1 p2 p3 p4
0 1 2 3
5 4 2 1
2
----

4
p1 p2 p3 p4
0 1 2 3
10 4 5 3
3
'''
    