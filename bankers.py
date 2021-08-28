import numpy as np
n=int(input())
m=int(input())
p=list(map(str,input().split()))
alloc=np.array([list(map(int,input().split())) for i in range(n)])
max=np.array([list(map(int,input().split())) for i in range(n)])
avail=np.array(list(map(int,input().split())))

need=max-alloc
def compare(i):
    for j in range(m):
        if(need[i][j]>avail[j]):
            return False
    return True



flag=[0]*n
safe_seq=[]
for d in range(n):
    for i in range(n):
        if(flag[i]==0 and compare(i)):
            for j in range(m):
                avail[j]+=alloc[i][j]

            flag[i]=1
            safe_seq.append(p[i])


if(sum(flag)!=n):
    print("not safe sequence ")
else:
    print(safe_seq)
    print(need)


'''
5
3
p0 p1 p2 p3 p4
0 1 0
2 0 0
3 0 2
2 1 1
0 0 2
7 5 3
3 2 2
9 0 2
2 2 2
4 3 3
3 3 2

'''