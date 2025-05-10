import FreeSimpleGUI as sg
import cv2
from filtros.filtro_bordas import aplicar_filtro_bordas
from filtros.filtro_cinza import aplicar_filtro_cinza
from filtros.filtro_contraste import aplicar_filtro_contraste
from filtros.filtro_inversao import aplicar_filtro_inversao
from filtros.filtro_nitidez import aplicar_filtro_nitidez
from filtros.filtro_desfoque import aplicar_filtro_desfoque
from transformacoes import rotate, resize
from manipular_imagem import convert_to_bytes
from layout import layout

# Definicao de variaveis
image_path = ""
image = None
image_filter = None
altura_imagem = 0
largura_imagem = 0

# Definicao do tema da interface
sg.theme('Dark Blue 3')

# Cria a janela com o layout do arquivo layout.py
window = sg.Window('Visualizador de Imagens', layout, resizable=True)

# Lógicas de funcionamento da interface
while True:
    # Leitura dos status das interacoes do usuario com o sistema
    event, values = window.read()

    # Lógica para fechar a janela
    if event == sg.WIN_CLOSED or event == 'Fechar':
        break

    # Selecao da imagem
    if event == 'Selecionar':
        message = "Selecione a imagem"
        image_path = sg.popup_get_file(
            message,
            title='Selecionar Imagem',
            file_types=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg")],
            modal=True,
            history=True
        )
        # Atualizacao da interface de acordo com a imagem escolhida
        if image_path:
            image = cv2.imread(image_path)
            altura_imagem, largura_imagem = image.shape[:2]
            window['-IMAGEM_ORIGINAL-'].update(data=convert_to_bytes(image))
            window['-Largura-'].update(value=largura_imagem)
            window['-Altura-'].update(value=altura_imagem)

    # Logicas para aplicacao das tranformacoes selecionadas pelo usuario
    if event == 'Aplicar Transformações':
        if image is None:
            sg.popup_error("Nenhuma imagem carregada! Selecione uma imagem antes de aplicar os filtros.")
            continue
        image_filter = image
        # Redimensionar
        image_filter = resize(image_filter, int(values['-Largura-']), int(values['-Altura-']))
        # Rotacionar
        if values['-90-']:
            image_filter = rotate(image_filter, cv2.ROTATE_90_CLOCKWISE)
        if values['-180-']:
            image_filter = rotate(image_filter, cv2.ROTATE_180)
        if values['-270-']:
            image_filter = rotate(image_filter, cv2.ROTATE_90_COUNTERCLOCKWISE)
        # Filtros
        if values['Cinza']:
            image_filter = aplicar_filtro_cinza(image_filter)
        if values['Inversao']:
            image_filter = aplicar_filtro_inversao(image_filter)
        if values['Contraste']:
            image_filter = aplicar_filtro_contraste(image_filter)
        if values['Desfoque']:
            image_filter = aplicar_filtro_desfoque(image_filter)
        if values['Nitidez']:
            image_filter = aplicar_filtro_nitidez(image_filter)
        if values['Bordas']:
            image_filter = aplicar_filtro_bordas(image_filter)
        # Exibe a imagem alterada
        window['-IMAGE-'].update(data=convert_to_bytes(image_filter))

    if event =='Salvar Imagem':
        if image_filter is None:
            sg.popup_error("Nenhuma imagem para salvar! Primeiro aplique alguma transformação.")
            continue
        save_path = sg.popup_get_file(
            "Salvar imagem como...",
            save_as=True,
            no_window=True,
            file_types=(("PNG Files", "*.png"), ("JPEG Files", "*.jpg")),
            default_extension=".png"
        )
        if save_path:
            cv2.imwrite(save_path, image_filter)
            sg.popup("Imagem salva com sucesso!", title="Sucesso")
        
window.close()







