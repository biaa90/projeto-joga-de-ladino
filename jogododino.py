import os
import pyautogui as auto
CAMINHO_PASTA = os.getcwd ()
print ("caminho da pasta:",CAMINHO_PASTA)
CAMINHO_PASTA_IMAGENS = os.path.join (CAMINHO_PASTA,".\\automacao.\\img")
print ("caminho da pasta imagens:", CAMINHO_PASTA_IMAGENS)

lista_fotos = os.listdir (CAMINHO_PASTA_IMAGENS)
print ("conteudos da lista de fotos:", lista_fotos)
caminho_dino = os.path.join (CAMINHO_PASTA , ".\\automacao\\dino.png")

while True:
    for foto in lista_fotos:
        caminho_da_foto =os.path.join (CAMINHO_PASTA_IMAGENS, foto)
        
        try:
            posicao_cacto = auto.locateOnScreen (caminho_da_foto, confidence=0.7)
            posiçao_dino = auto.locateOnScreen (caminho_dino, confidence = 0.6)

        except:
            posicao_cacto = None

        else:
            print ("posicao_cacto:",posicao_cacto.left)
            if posicao_cacto.left <= 985:
                auto.press("space")
                auto.keyDown("space")
        
           