import FreeSimpleGUI as sg
import cv2
import matplotlib.pyplot as plt
from filtros.filtro_bordas import aplicar_filtro_bordas

image_path = ""

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
            [sg.Image(key='-IMAGEM_ORIGINAL-')],
            [sg.Image(key='-IMAGE-')],
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
        print("Filtros selecionados:")
        if values['Cinza']:
            print("Escala Cinza")
        if values['Inversao']:
            print("Inversao")
        if values['Contraste']:
            print("Contraste")
        if values['Desfoque']:
            print("Desfoque")
        if values['Nitidez']:
            print("Nitidez")
        if values['Bordas']:
            print("Bordas")
            image = aplicar_filtro_bordas(image)

        plt.subplot(1, 2, 1)
        plt.imshow(image, cmap='gray')
        plt.title('Imagem Original')
        plt.axis('off')
        plt.subplot(1, 2, 2)
        plt.imshow(image, cmap='gray')
        plt.title('Imagem Filtrada')
        plt.axis('off')
        plt.show()
        
window.close()



