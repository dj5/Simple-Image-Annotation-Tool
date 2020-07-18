import cv2
import numpy as np
import os
import pandas as pd
from tkg import GUI
ix,iy,ix2,iy2 = -1,-1,-1,-1
# mouse callback function

flag=0
k=None
img=None
def draw_circle(event,x,y,flags,param):
    global ix,iy,ix2,iy2,flag

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        if flag ==0:
         ix,iy = x,y
         flag=1
        elif flag== 1:
         ix2,iy2=x,y
         flag=0
         
def main():
    global k,flag,img
    print("Select Path First")
    o=GUI()
    o.gui()
    df = pd.DataFrame(columns=["Filename","x1","y1","x2","y2","classname"])

    while o.path == "":
     print("Select Path First")
     o.gui()
    os.chdir(o.path)
    files =  os .listdir()
    while len(files)==0:
        print("Directory empty select different directory")
        o.gui()
    print("{0} Files Found".format(len(files)))

    print("Double Click on the Top Left and then Bottom-Right corner of object to get bounding box coordinates (You can see blue circles for selected coordinates)")
    print("Then press key 'c' to select class")

    for f in files:
        if f.find(".JPG")>-1 or f.find(".jpg")>-1 or f.find(".png")>-1 or f.find(".jpeg")>-1:

            img = cv2.imread(f,1)
            cv2.resize(img,(640,640))
            cv2.namedWindow('image',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('image', 600, 600)
            cv2.setMouseCallback('image',draw_circle)

            if o.quit==True or k==ord('q'):
             break
            while(1):

                cv2.imshow('image',img)


                k = cv2.waitKey(20) & 0xFF

                if o.next == True or k==ord('q'):
                    o.next=False
                    break
                elif k == ord('c'):
                    if flag ==0:
                     abpath=os.path.abspath(f)
                     o.gui()
                     classname=o.class_name
                     if classname!="":
                        x1,x2 = min(ix,ix2),max(ix,ix2)
                        y1,y2 = min(iy,iy2),max(iy,iy2)
                        df=df.append({"Filename":abpath,"x1":x1,"y1":y1 ,"x2":x2, "y2":y2,"classname":classname}, ignore_index=True)

                     print(df)

                    print (ix,iy,ix2,iy2)
            cv2.destroyAllWindows()
            df.to_csv(os.path.join(o.path,"data.csv"), index=False)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
