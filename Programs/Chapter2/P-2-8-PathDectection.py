from collections import defaultdict
import cv2 as cv
import numpy as np
filepath="Ch2-images/child_1.jpg"
img=cv.imread(filepath,0)
r=100
c=100
class Node:
    def __init__(self,r,c):
        self.r=r
        self.c=c
    def getNodeCoords(self):
        return self.r,self.c

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.Adjacency8=[]

    def get8Adjacency(self,img,p_r,p_c):
        x,y=img.shape
        for r in range(p_r - 1, p_r + 2):
            for c in range(p_c - 1, p_c + 2):
                if r<=x and c<=y:
                    self.Adjacency8.append([r,c])
                    #print(r, c, img[r, c])
        return self.Adjacency8
    def checkExistence(self,nd):
        for i in range(len(self.graph[])):
            print(self.graph[nd].pop(i))

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

#=================================
g = Graph()
lst8=g.get8Adjacency(img,100,100)
nd=Node(100,100)
for i in range(len(lst8)):
    g.checkExistence(nd)
    g.addEdge(nd, lst8[i])
for i in range(len(g.graph.items())):
    print(g.graph[nd][0])


print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
