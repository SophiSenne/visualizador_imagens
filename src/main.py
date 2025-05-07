import FreeSimpleGUI as sg

image_path = ""

sg.theme('Dark Blue 3')

layout = [  [sg.Text('Escolha uma imagem de seu computador para aplicar filtros')],
            [sg.Button('Selecionar')],
            [sg.Text(f'Imagem selecionada: {image_path}', key='-IMAGE_PATH-')],
            [sg.Text('Selecione os filtros a serem aplicados')],
            [sg.Checkbox('Escala de cinza')], 
            [sg.Checkbox('Inversão de Cores')],
            [sg.Checkbox('Aumento de contraste')],
            [sg.Checkbox('Desfoque')],
            [sg.Checkbox('Nitidez')],
            [sg.Checkbox('Detecção de bordas')],
            [sg.Button('Aplicar Filtros')], 
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
        
window.close()



