
# Cartoon : {proper edges(clear edges), homogeneous/uniform color , finally,showing edges and uniform colored image together}


# importing libraries 
import cv2 
import numpy as np 

# reading image 
img = cv2.imread('input.jpg',1) 
img = cv2.resize(img, (760, 820)) 
# cv2.imshow("Image", img)

# Edges Recognition
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
										cv2.THRESH_BINARY, 9, 5)

# Color
color = cv2.bilateralFilter(img, 9, 250, 250)
# Cartoonization 
cartoon = cv2.bitwise_and(color, color, mask =edges) 

# cv2.imshow("Edges", edges )
cv2.imshow("Cartoon", cartoon) 
k = cv2.waitKey(0) & 0xFF
# Press key 's' to save the image
if k == ord('s'):
	cv2.imwrite('cartoon_copy.jpg', cartoon)
cv2.destroyAllWindows()


# ***********************Other way to code**************************************

# from google.colab.patches import cv2_imshow
# import cv2
# import numpy as np
# # import matplotlib.pyplot as plt

# img = cv2.imread('koala.jpg',1)
# img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
# # img2 = cv2.resize(img1, (500, 540))  # resize
# img3 = cv2.medianBlur(img1, 5)  # smooth
# img4 = cv2.resize(img3, (500, 540))  # resize

# img5 = cv2.adaptiveThreshold(img4, 255,
#                              cv2.ADAPTIVE_THRESH_MEAN_C,
#                              cv2.THRESH_BINARY, 11, 11)  # getting edges
# # img6 = cv2.resize(img5, (500, 540))  # resize
# # cartoonization
# img7 = cv2.bilateralFilter(img, 9, 300, 300) # smoothen
# img8 = cv2.resize(img7, (500, 540))  # resize

# cartoonImage = cv2.bitwise_and(img8, img8, mask=img5)
# img9 = cv2.resize(cartoonImage, (500, 540))  # resize

# # print(img9)
# cv2.imshow('output', img9)
# # cv2_imshow(img9)
# k = cv2.waitKey(0) & 0xFF
# print(k)
# if k == 27:
#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     cv2.imwrite('profile_copy.png', img9)
#     cv2.destroyAllWindows()

