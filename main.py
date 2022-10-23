import numpy as np
import cv2
import time
import random

pixelCount = 250000
#Rotated Basic mazes
im = cv2.imread(f"new_test_data/Basic mazes/test{random.randint(1,4)}.PNG")  # Input image
mult = np.sqrt(pixelCount/(im.shape[0]*im.shape[1]))
im = cv2.resize(im, (0, 0), fx=mult, fy=mult)
print(im.shape)
# im = Image.open(f"new_test_data/colorGradient.png")  # Input image

startTime = time.time()
# Start of script
grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
lines = cv2.HoughLines(cv2.Canny(grey, 50, 150, apertureSize=3), 0.25, np.pi/180, 100)


if lines is not None:
    for line in lines:
        print(line, '\n')
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(im, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Maze', im)
cv2.imshow('grey', grey)
cv2.waitKey(6000)
cv2.destroyAllWindows()

# End of script
endTime = time.time()
print(f"Operation completed in {round(endTime-startTime,6)*1000}ms")
