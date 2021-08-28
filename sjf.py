# n=int(input())
# p=list(map(str,input().split()))
# at=list(map(int,input().split()))
# bt=list(map(int,input().split()))
# ct=[0]*n
# wt=[0]*n
# tat=[0]*n
# value=0
# bt1=bt.copy() #for avg bt
# gt=[]

# for i in range(n):
#     x=bt.index(min(bt))
#     if(at[x]>value):
#         x=at.index(min(at))

#     gt.append(p[i])
#     ct[x]=value+bt[x]
#     tat[x]=ct[x]-at[x]
#     wt[x]=ct[x]-bt[x]
    

#     value+=bt[x]
#     bt[x]=99999
#     # at[x]=99999
    


# print("completion time ",ct)
# print("turn around time ",tat)
# print("waiting time ",wt)
# print("gant chart ",gt)
# print("avg tat ",round(sum(tat)/n,3))
# print("avg bt ",(round(sum(bt1)/n,3))) #optional
# print("avg wt ",round(sum(wt)/n,3))




# # 5
# # process p1 p2 p3 p4 p5
# # 2 1 4 0 2
# # 1 5 1 6 3

# '''
# 5
# p1 p2 p3 p4 p5
# 2 1 4 0 2
# 1 5 1 6 3
# '''
n = int(input("Enter no. of process: "))
process = list(map(str, input("Process: ").split()))
At = list(map(int, input("Arrival time:").split()))
Bt = list(map(int, input("Burst time: ").split()))
gc = []
ct = [0]*n
wt = [0]*n
tat = [0]*n
rt = [0]*n
val = 0
x = At.index(min(At))
for i in range(n):

    if At[x]>val:
         x = At.index(min(At))
         
    gc = gc + [(process[x])]
    ct[x] = val + Bt[x]
    tat[x] = ct[x]-At[x]
    wt[x] = tat[x]-Bt[x]
    rt[x] = val-At[x]       
    val += Bt[x]
    Bt[x]=99999 
    x = Bt.index(min(Bt))
    
print("Processes       :", process)
print("Completion time :",ct)
print("Turn Around time:",tat)
print("Waiting time    :",wt)
print("Response time   :",rt)
print("Gantt Chart     :",gc)
print("Avg Turn Around Time:", round(sum(tat)/n,3))
print("Avg Wating Time     :", round(sum(wt)/n,3))


''''
4
Process: p1 p2 p3 p4
Arrival time:2 0 4 5
Burst time: 3 4 2 4


4
Process: p1 p2 p3 p4
Arrival time:0 2 4 5
Burst time: 7 4 1 4

'''