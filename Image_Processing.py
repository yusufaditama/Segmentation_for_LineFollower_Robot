import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
#Capturing Image
camera = cv2.VideoCapture(0)
while True:
    ret,frame = camera.read()
    cv2.imshow("Original",frame)
    
    #Frame Sizes
    print(frame.shape)
    
    #Resizing Image
    resizing = cv2.resize(frame, (320, 240))
    cv2.imshow("Resizing", resizing)
    
    #Cropping Image
    croppedFrame = resizing[200:241, 0:321]
    cv2.imshow("Cropping",croppedFrame)
    
    #Grayscale Image
    gray = cv2.cvtColor(croppedFrame, cv2.COLOR_BGR2GRAY)
    gray1 = gray[0:41, 0:41]
    gray2 = gray[0:41, 40:81]
    gray3 = gray[0:41, 80:121]
    gray4 = gray[0:41, 120:161]
    gray5 = gray[0:41, 160:201]
    gray6 = gray[0:41, 200:241]
    gray7 = gray[0:41, 240:281]
    gray8 = gray[0:41, 280:321]
    cv2.imshow("Grayscale",gray)
    
    #Thresholding
    ret, threshold1 = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
    ret, threshold2 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
    ret, threshold3 = cv2.threshold(gray3, 127, 255, cv2.THRESH_BINARY)
    ret, threshold4 = cv2.threshold(gray4, 127, 255, cv2.THRESH_BINARY)
    ret, threshold5 = cv2.threshold(gray5, 127, 255, cv2.THRESH_BINARY)
    ret, threshold6 = cv2.threshold(gray6, 127, 255, cv2.THRESH_BINARY)
    ret, threshold7 = cv2.threshold(gray7, 127, 255, cv2.THRESH_BINARY)
    ret, threshold8 = cv2.threshold(gray8, 127, 255, cv2.THRESH_BINARY)
    ret, threshold_yes = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    ret, threshold_no = cv2.threshold(croppedFrame, 127, 255, cv2.THRESH_BINARY)
    
    #Division of Thresholding
    box1 = cv2.rectangle(threshold_yes, (0,0), (40,40), (0,0,0),  2)
    box2 = cv2.rectangle(threshold_yes, (40,0), (80,40), (0,0,0),  2)
    box3 = cv2.rectangle(threshold_yes, (80,0), (120,40), (0,0,0),  2)
    box4 = cv2.rectangle(threshold_yes, (120,0), (160,40), (0,0,0),  2)
    box5 = cv2.rectangle(threshold_yes, (160,0), (200,40), (0,0,0),  2)
    box6 = cv2.rectangle(threshold_yes, (200,0), (240,40), (0,0,0),  2)
    box7 = cv2.rectangle(threshold_yes, (240,0), (280,40), (0,0,0),  2)
    box8 = cv2.rectangle(threshold_yes, (280,0), (320,40), (0,0,0),  2)
    cv2.imshow("Division",threshold_yes)
   
    #Segmentation
    if threshold1.any() != 0:       
        num1 = "0"
    else:
        num1= "1"
    if threshold2.any() != 0:
        num2 = "0"
    else:
        num2= "1"
    if threshold3.any() != 0:
        num3 = "0"
    else:
        num3= "1"
    if threshold4.any() != 0:
        num4 = "0"
    else:
        num4= "1"
    if threshold5.any() != 0:
        num5 = "0"
    else:
        num5= "1"
    if threshold6.any() != 0:
        num6 = "0"
    else:
        num6= "1"
    if threshold7.any() != 0:
        num7 = "0"
    else:
        num7= "1"
    if threshold8.any() != 0:
        num8 = "0"
    else:
        num8= "1"
        
    box = cv2.rectangle(threshold_no, (0, 0), (320, 40), (0, 255, 255), -1)
    
    cv2.line(threshold_no, (40,0), (40,320), (255,255,255),  2)
    cv2.line(threshold_no, (80,0), (80,320), (255,255,255),  2)
    cv2.line(threshold_no, (120,0), (120,320), (255,255,255),  2)
    cv2.line(threshold_no, (160,0), (160,320), (255,255,255),  2)
    cv2.line(threshold_no, (200,0), (200,320), (255,255,255),  2)
    cv2.line(threshold_no, (240,0), (240,320), (255,255,255),  2)
    cv2.line(threshold_no, (280,0), (280,320), (255,255,255),  2) 
    
    cv2.putText(threshold_no, num1, (10, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(threshold_no, num2, (50, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(threshold_no, num3, (90, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(threshold_no, num4, (130, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(threshold_no, num5, (170, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(threshold_no, num6, (210, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(threshold_no, num7, (250, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(threshold_no, num8, (290, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Segmentation",threshold_no)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
