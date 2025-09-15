



imagem_original = cv2.imread(arquivo_entrada)

imagem_filtrada_1 = cv2.medianBlur(imagem_original, 3)
arquivo_saida_1 = "resultado_1.tif"
cv2.imwrite(arquivo_saida_1, imagem_filtrada_1)
print(f"Primeira imagem filtrada salva como: {arquivo_saida_1}")
# --- Segunda aplicação do filtro de mediana ---
# Aplicamos o filtro na imagem que já foi filtrada uma vez
imagem_filtrada_2 = cv2.medianBlur(imagem_filtrada_1, 3)
arquivo_saida_2 = "resultado_2.tif"
cv2.imwrite(arquivo_saida_2, imagem_filtrada_2)
print(f"Segunda imagem filtrada salva como: {arquivo_saida_2}")
# --- Terceira aplicação do filtro de mediana ---
# Aplicamos o filtro na imagem que já foi filtrada duas vezes
imagem_filtrada_3 = cv2.medianBlur(imagem_filtrada_2, 3)
arquivo_saida_3 = "resultado_3.tif"
cv2.imwrite(arquivo_saida_3, imagem_filtrada_3)
print(f"Terceira imagem filtrada salva como: {arquivo_saida_3}")
print("\nProcesso concluído com sucesso!")
