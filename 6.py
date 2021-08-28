def firstfit(p,req,blocks):
    frag=blocks.copy()

    print("process\t required \t block size\t block num\t remaining ")
    for i in range(len(p)):
        flag=0
        for j in range(len(blocks)):
            if(req[i]<=blocks[j]):
                print(p[i],"\t\t",req[i],"\t\t",blocks[j],"\t\t",j+1,"\t\t",blocks[j]-req[i])
                frag[j]=blocks[j]-req[i]
                blocks[j]-=req[i]
                flag=1
                break
        if(flag==0):
            print(p[i],"not allocated")


    print("fragmentation is",frag)

def bestfit(p,req,blocks):
    for i in range(len(p)):
        for k in range(len(blocks)):
            li=[]
            for j in range(len(blocks)):
                if(req[i]<=blocks[j]):
                    li.append([blocks[j],j])
            if li==[]:
                print("process ",p[i]," cant be allocated")
                break 
            li.sort()
            print(p[i],li[0][0],li[0][1])   
            blocks[li[0][1]]=0
            break 
# def worstfit(p,req,blocks):
#     for i in range(len(p)):
#         for k in range(len(blocks)):
#             li=[]
#             for j in range(len(blocks)):
#                 if(req[i]<=blocks[j]):
#                     li.append([blocks[j],j])
#             if li==[]:
#                 print("process ",p[i]," cant be allocated")
#                 return 
#             li.sort()
#             print(p[i],li[len(li)-1][0],li[len(li)-1][1])   
#             blocks[li[len(li)-1][1]]=0
#             break 



def worstfit(p,req,blocks):
    for i in range(len(p)):
        for k in range(len(blocks)):
            li=[]
            for j in range(len(blocks)):
                if(req[i]<=blocks[j]):
                    li.append([blocks[j],j])
            if li==[]:
                print("process ",p[i]," cant be allocated")
                break 
            li.sort(reverse=True)
            print(p[i],li[0][0],li[0][1])   
            blocks[li[0][1]]=0
            break 



p=list(map(str,input('process ids ').split()))
req=list(map(int,input('required sizes for processes').split()))

blocks=list(map(int,input('available block sizes ').split()))
print("1-first fit\n2-best fit \n3.worst fit")

ch=int(input())
if(ch==1):
    firstfit(p,req,blocks)
elif ch==2:
    bestfit(p,req,blocks)
elif ch==3:
    worstfit(p,req,blocks)





'''
p1 p2 p3 p4 p5
3 1 4 5 7 
1 6 8 3 4 9
'''