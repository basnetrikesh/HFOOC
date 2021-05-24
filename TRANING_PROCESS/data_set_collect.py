import cv2
import dlib
from imutils import face_utils
from math import hypot
import numpy as np
def midpoint(p1,p2):
    return (int((p1.x+p2.x)/2),int((p1.y+p2.y)/2))#returning the modpoint in the form of tuple
def get_blinking_ratio(facial_landmarks,points): #this is the function to find the blinking ratio of the eye
    left_point=(facial_landmarks.part(points[0]).x,facial_landmarks.part(points[0]).y)
    right_point=(facial_landmarks.part(points[3]).x,facial_landmarks.part(points[3]).y)
    top_point=midpoint(facial_landmarks.part(points[1]),facial_landmarks.part(points[2]))
    bottom_point=midpoint(facial_landmarks.part(points[4]),facial_landmarks.part(points[5]))
    #cv2.line(frame,left_point,right_point,(0,255,0),1) #drawing the horizontal line in the eye
    #cv2.line(frame,top_point,bottom_point,(0,255,0),1) #drawing the vertical line in the eye
    hor_line_len=hypot((left_point[0]-right_point[0]),(left_point[1]-right_point[1])) #fining the horizontal line length
    ver_line_len=hypot((bottom_point[0]-top_point[0]),(bottom_point[1]-top_point[1])) #finding the vertical line length
    ratio=hor_line_len/ver_line_len
    return ratio
def crop_eye(gray, eye_points):
    x1, y1 = np.amin(eye_points, axis=0)
    x2, y2 = np.amax(eye_points, axis=0)
        
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2

    w = (x2 - x1) * 1.2
    h = w * IMG_SIZE[1] / IMG_SIZE[0]

    margin_x, margin_y = w / 2, h / 2

        
    min_x, min_y = int(cx - margin_x), int(cy - margin_y)
    max_x, max_y = int(cx + margin_x), int(cy + margin_y)
    eye_rect = np.rint([min_x, min_y, max_x, max_y]).astype(np.int)

    eye_img = gray[eye_rect[1]:eye_rect[3], eye_rect[0]:eye_rect[2]]

    return eye_img, eye_rect
IMG_SIZE=(34,26)
cap=cv2.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("PRETRAINED_MODELS\\shape_predictor_68_face_landmarks.dat")
i=0
j=0
open=True
while True:
    ret,frame=cap.read()
    if ret==False:
        continue
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=detector(gray)
    if len(faces)==0:
        continue
    face=faces[0]
    landmarks=predictor(gray,face)
    left_eye_ratio=get_blinking_ratio(landmarks,[36,37,38,39,40,41])
    right_eye_ratio=get_blinking_ratio(landmarks,[42,43,44,45,46,47])
    blink_ratio=(left_eye_ratio+right_eye_ratio)/2 #finding the mean of the left eye and right ratio
    print("Blink ratio:"+str(blink_ratio))
    shapes = face_utils.shape_to_np(landmarks)
    eye_img_l, eye_rect_l = crop_eye(gray, eye_points=shapes[36:42])
    eye_img_r, eye_rect_r = crop_eye(gray, eye_points=shapes[42:48])
    eye_img_l = cv2.resize(eye_img_l, dsize=IMG_SIZE)
    eye_img_r = cv2.resize(eye_img_r, dsize=IMG_SIZE)
    eye_img_r = cv2.flip(eye_img_r, flipCode=1)
    if blink_ratio>5.5: #for me 5.5 is perfect
        cv2.putText(frame,"BLINKING",(150,50),cv2.FONT_HERSHEY_COMPLEX,5,(255,0,0),2)
        #save the closed eye picture
        cv2.imwrite("TRANING_PROCESS\\collected\\close\\"+str(i)+"l"+".JPG",eye_img_l)
        cv2.imwrite("TRANING_PROCESS\\collected\\close\\"+str(i)+"r"+".JPG",eye_img_r)
        i=i+1
    else:
        cv2.imwrite("TRANING_PROCESS\\collected\\open\\"+str(j)+"l"+".JPG",eye_img_l)
        cv2.imwrite("TRANING_PROCESS\\collected\\open\\"+str(j)+"r"+".JPG",eye_img_r)
        j=j+1
    cv2.imshow("frame",frame)
    key=cv2.waitKey(10)
    if key==27:
        break
cv2.destroyAllWindows()
cap.release()





    