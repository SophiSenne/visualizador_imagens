import cv2

def aplicar_filtro_inversao(imagem):
    imagem_contraste = cv2.bitwise_not(imagem)
    return imagem_contraste