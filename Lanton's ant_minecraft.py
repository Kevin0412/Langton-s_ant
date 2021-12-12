import cv2
import numpy as np
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
board=np.zeros((2**17,2**17), np.bool_)
ant=[0,0,0]
size=1
def move(n):
    global size
    if board[ant[0],ant[1]]:
        ant[2]+=1
        board[ant[0],ant[1]]=False
        mc.setBlock(ant[0],ant[1]+128,n,35,15)
    else:
        ant[2]-=1
        board[ant[0],ant[1]]=True
        mc.setBlock(ant[0],ant[1]+128,n,35,0)
    ant[2]=ant[2]%4
    if ant[2]==0:
        ant[0]+=1
    if ant[2]==1:
        ant[1]+=1
    if ant[2]==2:
        ant[0]-=1
    if ant[2]==3:
        ant[1]-=1
    if size<abs(ant[0])+1:
        size=abs(ant[0])+1
    if size<abs(ant[1])+1:
        size=abs(ant[1])+1
for n in range(20000):
    move(n)
    img=np.zeros((2*size,2*size),np.uint8)
    for x in range(-size,size):
        for y in range(-size,size):
            if board[x,y]:
                img[x+size,y+size]=255
    img=cv2.resize(img,(720,720))
    cv2.imshow('image',img)
    print(n)
    if cv2.waitKey(1)&0xFF==27:
        break
