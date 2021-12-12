import cv2
import numpy as np
img=cv2.imread('bilibili.bmp')
img=cv2.resize(img,(360,360))
board=np.zeros((4000,4000,3), np.uint8)
board[1820:2180,1820:2180]=img
img=np.zeros((720,720,3), np.uint8)
img=board[1640:2360,1640:2360]
video = cv2.VideoWriter("ant_bilibili_2.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 125, (720,720))
ant=[[[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0]],
     [[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0]],
     [[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0],[2000,2000,0]]]
end=np.zeros((3,8),np.bool_)
def move(a,b):
    if int((board[ant[a][b][0],ant[a][b][1],a]%(2**(b+1)))/(2**b))==1:
        ant[a][b][2]+=1
        board[ant[a][b][0],ant[a][b][1],a]-=2**b
    else:
        ant[a][b][2]-=1
        board[ant[a][b][0],ant[a][b][1],a]+=2**b
    ant[a][b][2]=ant[a][b][2]%4
    if ant[a][b][2]==0:
        ant[a][b][0]+=1
        if ant[a][b][0]>3950:
            end[a][b]=True
    if ant[a][b][2]==1:
        ant[a][b][1]+=1
        if ant[a][b][1]>3950:
            end[a][b]=True
    if ant[a][b][2]==2:
        ant[a][b][0]-=1
        if ant[a][b][0]<50:
            end[a][b]=True
    if ant[a][b][2]==3:
        ant[a][b][1]-=1
        if ant[a][b][1]<50:
            end[a][b]=True
K=0
n=0
while(True):
    video.write(img)
    k=0
    n+=1
    for a in range(3):
        for b in range(8):
            if end[a][b]:
                k+=1
            else:
                move(a,b)
    img=board[1640:2360,1640:2360]
    cv2.imshow('image',img)
    if K<k:
        K=k
        print(K,n)
        print(end)
    if cv2.waitKey(1)&0xFF==27 or K==24:
        break
cv2.destroyAllWindows()
video.release()
img=board[80:3920,80:3920]
cv2.imwrite('ant_bilibili_2.bmp',img)
