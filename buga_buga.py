import pyautogui as gui
from loot_cadaver import lotear_capturar
from time import sleep

tentativa = 1

local_1 = (682,426)
local_2 = (736,424)
local_3 = (627,427)

while tentativa < 4:

    if tentativa == 1:
        lotear_capturar(local_1[0], local_1[1])
        sleep(0.25)
        #print(f'tentativa numero {tentativa} realizada com sucesso')
        tentativa += 1

    if tentativa == 2:
        lotear_capturar(local_2[0], local_2[1])
        sleep(0.25)
       # print(f'tentativa numero {tentativa} realizada com sucesso')
        tentativa += 1

    if tentativa == 3:
        lotear_capturar(local_3[0], local_3[1])
        sleep(0.25)
       # print(f'tentativa numero {tentativa} realizada com sucesso')
        tentativa += 1

