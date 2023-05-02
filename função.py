from pyautogui import screenshot
from comparar import compara_img


def see():
    import time

    while True:

        time.sleep(1)
        im1 = screenshot()
        im1.save('see/1.png')

        time.sleep(1)
        im1 = screenshot()
        im1.save('see/2.png')

        retorno = compara_img('see/1.png','see/2.png')

        if retorno:
            pass
        else:
            break
        
    return True


