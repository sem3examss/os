mem=int(input())
blocksize=int(input())
blocks=int(input())
processes=int(input())
req1=[]
for i in range(processes):
    req1.append(int(input('memory required by processes ')))
i=0
j=0
int_frag=0
ext_frag=0
while (i<blocks and j<processes):
    if req1[j]<=blocksize:
        int_frag+=blocksize-req1[j]
        print(i+1,"\t",req1[j],"\t",blocksize-req1[j])
        

    else:
        print(i+1,"\t",req1[j],"\tno")
    i+=1
    j+=1
    
print(int_frag)
print(mem-(blocks*blocksize))


'''
1000
300
3
5
275
400
290
293
100

'''