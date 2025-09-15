import cv2

img = "circuito.tif"

imagem_original = cv2.imread(img)

imagem_filtrada_1 = cv2.medianBlur(imagem_original, 3)
arquivo_saida_1 = "1_1.png"
cv2.imwrite(arquivo_saida_1, imagem_filtrada_1)
print(f"Primeira imagem filtrada salva como: {arquivo_saida_1}")

imagem_filtrada_2 = cv2.medianBlur(imagem_filtrada_1, 3)
arquivo_saida_2 = "1_2.png"
cv2.imwrite(arquivo_saida_2, imagem_filtrada_2)
print(f"Segunda imagem filtrada salva como: {arquivo_saida_2}")

imagem_filtrada_3 = cv2.medianBlur(imagem_filtrada_2, 3)
arquivo_saida_3 = "1_3.png"
cv2.imwrite(arquivo_saida_3, imagem_filtrada_3)
print(f"Terceira imagem filtrada salva Fcomo: {arquivo_saida_3}")

print("\nProcesso concluído com sucesso!")
