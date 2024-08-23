import cv2
import numpy as np

img = cv2.imread('./data/14.JPG')
width = int(img.shape[1])
print(width)
height = int(img.shape[0])
num = 0

a, b, r, a2, b2, r2 = 0, 0, 0, 0, 0, 0

while True:
    
    height += 10
    print("hight11111111111", height)
    print('widhds', width)

    img  = cv2.resize(img,(width, height))
    
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
    gray_blurred = edges
    # cv2.imshow('img', gray_blurred)
    detected_circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=50,maxRadius=300)

    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            num += 1
            a, b, r = pt[0], pt[1], pt[2]
            if r>=25:
            # Draw the circumference of the circle.
                print('radus', r)
                img2 = img
                cv2.imshow('111', img)

                cv2.circle(img2, (a, b), r, (0, 255, 0), 2)
        
                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(img2, (a, b), 1, (0, 0, 255), 3)
                cv2.imshow("Detected Circle", img2)
                # cv2.imshow('img', gray_blurred)
                cv2.waitKey(0)
                ######################################################## circle 2
                # cv2.imshow('img', gray_blurred)
                cv2.waitKey(0)

            print("2222222222222")

    print("11111111111111111111111") 
    cv2.waitKey(0)           
cv2.waitKey(0)

# cv2.imshow('edg', edges)
# cv2.waitKey(0)
