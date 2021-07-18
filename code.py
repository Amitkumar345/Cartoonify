# Cartoon : {
# 	proper edges(clear edges), homogeneous/uniform color 
#	finally,masking & showing edges and uniform colored image together
#	}

# ************************************************************* #

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
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 5)
# cv2.imshow("Edges", edges )

# Color
color = cv2.bilateralFilter(img, 9, 250, 250)
# cv2.imshow("Colored", edges )

# Cartoonization 
cartoon = cv2.bitwise_and(color, color, mask =edges) 
# Result
cv2.imshow("Cartoon", cartoon) 

k = cv2.waitKey(0) & 0xFF
# Press key 's' to save the image and any other key to stop the program 
if k == ord('s'):
	cv2.imwrite('cartoon_copy.jpg', cartoon)
	
cv2.destroyAllWindows()

# ************************************************************* #
