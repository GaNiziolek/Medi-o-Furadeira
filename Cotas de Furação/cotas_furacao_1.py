#todo: processamento está muito lento, Canny está muito pesado

import cv2
import numpy as np
import time

def escrever(imagem, texto, x, y):
    return(cv2.putText(imagem, texto, (x, y), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1,cv2.LINE_AA))
def nothing(x):
    pass
cv2.namedWindow('Edges', 0)

cv2.createTrackbar('Canny low', 'Edges', 100, 400, nothing)
cv2.createTrackbar('Canny high', 'Edges', 150, 400, nothing)

while True:
    img_src = cv2.imread('Imagens_Teste\Tampo Caemmun\Face 1 sup 1.jpg')

    if img_src is None:
        print('ERROR: Img is None')
        cv2.destroyAllWindows()
        exit()
    
    #img_src = cv2.resize(img_src, (1024, 720))
    img_eroded = cv2.erode(img_src, None, iterations=1)
    img_dilated = cv2.dilate(img_eroded, None, iterations=1)

    #img_gray = cv2.cvtColor(img_dilated, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.blur(img_dilated, (3, 3))
    
    canny_l = cv2.getTrackbarPos('Canny low', 'Edges')
    canny_h = cv2.getTrackbarPos('Canny high', 'Edges')
    img_edged = cv2.Canny(img_blur, canny_l, canny_h)
    
    (contours, hierarchy) = cv2.findContours(img_edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    n_obj = 0

    for cnt in contours:
        M = cv2.moments(cnt)
        
        if n_obj != 0 and M['m00'] != 0 :

            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])
            
            escrever(img_src, 'X {}'.format(cX), cX+5, cY-10)
            escrever(img_src, 'Y {}'.format(cY), cX+5, cY+10)
            escrever(img_src, 'N{}'.format(n_obj), cX-40, cY)
        n_obj += 1
        
    '''
    for i in range(len(contours)):
        print('[Next, Previous, First_Child, Parent] \n' + str(hierarchy[0]) + '\nContorno ' + str(i) + ': \n' + str(contours[i]) + '\n \n')
    '''

    tamanho_img = (640, 480)

    cv2.drawContours(img_src,contours, -1, (0,0,255),1)
    cv2.imshow('Peca blur', cv2.resize(img_blur, tamanho_img))
    cv2.imshow('Eroded', cv2.resize(img_eroded, tamanho_img))
    cv2.imshow('Dilated', cv2.resize(img_dilated, tamanho_img))
    cv2.imshow('Blur', cv2.resize(img_blur, tamanho_img))
    cv2.imshow('Edges', cv2.resize(img_edged, tamanho_img))
    cv2.imshow('ctns', cv2.resize(img_src, tamanho_img))
    #cv2.imwrite('Imagens Teste\res.jpeg', img_src)
    #cv2.imshow('edge', img_edged)

    k = cv2.waitKey(27)
    if k == 27:
        break

cv2.destroyAllWindows()