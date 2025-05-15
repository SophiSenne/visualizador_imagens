import cv2

def aplicar_filtro_bordas(imagem):
    if (len(imagem.shape) > 2):
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_gaussiana = cv2.GaussianBlur(imagem, (5, 5), 0)
    imagem_canny = cv2.Canny(imagem_gaussiana, 100, 200)
    return imagem_canny

