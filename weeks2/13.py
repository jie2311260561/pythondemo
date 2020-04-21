import numpy
def fact(n,*b):
    s=1
    for i in range(1,n+1):
        s *= i;
    for item in b:
        s *=item;
    return s

def mmmu(x,y,time):

    Zx = 0  
    Zy = y 
    
    for i in numpy.arange(1,time+1,0.5):
        if( i % 2 == 0):
            y *= 2 
        if( i % 3 == 0):
           Zx = x 
           x *= 2
           y = y - Zx
        if(i % 1 == 0):
            y = y - Zx
        if(y < 0):
            y=0
            break
    print('x剩余{}  y剩余{}'.format(x,y))
def reverse(num):
    ret=0
    while num:
        last=num%10
        ret=ret*10+last
        num//=10
    return ret
def keys():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for h in range(10):
                        if(i != j and i!=k  and i!= l and i!= h and j!= k and k!= l and l!= h):
                            x = i*10000+j*1000+k*100+l*10+h
                            y = h*10000+l*1000+k*100+j*10+i
                            if(x==y):
                                print('{}{}{}{}{}'.format(i,j,k,l,h))

            # s = reverse(i)
            # if(i * j == s):
            #     print('{} * {} = {}'.format(i,j,s))
                
        
            
global x  

   

if __name__ == '__main__':
    keys()
    # x = 10 
    # y = str(x)
    # z = y[::-1]
    # print(z)
    # z = eval(y) 
    # print('{}'.format(z))
     # mmmu(10,90,60)
    # x=3
    # x *=2
    # print('{}'.format(x))
    # for i in range(Cx):
    #     x *= 2
    #     Zx = x
    #     y = y - x
    # for i in range(Cy):
    #     y *=2;
    #     Zy = y;

