import pygame as py
import time
visited=[[0]*701 for i in range(901)]
def bfs(start,target,visited):
    q=[start]
    listpoints=[]
    while len(q)!=0:
        i,j=q.pop(0)
        if i<0 or j<0 or i>900 or j>700 or visited[i][j]==1:
            continue
        if i==target[0] and j==target[1]:
            return listpoints
        listpoints.append((i,j))
        visited[i][j]=1
        q.append((i,j+50))
        q.append((i,j-50))
        q.append((i+50,j))
        q.append((i-50,j))


py.init()
screen=py.display.set_mode((900,700))
on=False
start=tuple(map(int,input('Enter the source:').split()))
target=tuple(map(int,input("Enter the target:").split()))
while not on:
    for event in py.event.get():
        if event.type==py.QUIT:
            on=True
    i=0
    j=0
    while i<=900 and j<=700:
        py.draw.rect(screen,(0,0,244), (i, j, 50, 50), 2)
        i=i+50
        if i%900==0:
            i=0
            j=j+50
        py.display.update()
    py.draw.rect(screen, (255, 0,0), (start[0],start[1],50, 50), 0)
    py.draw.rect(screen, (255, 0, 0), (target[0],target[1], 50, 50), 0)
    f=0
    if event.type == py.MOUSEBUTTONUP:
        for i in bfs(start,target, visited):
            py.draw.rect(screen, (255, 0, 0), (start[0],start[1], 50, 50), 0)
            py.draw.rect(screen,(0,255,0),(i[0],i[1],50,50),0)
            time.sleep(0.1)
            py.display.update()
            if i[0]==target[0] and i[1]==target[1]:
                py.draw.rect(screen, (255, 0, 0), (target[0],target[1], 50, 50), 0)
                continue
        py.display.flip()
        py.time.delay(100000)

