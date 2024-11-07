y=(11,)
print(y)
print(type(y))
# 
nes=(1,2,(3,4),('a','b'))
print(nes)
#
def g():
    x=10
    y=20
    return x,y
coordinates=g()
print(coordinates)
x,y=g()
print("x:{x},y:{y}")