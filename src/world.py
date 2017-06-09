from pprint import pprint

def create_world(filename):
    import re
    buffer=open(filename).read()
    lines=buffer.splitlines()
    numbers=[]
    numbers+=re.findall("[-\d]+",lines[0])
    x=int(numbers[0])
    y=int(numbers[1])
    a2d = [ [0]*x for _ in range(y)]
    for i in range(1,len(lines)):
        wallnumbers=[]
        robotnumbers=[]
        goalnumbers=[]
        value=lines[i].strip().split()
        if value[0]=='w':
            for j in range(0,len(value)):
                wallnumbers+=re.findall("[-\d]+",value[j])
            wx=int(wallnumbers[0])
            wy=int(wallnumbers[1])
            a2d[wx][wy]=1
        if value[0]=="r2d2":
            for j in range(0,len(value)):
                robotnumbers+=re.findall("[-\d]+",value[j])
            rx=int(robotnumbers[2])
            ry=int(robotnumbers[3])
        if value[0]=="goal":
            for j in range(0,len(value)):
                goalnumbers+=re.findall("[-\d]+",value[j])
            gx=int(goalnumbers[0])
            gy=int(goalnumbers[1])
    e=rx
    f=ry
    r2d2=a2d[e][f]
    a2d[e][f]='r'
    goal=a2d[gx][gy]
    a2d[gx][gy]='g'
    return a2d

def where_is_robot(a2d):
    l=len(a2d)
    for i in range(l):
        for j in range(l):
            if(a2d[i][j]=='r'):
                n=[i,j]
                break;
    return n
    
                            
def move_robot(x,y,a2d):
    r=where_is_robot(a2d)
    a2d[r[0]][r[1]]='p'
    a2d[x][y]='r'
    return a2d 

    
def goal_reached(a2d):

    for i in range(0,len(a2d)):
        for j in range(0,len(a2d[0])):
            if(a2d[i][j]=='g'):
                goal=[i,j]
                return False
                break
    return True        
                

    
'''for i in range(0,len(a2d)):
        for j in range(0,len(a2d[0])):
            if(a2d[i][j]=='g'):
                goal=[i,j]
                break
    if(goal==where_is_robot(a2d)):
        return True
    else:
        return False '''
    
'''def robot_back(a2d):
    n=where_is_robot(a2d)
    if (is_feasible(n[0],n,a2d)):'''
        
#pprint(create_world("world1.dat"))
#print(where_is_robot(create_world("world1.dat")))
def is_feasible(new_x,new_y,a2d):
    n = where_is_robot(a2d)
    p=len(a2d)
    q=len(a2d[0])
    
    
    if(0<=new_x<p and 0<=new_y<q):
        if((new_x==n[0] and new_y!=n[1])or(new_x!=n[0] and new_y==n[1])):
            if(a2d[new_x][new_y]==1 or a2d[new_x][new_y]=='p'):
                return False
            else:
                return True
        else:
            return False
    else:
        return False
    
def is_feasible2(new_x,new_y,a2d):
    n = where_is_robot(a2d)
    p=len(a2d)
    q=len(a2d[0])
    
    
    if(0<=new_x<p and 0<=new_y<q):
        if((new_x==n[0] and new_y!=n[1])or(new_x!=n[0] and new_y==n[1])):
            if(a2d[new_x][new_y]==1):
                return False
            else:
                return True
        else:
            return False
    else:
        return False
    
'''n=where_is_robot(create_world("world1.dat"))
print(is_feasible(6, 0, create_world("world1.dat")))
robot1=n[0]
robot2=n[1]  
print(n)
print(is_feasible(n[0]+1,n[1],create_world("world1.dat")))
pprint(move_robot(7, 7, create_world("world1.dat")))
print(goal_reached(move_robot(5, 0, create_world("world1.dat"))))
print(where_is_robot(move_robot(5, 0, create_world("world1.dat"))))
print(is_feasible(2, 0, move_robot(5, 0, create_world("world1.dat"))))
print(goal_reached(move_robot(2,7,(create_world("world1.dat")))))'''