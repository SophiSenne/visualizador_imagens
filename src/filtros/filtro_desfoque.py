import cv2

def aplicar_filtro_desfoque(imagem):
    imagem_blur = cv2.blur(imagem, ksize=(3,3))
    return imagem_blur