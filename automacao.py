import pyautogui as pag
import pyperclip as pcl
import time

from func import verifica_tela
from func.geral import caminho_absoluto as caminho

def click_imagem(caminho_, nome_img):
    verifica_tela.verificar_imagem_encontrada(time.time(), 15, caminho(caminho_), 0.5, nome_img)
    verifica_tela.click(caminho(caminho_), 1)

confirmacao_iniciamento_automacao = pag.confirm(text='Deseja iniciar a automação da atividade 121?', title='Automação 121', buttons=['OK', 'Cancel'])

if confirmacao_iniciamento_automacao == 'OK':

    selec_impressora = None
    while selec_impressora == None:
        selec_impressora = pag.confirm(text='Qual impressora você deseja enviar as etiquetas?', title='Selecione a impressora', buttons=['Estoque', 'Pallet'])

    if selec_impressora == 'Pallet':
        caminho_impressora = 'img/atividade_20/pallet_pallet.png'

        nome_impressora = 'PALLET'

    elif selec_impressora == 'Estoque':
        caminho_impressora = 'img/atividade_20/pallet_pallet.png'
        nome_impressora = 'ESTOQUE1'

    # pag.alert(text='Se necessario encerrar a automação, mova o mouse para o canto da tela.', title='ATENÇÃO!', button='OK')
    pag.alert(text='1. Atividade 121 aberta no Chrome\n2. Impressão de etiquetas aberta em endereço', title='REQUISITOS', button='OK')

    # 1 Ir ao navegador
    click_imagem('img/geral/icone_chrome.png', 'icone_chrome')

    enderecos = []

    aceitar = True
    while aceitar == True:

        # 2 Aceitar atividade
            # Click em 'Aceitar'
        click_imagem('img/atividade_121/aceitar.png', 'aceitar - aceitar atividade')

        # 3 Guardar informação da UMA
            # Click triplo em 'UMA: 0'
        verifica_tela.verificar_imagem_encontrada(time.time(), 10, 'img/atividade_121/uma.png', 0.5, 'campo uma')
        time.sleep(0.5)
        click_imagem('img/atividade_121/uma.png', 'uma - onde fica a UMA da atividade')
        verifica_tela.click('img/atividade_121/uma.png', 2)

            # Copiar informação da uma e guardar
            # Copiar a informação 'UMA: 000000000000168250'
        time.sleep(0.5)
        pag.hotkey('ctrl', 'c')

            # tratar a informação do endereço 'UMA: 000000000000168250\r\n' para '000000000000168250' e guardar em uma variavel
        uma_copiada = pcl.paste()

        # 4 Tratar informação da uma para confirmar () e guardar
            # Tratar informação da uma e guardar
        uma_tratada = ''.join(filter(str.isdigit, uma_copiada))

        # 5 Confirmar UMA
            # Click campo de uma
        click_imagem('img/atividade_121/campo_uma.png', 'campo_uma - onde fica o local para colocar UMA na atividade')

            # Colar UMA tratada
        pcl.copy(uma_tratada)
        pag.hotkey('ctrl', 'v')

            # Click em prosseguir
        click_imagem('img/atividade_121/prosseguir.png', 'prosseguir - onde fica o botão para prosseguir da uma')

        # 6 Guardar informação do endereço
            # Click triplo em endereço
        verifica_tela.verificar_imagem_encontrada(time.time(), 10, 'img/atividade_121/end_destino.png', 0.5, 'campo end_destino')
        time.sleep(0.5)
        click_imagem('img/atividade_121/end_destino.png', 'end_destino - onde fica o end_destino da atividade')
        verifica_tela.click('img/atividade_121/end_destino.png', 2)

            # Copiar informação do endereço e guardar
        time.sleep(0.5)
        pag.hotkey('ctrl', 'c')
        endereco_copiado = pcl.paste()

        # 7 Tratar informação do endereço para confirmar e imprimir (015-015-01-01 -> 010150150101) e guardar
            # tratar a informação do end 'End. Origem: 017-003-04-02\r\n' para '010170030402' e guardar em uma variavel
        endereco_tratado = '01' + ''.join(filter(str.isdigit, endereco_copiado))
        enderecos.append(endereco_tratado)

        # 8 Confirmar endereço
            # Click campo de endereço de destino
        click_imagem('img/atividade_121/campo_end_destino.png', 'campo_end_destino - onde fica o campo_end_destino da atividade')

            # Colar endereço tratado
        pcl.copy(endereco_tratado)
        pag.hotkey('ctrl', 'v')

            # Click em confirmar
        click_imagem('img/atividade_121/confirmar.png', 'confirmar - onde fica o botão de confirmar da atividade')

        # 10 confirmar
            # Click em confirmar confirmação
        click_imagem('img/atividade_121/confirmar_confirmacao.png', 'confirmar_confirmacao - onde fica o botão de confirmar a confirmação da atividade')

        # 13 voltar para atividade
        # click_imagem('img/geral/icone_chrome.png', 'icone_chrome')

        verifica_tela.verificar_imagem_encontrada(time.time(), 10, 'img/atividade_121/aceitar.png', 0.5, 'campo uma')

        time.sleep(1)

        aceitar = verifica_tela.verificar_imagem(caminho('img/atividade_121/aceitar.png'))

    enderecos.reverse()

    # 10 Ir para impressão de etiquetas
    click_imagem('img/geral/icone_impressao_etiqueta.png', 'icone_impressao_etiqueta')

    for endereco in enderecos:

        # 12 Imprimir etiquetas
            # Colar informação de endereço tratada
        pcl.copy(endereco)
        pag.hotkey('ctrl', 'v')

            # Click em 'Imprimir'
        click_imagem('img/impressao_etiqueta/imprimir.png', 'imprimir - botão para imprimir')

            # selecionar nome da impressora
        pag.press('right', presses=20)
        pag.press('backspace', presses=20)

            # Colar nome da impressora
        pcl.copy(nome_impressora)
        pag.hotkey('ctrl', 'v')

            # Click em 'Imprimir'
        pag.press('tab')
        pag.press('enter')