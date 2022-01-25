'''
Consider a game, in which you have two types of powers, A and B and there are 3 types of Areas X, Y and Z.
Every second you have to switch between these areas, each area has specific properties by which your power A and power B increase or decrease.
We need to keep choosing areas in such a way that our survival time is maximized.
Survival time ends when any of the powers, A or B reaches less than 0.

Initial value of Power A = 20
Initial value of Power B = 8

Area X (3, 2) : If you step into Area X,
                A increases by 3,
                B increases by 2

Area Y (-5, -10) : If you step into Area Y,
                   A decreases by 5,
                   B decreases by 10

Area Z (-20, 5) : If you step into Area Z,
                  A decreases by 20,
                  B increases by 5

It is possible to choose any area in our first step.
We can survive at max 5 unit of time by following
these choice of areas :
X -> Z -> X -> Y -> X
'''

def findMaxSurvivalTime(a,b,x,y,z,currArea, memory = {}):
    if(a <=0 or b<=0):
        return 0
    key = str(a) + "-" + str(b)
    if(key in memory):
        return memory[key]
    if(currArea == 'x'):
        tmp = 1+ max(
            findMaxSurvivalTime(a+y[0],b+y[1],x,y,z,"y",{}) ,
            findMaxSurvivalTime(a+z[0],b+z[1],x,y,z,"z",{})
            )
    elif(currArea == 'y'):
        tmp = 1 + max(
            findMaxSurvivalTime(a + x[0], b + x[1], x, y, z, "x", {}),
            findMaxSurvivalTime(a + z[0], b + z[1], x, y, z, "z", {})
        )
    elif(currArea == 'z'):
        tmp = 1 + max(
            findMaxSurvivalTime(a + x[0], b + x[1], x, y, z, "x", {}),
            findMaxSurvivalTime(a + z[0], b + z[1], x, y, z, "y", {})
        )
    memory[key] = tmp
    return tmp




a = 20
b = 8
x = [3,2]
y = [-5,-10]
z = [-20, 5]

print(
    max(
        findMaxSurvivalTime(a+x[0],b+x[1],x,y,z,"x",{}),
        findMaxSurvivalTime(a+y[0],b+y[1],x,y,z,"y",{}) ,
        findMaxSurvivalTime(a+z[0],b+z[1],x,y,z,"z",{})
        )

)