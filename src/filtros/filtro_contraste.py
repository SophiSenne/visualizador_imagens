import cv2

def aplicar_filtro_contraste(imagem):
    imagem_contraste = cv2.convertScaleAbs(imagem, alpha=1.5, beta=0)
    return imagem_contraste