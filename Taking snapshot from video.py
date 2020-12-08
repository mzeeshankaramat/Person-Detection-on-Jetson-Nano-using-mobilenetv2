import cv2
cap = cv2.VideoCapture('7.avi')
def getFrame(sec):
    cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    ret,image = cap.read()    ## ret contains bool value while image has captured frame
    if ret:
        cv2.imwrite("C:/study/7th Sem/CV/Project/data/image"+str(count)+".jpg", image)     # save frame as JPG file
        cv2.imshow('frame', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
    return ret     
sec = 0
frameRate = 1 #want to capture frames with how much delay...it will capture frame every 2 sec
count=1     #for saving frames in sequence
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    


