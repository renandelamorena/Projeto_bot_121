import pyautogui as pag
import time

from func.geral import pause
from func import verifica_tela

pag.alert(text='Monitoração geral de atividades aberta nas atividades liberadas da movimentação de recebimento (Código 2)', title='REQUISITOS', button='OK')

pause(0.8)

verificacao_ativida = True
while verificacao_ativida == True:

    # Click em icone da monitoração geral de atividade
    verifica_tela.click_imagem('img\monitotacao_geral\icone_movimentacao_geral.png', 'icone_movimentacao_geral')

    # Verifica se tem atividade de movimentação de recebimento
    verifica_tela.verificar_imagem_encontrada(time.time(), 20, 'img\monitotacao_geral\movimentacao_rec.png', 1, 'movimentacao_rec')

    pag.press('enter')

    # Click em finalizar atividade
    verifica_tela.click_imagem(r'img\monitotacao_geral\finalizar_atividade.png', 'finalizar_atividade')

    pag.press('enter')

    pag.press('esc')

    verifica_tela.verificar_imagem_encontrada(time.time(), 20, 'img\monitotacao_geral\movimentacao_rec.png', 1, 'movimentacao_rec')
    verificacao_ativida = verifica_tela.verificar_imagem('img\monitotacao_geral\movimentacao_rec.png')