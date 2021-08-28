n=int(input("enter number of processes "))
p=list(map(str,input().split()))
bt=list(map(int,input().split()))
at=list(map(int,input().split()))
value=0
gt=[]
ct=[0]*n
wt=[0]*n
tat=[0]*n
for i in range(n):
    x=at.index(min(at))
    if at[x]>value:
        value=at[x]
    gt.append(p[x])
    ct[x]=value+bt[x]
    tat[x]=ct[x]-at[x]
    wt[x]=tat[x]-bt[x]
    value+=bt[x]
    at[x]=99999

print("completion time ",ct)
print("turn around time ",tat)
print("waiting time ",wt)
print("gant chart ",gt)
print("avg tat ",round(sum(tat)/n,3))
print("avg bt ",(round(sum(bt)/n,3)))
print("avg wt ",round(sum(wt)/n,3))



'''
3
p1 p2 p3
5 9 6 
0 3 6

'''

'''
5
p1 p2 p3 p4 p5
4 3 2 1 3 
3 5 0 5 4 

'''