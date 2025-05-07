import cv2

def aplicar_filtro_bordas(imagem):
    imagem = cv2.resize(imagem, (512, 512))
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_gaussiana = cv2.GaussianBlur(imagem_cinza, (5, 5), 0)
    imagem_canny = cv2.Canny(imagem_gaussiana, 100, 200)
    _, imagem_threshold = cv2.threshold(imagem_canny, 127, 255, cv2.THRESH_BINARY)
    contornos, _ = cv2.findContours(imagem_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imagem_contornos = cv2.drawContours(imagem.copy(), contornos, -1, (0, 255, 0), 3)
    return imagem_contornos
