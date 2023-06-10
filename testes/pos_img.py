from pyautogui import locateOnScreen

def localiza_img_tela(path):
    import time
    from PIL import Image

    # Carrega a imagem
    imagem = Image.open(path)

    # Obtém as dimensões da imagem
    largura, altura = imagem.size

    # Encontra a posição da imagem na tela
    posicao = None
    while posicao is None:
        posicao = locateOnScreen(path)
        time.sleep(1)

    # Obtém as coordenadas x e y do canto superior esquerdo da imagem
    x, y = posicao.left, posicao.top

    # Exibe as dimensões e a posição da imagem na tela
    return x,y,largura,altura