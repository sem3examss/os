n=int(input('buff size '))

mutex=1
empty=n
full=0
x=0
def wait(s):
    s-=1
    return s
def signal(s):
    s+=1
    return s

def producer():
    global mutex,empty,full,n,x
    mutex=wait(mutex)
    empty=wait(empty)
    x+=1
    print("producer produced item ",x)
    full=signal(full)
    mutex=signal(mutex)

def consumer():
    global mutex,empty,full,n,x
    mutex=wait(mutex)
    full=wait(full)
    
    print("consumer consumed item ",x)
    x-=1
    empty=signal(empty)
    mutex=signal(mutex)  
    






ch=int(input())
while ch:
    if ch==1:
        if(mutex==1 and empty!=0):
            producer()
        else:
            print("buffer is full cant produce ")

    elif ch==2:
        if( mutex==1 and full!=0):
            consumer()
        else:
            print("consumer cant consume , bufer is empty ")
    else:
        print("enter proper choice ")

    ch=int(input())
