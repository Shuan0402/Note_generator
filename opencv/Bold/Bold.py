import cv2
img = cv2.imread('test.jpg')
cv2.imshow('oxxostudio1', img)   # 原始影像

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

img = cv2.erode(img, kernel)     # 先侵蝕，將白色小圓點移除
cv2.imshow('oxxostudio2', img)   # 侵蝕後的影像

cv2.waitKey(0)                   # 按下 q 鍵停止
cv2.destroyAllWindows()