from handDetector import HandDetector
import cv2
import mediapipe as mp
import time
import pyautogui

camera = cv2.VideoCapture(0)
camera.set(3,1280)
camera.set(4,720)

screenWidth, screenHeight = pyautogui.size()
handDetector = HandDetector(min_detection_confidence=0.7)

cursor_speed = 0.8
scrollUP_value = 50
scrollDown_value = -50

movement_control = False
left_clicked = False
double_clicked = False
dragging = False
scroll_up = False
scroll_down = False
rigth_clicked = False

previous_x4 = None
previous_y8 = None
previous_y12 = None
previous_y16 = None

threshold = 50

x4_changed = False
y8_change_control = False 
y12_change_control = False 
y16_change_control = False 

def move_cursor(x,y):
    global cursor_speed
    mousePositionX = screenWidth/frameWidth*x
    mousePositionY = screenHeight/frameHeight*y
    mousePositionX = mousePositionX * cursor_speed
    mousePositionY = mousePositionY * cursor_speed
    pyautogui.moveTo(mousePositionX, mousePositionY)

while True:
    ret,frame = camera.read()
    frame = cv2.flip(frame,1)
    frameHeight, frameWidth, _ = frame.shape
    handLandmarks = handDetector.findHandLandMarks(image=frame, draw=True)

    if(len(handLandmarks) != 0):
        x0, y0 =handLandmarks[0][1], handLandmarks[0][2]
        x1, y1 =handLandmarks[1][1], handLandmarks[1][2]
        x2, y2 =handLandmarks[2][1], handLandmarks[2][2]
        x3, y3 =handLandmarks[3][1], handLandmarks[3][2]
        x4, y4 =handLandmarks[4][1], handLandmarks[4][2]
        x5, y5 =handLandmarks[5][1], handLandmarks[5][2]
        x6, y6 =handLandmarks[6][1], handLandmarks[6][2]
        x7, y7 =handLandmarks[7][1], handLandmarks[7][2]
        x8, y8 =handLandmarks[8][1], handLandmarks[8][2]
        x9, y9 =handLandmarks[9][1], handLandmarks[9][2]
        x10, y10 =handLandmarks[10][1], handLandmarks[10][2]
        x11, y11 =handLandmarks[11][1], handLandmarks[11][2]
        x12, y12 =handLandmarks[12][1], handLandmarks[12][2]
        x13, y13 =handLandmarks[13][1], handLandmarks[13][2]
        x14, y14 =handLandmarks[14][1], handLandmarks[14][2]
        x15, y15 =handLandmarks[15][1], handLandmarks[15][2]
        x16, y16 =handLandmarks[16][1], handLandmarks[16][2]
        x17, y17 =handLandmarks[17][1], handLandmarks[17][2]
        x18, y18 =handLandmarks[18][1], handLandmarks[18][2]
        x19, y19 =handLandmarks[19][1], handLandmarks[19][2]
        x20, y20 =handLandmarks[20][1], handLandmarks[20][2]

        if previous_y8 is not None:
            change = y8 - previous_y8
            if abs(change) > threshold:
                if change > 0:
                    y8_change_control = True
                else:
                    y8_change_control = False
        
        previous_y8 = y8  
        
        if previous_y12 is not None:
            change = y12 - previous_y12
            if abs(change) > threshold:
                if change > 0:
                    y12_change_control = True
                else:
                    y12_change_control = False
        
        previous_y12 = y12 

        if previous_y16 is not None:
            change = y16 - previous_y16
            if abs(change) > threshold:
                if change > 0:
                    y16_change_control = False
                else:
                    y16_change_control = True
        
        previous_y16 = y16 


        if previous_x4 is not None:
            change = x4 - previous_x4
            if abs(change) > threshold:
                if change > 0:
                    x4_change_control = False
                else:
                    x4_change_control = True
        
        previous_x4 = x4 

        #Index finger and movement control
        if y8 < y7 and y12 < y11  and y16 > y13 and y20 > y17 and x4 > (x2+20):
            movement_control = True
            left_clicked = False
            dragging = False
            scroll_up = False
            scroll_down = False
            double_clicked = False
        elif y8 < y7 and y12 > y11 and y16 > y13 and y20 > y17 and x4 > (x2+20) and y12_change_control:
            left_clicked = True
            movement_control = False
            dragging = False
            scroll_up = False
            scroll_down = False
            double_clicked = False
        elif y12 > y9  and y16 > y13 and y20 > y17 and y8 > y5 and x4 > (x2+20) and y8_change_control and y12_change_control:
            dragging = True
            movement_control = False
            left_clicked = False
            scroll_up = False
            scroll_down = False
            double_clicked = False
        elif y12 < y11 and y16 < y15 and y20 < y19 and y8 < y7 and x4 > (x2+20):
            dragging = False
            movement_control = False
            left_clicked = False
            scroll_up = True
            scroll_down = False
            double_clicked = False
        elif y12 < y11 and y16 < y15 and y20 < y19 and y8 < y7 and x4 < (x2-20):
            dragging = False
            movement_control = False
            left_clicked = False
            scroll_up = False
            scroll_down = True
            double_clicked = False
        elif y12 < y11 and y16 < y15 and y20 > y17 and y8 < y7 and x4 > (x2+20) and y16_change_control:
            double_clicked = True
            dragging = False
            movement_control = False
            left_clicked = False
            scroll_up = False
            scroll_down = False

        elif y12 < y11 and y16 > y13 and y20 > y17 and y8 < y7 and x4 < (x2-20) and x4_change_control:
            double_clicked = False
            rigth_clicked = True
            dragging = False
            movement_control = False
            left_clicked = False
            scroll_up = False
            scroll_down = False


        if movement_control == True and left_clicked == False and dragging == False and scroll_up == False and scroll_down == False and double_clicked == False:
            left_clicked = False
            rigth_clicked = False
            cv2.circle(img=frame, center=(x8,y8), radius=25, color=(0, 255, 255))
            print("Movement")
            move_cursor(x8,y8)
        elif left_clicked == True and rigth_clicked == False and movement_control == False and dragging == False and scroll_up == False and scroll_down == False and double_clicked == False:
            movement_control = False
            pyautogui.click()
            print("Left Clicking")
            left_clicked = False
            dragging = False
            y12_change_control = False
            double_clicked = False
            rigth_clicked = False

        #Double Clicked
        elif double_clicked == True and rigth_clicked == False and dragging == False and left_clicked == False and movement_control == False and scroll_up == False and scroll_down == False:
            movement_control = False
            left_clicked = False
            rigth_clicked = False
            pyautogui.doubleClick()
            double_clicked = False
            print("Double Clicking")
            dragging = False
            y12_change_control = False
            y16_change_control = False

        #Scrolling up
        elif left_clicked == False and rigth_clicked == False and movement_control == False and dragging == False and scroll_up == True and scroll_down == False and double_clicked == False:
            left_clicked = False
            dragging = False
            movement_control = False
            double_clicked = False
            rigth_clicked = False
            print("Scrolling up")
            pyautogui.scroll(scrollUP_value)
        #Scrolling down
        elif left_clicked == False and rigth_clicked == False and movement_control == False and dragging == False and scroll_up == False and scroll_down == True and double_clicked == False: 
            left_clicked = False
            dragging = False
            movement_control = False
            double_clicked = False
            rigth_clicked = False
            print("Scrolling down")
            pyautogui.scroll(scrollDown_value)
        #Dragging
        elif dragging == True and rigth_clicked == False and left_clicked == False and movement_control == False and scroll_up == False and scroll_down == False and double_clicked == False:
            left_clicked = False
            movement_control = False
            double_clicked = False
            rigth_clicked = False
            print("Dragging")
            pyautogui.mouseDown(button = "left")
        #Rigth Click
        elif rigth_clicked == True and dragging == False and left_clicked == False and movement_control == False and scroll_up == False and scroll_down == False and double_clicked == False:
            left_clicked = False
            movement_control = False
            double_clicked = False
            dragging = False
            print("Rigth Click")
            pyautogui.click(button='right')
            rigth_clicked = False
            x4_change_control = False

    cv2.imshow("Frame",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()