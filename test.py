#!\usr\bin\env python3

import cv2
import numpy as np

if __name__ == "__main__":

    vid = cv2.VideoCapture('IMG_5774.mp4')
    cv2.namedWindow('test')

    nframes = int(round(vid.get(cv2.CAP_PROP_FRAME_COUNT)))
    frame_rate = vid.get(cv2.CAP_PROP_FPS)

    kernel = np.ones((5,5),np.uint8)
    
    for i in range(nframes):
        retval,raw = vid.read()
        if retval:
            hsv = cv2.cvtColor(raw,cv2.COLOR_BGR2HSV)
            ir = cv2.inRange(hsv,(25,32,0),(40,255,255))
            er = cv2.erode(ir,kernel,iterations=2)
            c,h = cv2.findContours(er,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

            display = raw.copy()
            if c:
                As = [cv2.contourArea(ec) for ec in c]
                max_i = np.argmax(As)
                biggest=c[max_i]
                biggestA = np.max(As)
                if (biggestA>1200):
                    x,y,width,height = cv2.boundingRect(biggest)
                    cv2.rectangle(display,(x,y),(x+width,y+height),(0,255,0),2)
            cv2.imshow('test',display)
            cv2.waitKey(int(round(1000/frame_rate)))
            cv2.imwrite('results/frame{0:03d}.png'.format(i),display)

    cv2.destroyAllWindows()
