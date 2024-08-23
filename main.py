import cv2
import os
import numpy as np
# Read the original image
img = cv2.imread('./data/11.jpg') 

width = int(img.shape[1])
height = int(img.shape[0])
num = 0
list_a = []
list_b = []
list_r = []
while True:
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
    
    # Sobel Edge Detection
    # sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    # sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    # Display Sobel Edge Detection Images
    # cv2.imshow('Sobel X', sobelx)
    # # cv2.waitKey(0)
    # cv2.imshow('Sobel Y', sobely)
    # cv2.waitKey(0)
    # cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
    # cv2.waitKey(0)
    
    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection


    height += 10
    img = cv2.resize(edges, (width, height))


    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Blur using 3 * 3 kernel.
    # gray_blurred = cv2.blur(gray, (3, 3))

    gray_blurred = img
    
    # Apply Hough transform on the blurred image.
    # detected_circles = cv2.HoughCircles(gray_blurred, 
    #                 cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
    #             param2 = 30, minRadius = 1, maxRadius = 40)
    detected_circles = cv2.HoughCircles(gray_blurred, 
                cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
            param2 = 30, minRadius = 1, maxRadius = 40)

    # detected_circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT,1,20,
    #                         param1=50,param2=30,minRadius=0,maxRadius=0)
    
    # Draw circles that are detected.
    if detected_circles is not None:
    
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
    
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            if r>=30:
            # Draw the circumference of the circle.
                print('radus', r)
                cv2.circle(img, (a, b), r, (0, 255, 0), 2)
        
                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
                cv2.imshow( str(num)+"Detected Circle", img)
                list_a.append(a)
                list_b.append(b)
                list_r.append(r)
                num += 1
                if num == 2:
                    break
        # tank_height = list_r[1] - list_r[0] + sqrt((list_a[1]-list_a[0])**2 + (list_b[1]-list_b[0])**2)

            cv2.waitKey(0)














# Convert to graycsale
# for img in path_list:
#     img = "./data/" + img
#     print("11111path:", img)
#     img1 = cv2.imread(img)
#     img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     # Blur the image for better edge detection
#     img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
    
#     # Sobel Edge Detection
#     # sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
#     # sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
#     sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
#     # Display Sobel Edge Detection Images
#     # cv2.imshow('Sobel X', sobelx)
#     # # cv2.waitKey(0)
#     # cv2.imshow('Sobel Y', sobely)
#     # cv2.waitKey(0)
#     # cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
#     # cv2.waitKey(0)
    
#     # Canny Edge Detection
#     edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
#     # Display Canny Edge Detection Image
#     cv2.imshow('Canny Edge Detection', edges)
#     cv2.waitKey(0)
    
#     cv2.destroyAllWindows()