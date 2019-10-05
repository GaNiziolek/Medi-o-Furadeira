import cv2

imagem_original = cv2.imread('E:\\Downloads\\eu e mariana.jpg')

imagem_gray = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)

imagem_cont = cv2.Canny(imagem_gray, 20, 100)

cv2.imshow('Imagem',imagem_original)
cv2.imshow('Imagem cinza', imagem_gray)
cv2.imshow('Contornos', imagem_cont)
cv2.waitKey(0)
cv2.destroyAllWindows()
