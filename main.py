
#########################IMPORTING LIBRARIES########################
import cv2
import dlib
import winsound
import pyautogui
import numpy as np
from tkinter import *
from PIL import Image,ImageTk
pyautogui.FAILSAFE = False
from imutils import face_utils
#######################IMPORTING FUNCTIONS AND VARIABLES##############
from utils import *
from variables import * 
#####################
keyboard=np.zeros((300,800,3),np.uint8)
font_letter=cv2.FONT_HERSHEY_PLAIN
bd=Blink_detection()
white_board=np.zeros((100,800,3),np.uint8)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("PRETRAINED_MODELS\\shape_predictor_68_face_landmarks.dat")
cap=cv2.VideoCapture(0)
#####################

############# WINDOW VARIBALES#############
mouse = True

##TKINTER WINDOWS SETUP#####
win=Tk()
win.wm_attributes("-topmost",1)
win.title("Hands free operation of computer")
win.geometry("800x600")
win.configure(background="green")
l1=Label(win,bg="black")
l1.pack()



############# DRAWING THE KEYBOARD#################
def draw_keyboard(letter_index,letter,light):

    if letter_index==0:
        x=0
        y=0
    elif letter_index==1:
        x=80
        y=0
    elif letter_index==2:
        x=160
        y=0
    elif letter_index==3:
        x=240
        y=0
    elif letter_index==4:
        x=320
        y=0
    elif letter_index==5:
        x=400
        y=0
    elif letter_index==6:
        x=480
        y=0
    elif letter_index==7:
        x=560
        y=0
    elif letter_index==8:
        x=640
        y=0
    elif letter_index==9:
        x=720
        y=0
    elif letter_index==10:
        x=0
        y=50
    elif letter_index==11:
        x=80
        y=50
    elif letter_index==12:
        x=160
        y=50
    elif letter_index==13:
        x=240
        y=50
    elif letter_index==14:
        x=320
        y=50
    elif letter_index==15:
        x=400
        y=50
    elif letter_index==16:
        x=480
        y=50
    elif letter_index==17:
        x=560
        y=50
    elif letter_index==18:
        x=640
        y=50
    elif letter_index==19:
        x=720
        y=50
    elif letter_index==20:
        x=0
        y=100
    elif letter_index==21:
        x=80
        y=100
    elif letter_index==22:
        x=160
        y=100
    elif letter_index==23:
        x=240
        y=100
    elif letter_index==24:
        x=320
        y=100
    elif letter_index==25:
        x=400
        y=100
    elif letter_index==26:
        x=480
        y=100
    elif letter_index==27:
        x=560
        y=100
    elif letter_index==28:
        x=640
        y=100
    elif letter_index==29:
        x=720
        y=100
    elif letter_index==30:
        x=0
        y=150
    elif letter_index==31:
        x=80
        y=150
    elif letter_index==32:
        x=160
        y=150
    elif letter_index==33:
        x=240
        y=150
    elif letter_index==34:
        x=320
        y=150
    elif letter_index==35:
        x=400
        y=150
    elif letter_index==36:
        x=480
        y=150
    elif letter_index==37:
        x=560
        y=150
    elif letter_index==38:
        x=640
        y=150
    elif letter_index==39:
        x=720
        y=150
    elif letter_index==40:
        x=0
        y=200
    elif letter_index==41:
        x=80
        y=200
    elif letter_index==42:
        x=160
        y=200
    elif letter_index==43:
        x=240
        y=200
    elif letter_index==44:
        x=320
        y=200
    elif letter_index==45:
        x=400
        y=200
    elif letter_index==46:
        x=480
        y=200
    elif letter_index==47:
        x=560
        y=200
    elif letter_index==48:
        x=640
        y=200
    elif letter_index==49:
        x=720
        y=200
    elif letter_index==50:
        x=0
        y=250
    elif letter_index==51:
        x=80
        y=250
    elif letter_index==52:
        x=160
        y=250
    elif letter_index==53:
        x=240
        y=250
    elif letter_index==54:
        x=320
        y=250
    elif letter_index==55:
        x=400
        y=250
    elif letter_index==56:
        x=480
        y=250
    elif letter_index==57:
        x=560
        y=250
    elif letter_index==58:
        x=640
        y=250
    elif letter_index==59:
        x=720
        y=250
    font=cv2.FONT_HERSHEY_PLAIN
    letter_thickness=2
    key_space=2
    font_scale=3
    height=50
    width=80
    if light==True:
        cv2.rectangle(keyboard,(x+key_space,y+key_space),(x+width-key_space,y+height-key_space),(0,255,0),-1)
    else:
        cv2.rectangle(keyboard,(x+key_space,y+key_space),(x+width-key_space,y+height-key_space),(0,255,0),key_space)
    letter_size=cv2.getTextSize(letter,font,font_scale,letter_thickness)[0]
    letter_height,letter_width=letter_size[1],letter_size[0]
    letter_x=int((width-letter_width)/2)+x
    letter_y=int((height+letter_height)/2)+y
    cv2.putText(keyboard,letter,(letter_x,letter_y),font,font_scale,(255,255,255),letter_thickness)
