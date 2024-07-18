import pyperclip as pcl
import time
import pyautogui as pag

import pandas as pd

from func import verifica_tela
from func.geral import caminho_absoluto as caminho

def click_imagem(caminho_, nome_img):
    verifica_tela.verificar_imagem_encontrada(time.time(), 15, (caminho_), 0.5, nome_img)
    verifica_tela.click((caminho_), 1)

confirmacao_iniciamento_impressao = pag.confirm(text='Deseja iniciar a impressão de etiquetas?', title='Autumação - imprimir etiquetas', buttons=['OK', 'Cancel'])

pag.alert(text='Excel "atividade 4 - armagenagem receb" atualizado', title='REQUISITOS', button='OK')

if confirmacao_iniciamento_impressao == 'OK':

    selec_impressora = None
    while selec_impressora == None:
        selec_impressora = pag.confirm(text='Qual impressora você deseja enviar as etiquetas?', title='Selecione a impressora', buttons=['Estoque', 'Pallet'])

        if selec_impressora == 'Pallet':
            caminho_impressora = 'img/atividade_20/pallet_pallet.png'
            nome_impressora = 'PALLET'

        elif selec_impressora == 'Estoque':
            caminho_impressora = 'img/atividade_20/pallet_pallet.png'
            nome_impressora = 'ESTOQUE1'

    uma_inicial = int(pag.prompt(title='Selecionar UMA Inicial', text='Digite os numeros da UMA inicial:',  default=''))
    uma_final = int(pag.prompt(title='Selecionar UMA Final', text='Digite os numeros da UMA final:', default=''))

    # Atividade 4
    atividades = pd.read_excel('atividade 4 - armagenagem receb.xlsx')

    selecao_sequencia_de_uma = (
        (atividades['UMA Orig.'] >= uma_inicial) & \
        (atividades['UMA Orig.'] <= uma_final)
    )

    sequencia_de_uma = atividades[selecao_sequencia_de_uma]

    enderecos = sequencia_de_uma['Ender.Destino'].to_list()

    # Revertendo a ordem da lista
    enderecos.reverse()

    # ---

    # 10 Ir para impressão de etiquetas
    click_imagem('img/geral/icone_impressao_etiqueta.png', 'icone_impressao_etiqueta')

    for endereco in enderecos:

        # Remover os traços
        string_sem_tracos = endereco.replace('-', '')
        # Adicionar '01' na frente
        resultado_final = '01' + string_sem_tracos

        # 12 Imprimir etiquetas
            # Colar informação de endereço tratada
        pcl.copy(resultado_final)
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