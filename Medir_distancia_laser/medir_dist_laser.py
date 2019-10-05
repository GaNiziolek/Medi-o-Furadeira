import cv2

def escrever(imagem, texto, x, y):
    return(cv2.putText(imagem, texto, (x, y), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1,cv2.LINE_AA))

#Constantes a serem reguladas de acordo com o ambiente
#em pixels
min_dist_val = 600 
max_dist_val = 650

#em metros
max_dist = 2
precisao = max_dist / (max_dist_val - min_dist_val)

#aqui devem ser ajustados a tolerância para a cor do laser
min_range = (13,7,212)
max_range = (53,47,252)

img_src = cv2.imread('Img_teste\Maior_distancia.jpg')

while True:
    mask_bgr = cv2.inRange(img_src,min_range, max_range) 
    res_bgr = cv2.bitwise_and(img_src,img_src, mask =mask_bgr)

    img_gray = cv2.cvtColor(res_bgr, cv2.COLOR_BGR2GRAY)
    img_cnt, lx = cv2.findContours(img_gray , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE) 

    #cv2.drawContours(img_src , img_cnt , -1 , (0,255,0) , 1)

    for cnt in img_cnt:
        M = cv2.moments(cnt)

        if M['m00'] != 0:

            X = int(M['m10'] / M['m00'])
            Y = int(M['m01'] / M['m00'])

            escrever(img_src, 'X - {}'.format(X) , X+10, Y-15)
            escrever(img_src, 'Y - {}'.format(Y) , X+10, Y+15)

            val = abs(min_dist_val - X)

    dist = val * precisao

    escrever(img_src, 'Distancia: {:.2f} metros'.format(dist), 50, 50)
    cv2.imshow('imagem', img_src)

    key = cv2.waitKey(1) 
    if key == 27:
        break
    
cv2.destroyAllWindows()
