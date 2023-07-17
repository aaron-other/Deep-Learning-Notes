import cv2 as cv

img = cv.imread('../image/demo.jpg')
w, h = img.shape[: 2]
cv.imshow('1', img)
print(w, h)
cv.waitKey(0)
cv.destroyAllWindows()
