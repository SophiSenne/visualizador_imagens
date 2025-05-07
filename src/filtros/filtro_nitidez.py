import cv2

def aplicar_filtro_nitidez(imagem):
    imagem_blurred = cv2.GaussianBlur(imagem, (5,5), 1.0)
    imagem_nitidez = cv2.addWeighted(imagem, 1.0 + 1.5, imagem_blurred, -1.5, 0)
    return imagem_nitidez