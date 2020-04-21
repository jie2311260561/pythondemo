import math
def bijiuliang():
    for r in range(1,21):
        for x in range(1,r):
            for y in range(1,x):
                for z in range(1,y):
                        # if r == x+y+2*z :
                            if  math.isclose((1/r +  1/ x + 1/y + 1/z) , 1.0,rel_tol=1e-5)  :
                                print("{},{},{},{},{}".format(r,x,y,z,z-z))

bijiuliang()

