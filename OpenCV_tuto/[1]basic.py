import cv2

img = cv2.imread('assets/test.jpeg', 1)
img = cv2.resize(img, (400, 400))
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) metá
img = cv2.rotate(img, cv2.cv2.ROTATE_180)

# Manipulate
cv2.imwrite('new_img.jpg', img) #Salva una copia con le modifiche effettuate

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()