import cv2

def rotate(image, rotation):
    imagem_rotacionada = cv2.rotate(image, rotation)
    return imagem_rotacionada

def resize(image, largura, altura):
    resized_image = cv2.resize(image, (largura, altura))
    return resized_image

