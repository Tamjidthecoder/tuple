def palind(r):
    e = len(r) -1
    S = 0
    while(s<e):
    if(r[s]!=r[e]):
        return False
        S+=1
        e -= 1
        return True

r = (1,2,3,3,2,1)

if(palind(r)): 
    print("The Tuple is Flip-Flop")
else:  
    print("The Tuple is not Flip-Flop")