##################################################

############# DRAWING FOR MOUSE ################
def get_stationary_rectangle():
    #This is to draw the stationary rectangle
    ret,frame=cap.read()
    if ret==False:
        get_stationary_rectangle()
    frame = cv2.flip(frame, flipCode=1 )
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=detector(gray)
    #checking the length of the faces to prevent the exception in later
    if len(faces)==0:
        get_stationary_rectangle()
    face=faces[0]
    landmarks=predictor(gray,face)
    width,height=pyautogui.size() #screen width and height
    r_height=landmarks.part(58).y-landmarks.part(28).y
    r_width=int((width*r_height)/height)
    x1=int(landmarks.part(28).x-r_width/2)
    y1=landmarks.part(28).y
    x2=int(landmarks.part(28).x+r_width/2)
    y2=int(landmarks.part(28).y+r_height)
    return(x1,y1,x2,y2)
################################################

#to get the coordinate of the rectangle which remains same through out the run.
r_points=get_stationary_rectangle()

width,height=pyautogui.size()
sx=(width-0)/(r_points[2]-r_points[0])
sy=(height-0)/(r_points[3]-r_points[1])
while True:
    #main_windows = np.zeros((780,1000,3),np.uint8)
    ret,frame=cap.read() #reading the frame form the webcam
    if ret==False:
        continue
    frame = cv2.flip(frame, flipCode=1 )
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #coverting the bgr frame to gray scale
    faces=detector(gray) #this returns the dlib rectangle
    #now extracting the rectangle which contain the upper and lower cordinates of the face
    if len(faces)==0: #to handle when enable to detect the face due to lighting condition
        continue
    face=faces[0]
    landmarks= predictor(gray, face)

    shapes = face_utils.shape_to_np(landmarks)
    eye_img_l, eye_rect_l = bd.crop_eye(gray, eye_points=shapes[36:42])
    eye_img_r, eye_rect_r = bd.crop_eye(gray, eye_points=shapes[42:48])

    eye_img_l = cv2.resize(eye_img_l, dsize=IMG_SIZE)
    eye_img_r = cv2.resize(eye_img_r, dsize=IMG_SIZE)
    eye_img_r = cv2.flip(eye_img_r, flipCode=1)
    eye_input_l = eye_img_l.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.
    eye_input_r = eye_img_r.copy().reshape((1, IMG_SIZE[1], IMG_SIZE[0], 1)).astype(np.float32) / 255.

    pred_l,pred_r=bd.model_predict(eye_input_l,eye_input_r)
    print("left eye openning: "+str(pred_l))
    print("right eye openning: "+str(pred_r))
    if mouse == True:

        x=landmarks.part(34).x
        y=landmarks.part(34).y
        #changing the origin
        cv2.rectangle(frame,(r_points[0],r_points[1]),(r_points[2],r_points[3]),(255,255,255),3)
        x_r=x-r_points[0]
        y_r=y-r_points[1]
        #my_text=str(x_r)+","+str(y_r)
        cv2.circle(frame,(landmarks.part(34).x,landmarks.part(34).y),5,(255,0,0),2)
        cv2.circle(frame,(landmarks.part(63).x,landmarks.part(63).y),5,(255,0,0),2)
        cv2.circle(frame,(landmarks.part(67).x,landmarks.part(67).y),5,(255,0,0),2)
        #cv2.putText(frame,my_text,(100,150),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),3)
        #changing that cordinate into the screen cordinate
        x_m=int(x_r*sx)
        y_m=int(y_r*sy)
        cv2.putText(frame,str(x_m)+","+str(y_m),(200,50),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),2)
        if x_m<0:
            x_m=0
        if x_m>width:
            x_m=width-1
        if y_m<0:
            y_m=0
        if y_m>height:
            y_m=height-1
        print("move pointer to:"+"("+str(x_m)+","+str(y_m)+")")
        pyautogui.moveTo(x_m,y_m)
        if pred_l<0.01:
            print("left eye blink detected")
            print("left click")
            if pred_l<0.001 and pred_r<0.001:
                pass
            cv2.putText(frame,"Left click",(10,50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
            pyautogui.leftClick(x=x_m,y=y_m)

        if pred_r<0.01:
            print("right eye blink detected")
            print("right click")
            if pred_l<0.001 and pred_r<0.001:
                pass
            cv2.putText(frame,"Right click",(450,50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),1)
            pyautogui.rightClick(x=x_m,y=y_m)
        
        #cv2.imshow("frame",frame)
        cv2.rectangle(frame, pt1=tuple(eye_rect_l[0:2]), pt2=tuple(eye_rect_l[2:4]), color=(64,224,208), thickness=2)
        cv2.rectangle(frame, pt1=tuple(eye_rect_r[0:2]), pt2=tuple(eye_rect_r[2:4]), color=(255,0,0), thickness=2)
        frame = cv2.resize(frame,(800,600))
        frame_copy=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frame_copy=ImageTk.PhotoImage(Image.fromarray(frame_copy))
        l1['image']=frame_copy
        win.update()
        mouth_distance=landmarks.part(67).y-landmarks.part(63).y
        if mouth_distance>10:
            print("mouth open")
            mouth_open+=1
        if mouth_open==10:
            mouse = False
            mouth_open=0
            print("Entering into keyboard mode")

    elif mouse == False:
        main_windows = np.zeros((780,1000,3),np.uint8)

        if col_select==True:
            frame_count_row=frame_count_row+1
        else:
            frame_count_column=frame_count_column+1
        
        if frame_count_column==10:
            col=col+1
            if col==10:
                col=0 #to return form last column to the first column
            frame_count_column=0
        if frame_count_row==10:
            row=row+1
            if row==6:
                row=0 #to return form the last row of the entered column to the first 
                col_select=False #to exit from the entered column when all the keys of that column blink
            frame_count_row=0
        if col==0:
            col_index=first_col_index
        elif col==1:
            col_index=second_col_index
        elif col==2:
            col_index=third_col_index
        elif col==3:
            col_index=fourth_col_index
        elif col==4:
            col_index=fifth_col_index
        elif col==5:
            col_index=sixth_col_index
        elif col==6:
            col_index=seventh_col_index
        elif col==7:
            col_index=eighth_col_index
        elif col==8:
            col_index=ninth_col_index
        elif col==9:
            col_index=tenth_col_index
        keyboard[:]=(0,0,0) #reseting the keyboard
        if col_select==False:
            for i in range(0,60):
                if i in col_index:
                    draw_keyboard(i,key_set[i],True)
                else:
                    draw_keyboard(i,key_set[i],False)
        else:
            for i in range(0,60):
                if i == col_index[row]:
                    draw_keyboard(i,key_set[i],True)
                    
                else:
                    draw_keyboard(i,key_set[i],False)

        #######################VIDEO CAPTURE#####################

        if pred_l < 0.3 and pred_r <0.3:
            cv2.putText(main_windows,"------BLINK DETECTED------",(375,325), font_letter,1, (0,0,255),2)
            print("Both eyes blink detected")
            blink_count=blink_count+1
            if col_select==True:
                blink_count_indivisual_key=blink_count_indivisual_key+1
                frame_count_row=frame_count_row-1 #to stay on the active key when ever we blink for longer period
            else:
                frame_count_column=frame_count_column-1 #to stay on the active column when ever we blink for longer period
        else:
            blink_count=0
            blink_count_indivisual_key=0
        if blink_count==10:
            col_select=True #to enter inside the column when the we blink for 10 frames
        #implementing keyboard typing
        if blink_count_indivisual_key==10 and col_select==True:
            col_select=False #to disable the active column
            if key_set[col_index[row]]=='<-':
                type_text=type_text[:-1]
            else:
                print("Typed key:"+key_set[col_index[row]])
                #pyautogui.typewrite(key_set[col_index[row]])
                type_text=type_text+key_set[col_index[row]]
            blink_count_indivisual_key=0
            white_board[:]=(0,0,0)
            winsound.Beep(500,100)
            cv2.putText(white_board,type_text,(10,50),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),3)
            row=0 #resetting the row


            # visualize
        state_l = 'O %.1f' if pred_l > 0.1 else '- %.1f'
        state_r = 'O %.1f' if pred_r > 0.1 else '- %.1f'

        state_l = state_l % pred_l
        state_r = state_r % pred_r

        cv2.rectangle(frame, pt1=tuple(eye_rect_l[0:2]), pt2=tuple(eye_rect_l[2:4]), color=(64,224,208), thickness=2)
        cv2.rectangle(frame, pt1=tuple(eye_rect_r[0:2]), pt2=tuple(eye_rect_r[2:4]), color=(255,0,0), thickness=2)

        # Combaining all windows into single window: 
        main_windows[50:150, 100:200] = cv2.resize(cv2.cvtColor(eye_img_l,cv2.COLOR_BGR2RGB),(100,100))
        cv2.putText(main_windows,"CROPPED LEFT EYE",(90,170), font_letter,1, (255,255,51),2)
        cv2.putText(main_windows,str(state_l+"%"),(100,200), font_letter,2, (0,0,255),2)
        main_windows[50:150, 800:900] = cv2.resize(cv2.cvtColor(eye_img_r,cv2.COLOR_BGR2RGB),(100,100))
        cv2.putText(main_windows,"CROPPED RIGHT EYE",(790,170), font_letter,1, (255,255,51),2)
        cv2.putText(main_windows,str(state_r+"%"),(800,200), font_letter,2, (0,0,255),2)

        main_windows[0:300, 300:700]= cv2.resize(frame,(400,300))
        main_windows[350:650, 100:900] =  keyboard
        main_windows[670:770, 100:900] = white_board
        main_windows=cv2.resize(main_windows,(800,600))
        #cv2.imshow("Main_Windows",main_windows)
        main_windows_copy=cv2.cvtColor(main_windows,cv2.COLOR_BGR2RGB)
        main_windows_copy=ImageTk.PhotoImage(Image.fromarray(main_windows_copy))
        l1['image']=main_windows_copy
        win.update()
        mouth_distance=landmarks.part(67).y-landmarks.part(63).y
        if mouth_distance>10:
            print("mouth open")
            mouth_open+=1
        if mouth_open==10:
            cv2.destroyAllWindows()
            mouse = True
            mouth_open=0
            print("Entering into mouse mode")
cap.release()
