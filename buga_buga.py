from func import lotear_capturar,pescar
from time import sleep


def bot_start():
    """
    Informações necessárias que o usuário precisa informar para manter o bot funcionando corretamente!
    Oque são cada uma?
        agua = posição x e y onde o bot deve atirar a isca da vara de pesca, exemplo: agua = (245,523)
        vara = posição x e y onde o bot deve clicar para ativar a vara de pesca, exemplo: vara = (245,523)
        lista_batalha = posição x e y onde o bot deve aclicar para marcar o pokemon pescado para a batalha, exemplo: lista_batalha = (245,523)
        regiao_peixe = um pouco mais complexo, pois é composto pela posição x e y e a largura e altura, 
        em resumo é uma area retangular onde o bot deve fiscalizar para checar se o peixe deve ou não ser puxado, exemplo: regiao_peixe = (245,523,215,245)

    """
    agua = (671,591)
    vara = (1221,100)
    lista_batalha = (1237,312)
    regiao_peixe = (1129,193,35,42)

    """
    Relembrando!
        tentativa = Corresponde a quantas tentativas o bot deve fazer para garantir que ira lootear e tacar pokebola no alvo
        local_1 = Corresponde as posições x e y onde o bot ira fazer sua primeira tentativa de lotear e tacar pokebola
        local_2 = Corresponde as posições x e y onde o bot ira fazer sua segunda tentativa de lotear e tacar pokebola
        local_3 = Corresponde as posições x e y onde o bot ira fazer sua terceira tentativa de lotear e tacar pokebola
    """
    tentativa = 1

    local_1 = (682,426)
    local_2 = (736,424)
    local_3 = (627,427)

    sleep(8)

    # tentando pescar
    """
    Passo a passo para realizar uma pesca:
        1 - localizar a agua
        2 - clicar na vara de pesca
        3 - clicar na agua
        4 - vigiar o icone do peixe
        5 - se peixe ficar verde:
            pescar
            ir na lista de batalha
            clicar no peixe
            usar de f1 a f10
            chamar a função de lotear a capturar
            voltar ao passo 2
        6 - se peixe ficar escuro:
            aguardar ficar verde

    """


    # Pescando -> Loteando e tacando boll -> reiniciando o ciclo

    pescar(agua=agua,vara=vara,lista_batalha=lista_batalha,regiao_peixe=regiao_peixe)

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
        
    tentativa = 1

