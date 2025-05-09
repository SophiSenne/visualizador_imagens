import FreeSimpleGUI as sg

layout = [  [sg.Text('Escolha uma imagem de seu computador')],
            [sg.Button('Selecionar')],
            [sg.Text('Rotação da imagem:')], 
            [sg.Radio('0°', "Rotacao", default=True, key='-0-'), 
             sg.Radio('90°', "Rotacao", key='-90-'),
             sg.Radio('180°', "Rotacao", key='-180-'), 
             sg.Radio('270°', "Rotacao", key='-270-')],
            [sg.Text('Redimensionar Imagem:')],
            [sg.Text('Largura'), sg.Spin([i for i in range(50,500)], key='-Largura-'),
             sg.Text('Altura'), sg.Spin([i for i in range(50,500)], key='-Altura-')],            
            [sg.Text('Selecione os filtros a serem aplicados')],
            [sg.Checkbox('Escala de cinza', key='Cinza')], 
            [sg.Checkbox('Inversão de Cores', key='Inversao')],
            [sg.Checkbox('Aumento de contraste', key='Contraste')],
            [sg.Checkbox('Desfoque', key='Desfoque')],
            [sg.Checkbox('Nitidez', key='Nitidez')],
            [sg.Checkbox('Detecção de bordas', key='Bordas')],
            [sg.Button('Aplicar Transformações')],
            [sg.Image(key='-IMAGEM_ORIGINAL-'), sg.Image(key='-IMAGE-')],
            [sg.Button('Salvar Imagem'), sg.Button('Fechar')] 
        ]