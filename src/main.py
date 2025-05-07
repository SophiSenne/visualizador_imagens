import FreeSimpleGUI as sg
import cv2
import matplotlib.pyplot as plt
import io
import numpy as np
from PIL import Image

from filtros.filtro_bordas import aplicar_filtro_bordas
from filtros.filtro_blur import aplicar_filtro_blur
from filtros.filtro_cinza import aplicar_filtro_cinza
from filtros.filtro_contraste import aplicar_filtro_contraste
from filtros.filtro_inversao import aplicar_filtro_inversao
from filtros.filtro_nitidez import aplicar_filtro_nitidez
from filtros.filtro_desfoque import aplicar_filtro_desfoque

image_path = ""

def convert_to_bytes(img):
    if len(img.shape) == 2:  # grayscale
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    elif img.shape[2] == 4:  # remove alpha channel if present
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    with io.BytesIO() as output:
        img.save(output, format="PNG")
        return output.getvalue()

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Escolha uma imagem de seu computador para aplicar filtros')],
            [sg.Button('Selecionar')],
            [sg.Text(f'Imagem selecionada: {image_path}', key='-IMAGE_PATH-')],
            [sg.Text('Selecione os filtros a serem aplicados')],
            [sg.Checkbox('Escala de cinza', key='Cinza')], 
            [sg.Checkbox('Inversão de Cores', key='Inversao')],
            [sg.Checkbox('Aumento de contraste', key='Contraste')],
            [sg.Checkbox('Desfoque', key='Desfoque')],
            [sg.Checkbox('Nitidez', key='Nitidez')],
            [sg.Checkbox('Detecção de bordas', key='Bordas')],
            [sg.Button('Aplicar Filtros')], 
            [sg.Image(key='-IMAGEM_ORIGINAL-'), sg.Image(key='-IMAGE-')],
            [sg.Button('Fechar')] 
        ]

window = sg.Window('Visualizador de Imagens', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Fechar':
        break
    if event == 'Selecionar':
        message = "Selecione a imagem"
        image_path = sg.popup_get_file(
            message,
            title='Selecionar Imagem',
            file_types=[("Imagens", "*.png;*.jpg;*.jpeg")],
            modal=True,
            history=True
        )
        if image_path:
            window['-IMAGE_PATH-'].update(f'Imagem selecionada: {image_path}')
            image = cv2.imread(image_path)

    if event == 'Aplicar Filtros':
        image_filter = image
        print("Filtros selecionados:")
        if values['Cinza']:
            print("Escala Cinza")
            image_filter = aplicar_filtro_cinza(image_filter)
        if values['Inversao']:
            print("Inversao")
            image_filter = aplicar_filtro_inversao(image_filter)
        if values['Contraste']:
            print("Contraste")
            image_filter = aplicar_filtro_contraste(image_filter)
        if values['Desfoque']:
            print("Desfoque")
            image_filter = aplicar_filtro_desfoque(image_filter)
        if values['Nitidez']:
            print("Nitidez")
            image_filter = aplicar_filtro_nitidez(image_filter)
        if values['Bordas']:
            print("Bordas")
            image_filter = aplicar_filtro_bordas(image_filter)

        window['-IMAGEM_ORIGINAL-'].update(data=convert_to_bytes(image))
        window['-IMAGE-'].update(data=convert_to_bytes(image_filter))
        
window.close()







