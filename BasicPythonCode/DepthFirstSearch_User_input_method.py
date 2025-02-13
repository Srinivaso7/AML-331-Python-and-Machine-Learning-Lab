'''
Implementation of Depth First Search algorithm with user input system, Where the user has the provision to 
dynamically create the graph of their choice without defining the graph inside the code.
'''

#Time complexity : O(V + E)

#Space complexity : O(V)

flag=0
visited=[]
graph={}

def addnode(v):
    if v in graph:
        print("present")
    else:
        graph[v]=[]
    
def addedge(v1,v2):
    if v1 not in graph:
        print (v1,"is not present")
    elif v2  not in graph:
        print (v2,"is not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
def DFS(visited,graph,node,goal,flag):
    if(flag==0):
        if(node not in visited):
            visited.append(node)
            print(node)
            if(node==goal):
                print("Goal node Found")
                flag=1
                exit(0)
            elif(flag==0):
                for neighbour in graph[node]:
                    DFS(visited,graph,neighbour,goal,flag)
        
n=int(input("Enter the number of nodes:"))     
for i in range(1,n+1):
    print("Enter the value of node ",i)
    v=int(input())
    addnode(v)
for i in range(1,n+1):
    print("Enter the number of connections of node ",i)
    m=int(input())
    for j in range(0,m):
        x=int(input("Enter the connections:"))
        addedge(i,x)
x=int(input("Enter the goal node:"))
s=int(input("Enter the starting node:"))
print("Depth First Search is :")
DFS(visited,graph,s,x,0)