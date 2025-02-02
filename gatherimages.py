import cv2
import os
import sys

try:
    label_name=sys.argv[1];
    num_samples=int(sys.argv[2])
except:
    print("Please enter the arguments!!");
    print(desc)
    exit(-1)

IMG_SAVE_PATH='images'
IMG_CLASS_PATH=os.path.join(IMG_SAVE_PATH,label_name)

try:
    os.mkdir(IMG_SAVE_PATH)
except FileExistsError:
    pass

try:
    os.mkdir(IMG_CLASS_PATH)
except FileExistsError:
    print('{} Directory already exists'.format(IMG_CLASS_PATH))
    print("ALL images will be stored in this existing folder")

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)


start=False
count=0
while True:
    ret,frame=cap.read()
    if not ret:
        continue
    if count==num_samples:
        break
    cv2.rectangle(frame,(100,100),(500,500),(255,255,255),2)
    if start:
        roi=frame[100:500,100:500]
        save_path=os.path.join(IMG_CLASS_PATH,'{}.jpg'.format(count+1))
        cv2.imwrite(save_path,roi)
        count += 1

    font =cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,"collecting {}".format(count),(5,50),font,0.7,(0,255,255),2,cv2.LINE_AA)
    cv2.imshow("COLLECTING IMAGES",frame)

    k = cv2.waitKey(10)
    if k == ord('a'):
        start=not start
    if k== ord('q'):
        break
print("\n images are saved to {}".format(count,IMG_CLASS_PATH))
cap.release()
cv2.destroyAllWindows()


