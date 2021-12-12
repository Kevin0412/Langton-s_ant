import cv2
import numpy as np
img=cv2.imread('bilibili.bmp')
board=np.zeros((2**15,2**15,3), np.uint8)
board[110:610,110:610]=img
img=np.zeros((720,720,3), np.uint8)
img=board[0:720,0:720]
video = cv2.VideoWriter("ant_bilibili.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 60, (720,720))
ant=[[[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0]],
     [[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0]],
     [[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0],[360,360,0]]]
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
    if ant[a][b][2]==1:
        ant[a][b][1]+=1
    if ant[a][b][2]==2:
        ant[a][b][0]-=1
    if ant[a][b][2]==3:
        ant[a][b][1]-=1
for n in range(216000):
    for a in range(3):
        for b in range(8):
           move(a,b)
    img=board[0:720,0:720]
    cv2.imshow('image',img)
    video.write(img)
    print(n)
    if cv2.waitKey(1)&0xFF==27:
        break
cv2.destroyAllWindows()
video.release()

