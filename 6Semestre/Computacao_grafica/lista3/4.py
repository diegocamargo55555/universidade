import cv2
import numpy as np
from matplotlib import pyplot as plt

def rejeita_banda(shape, r_in, r_out):
    rows, cols = shape
    center_row, center_col = rows // 2, cols // 2

    y, x = np.ogrid[-center_row:rows-center_row, -center_col:cols-center_col]
    dist_from_center = np.sqrt(x**2 + y**2)

    mask = (dist_from_center < r_in) | (dist_from_center > r_out)
    
    return mask.astype(float)




def apply_frequency_filter(image, filter_mask):
    # 1. Transformada de Fourier e centralização do espectro
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # 2. Aplicar a máscara (multiplicação elemento a elemento)
    # A máscara precisa ser de 2 canais para multiplicar a parte real e imaginária
    mask_2ch = np.stack([filter_mask, filter_mask], axis=-1)
    f_shift_filtered = dft_shift * mask_2ch
    
    # 3. Desfazer a centralização
    f_ishift = np.fft.ifftshift(f_shift_filtered)
    
    # 4. Transformada Inversa de Fourier para voltar ao domínio espacial
    img_back = cv2.idft(f_ishift)
    
    # 5. Obter a magnitude e normalizar para visualização
    img_filtered = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    cv2.normalize(img_filtered, img_filtered, 0, 255, cv2.NORM_MINMAX)
    
    return img_filtered.astype(np.uint8)


image_files = ["img_aluno.png", "teste.tif"]
cv2.imread(image_files[0], cv2.IMREAD_GRAYSCALE)


    # Parâmetros dos filtros (EXPERIMENTE MUDAR ESSES VALORES!)
    # Raio interno e externo do anel
inner_radius = 40
outer_radius = 80

    # Processa cada imagem da lista
for filename in image_files:
        # Carrega a imagem em escala de cinza
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

        # --- Geração e Aplicação dos Filtros ---
        
        # Filtro Rejeita-Banda
        reject_mask = rejeita_banda(img.shape, inner_radius, outer_radius)
        img_rejected = apply_frequency_filter(img, reject_mask)

        # Filtro Passa-Banda
        pass_mask = 1 - rejeita_banda(img.shape, inner_radius, outer_radius)
        img_passed = apply_frequency_filter(img, pass_mask)
        
        # --- Visualização dos Resultados ---
        plt.figure(figsize=(18, 10))
        plt.suptitle(f'Filtragem em Frequência: {filename}', fontsize=16)

        # Original
        plt.subplot(2, 3, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Imagem Original')
        plt.axis('off')

        # Filtro Rejeita-Banda
        plt.subplot(2, 3, 2)
        plt.imshow(reject_mask, cmap='gray')
        plt.title(f'Máscara Rejeita-Banda\n(r_in={inner_radius}, r_out={outer_radius})')
        plt.axis('off')

        plt.subplot(2, 3, 3)
        plt.imshow(img_rejected, cmap='gray')
        plt.title('Resultado Rejeita-Banda')
        plt.axis('off')

        # Espectro de Fourier da imagem original para referência
        dft_original = np.fft.fftshift(cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT))
        magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_original[:, :, 0], dft_original[:, :, 1]) + 1)
        plt.subplot(2, 3, 4)
        plt.imshow(magnitude_spectrum, cmap='gray')
        plt.title('Espectro de Frequência Original')
        plt.axis('off')
        
        # Filtro Passa-Banda
        plt.subplot(2, 3, 5)
        plt.imshow(pass_mask, cmap='gray')
        plt.title(f'Máscara Passa-Banda\n(r_in={inner_radius}, r_out={outer_radius})')
        plt.axis('off')

        plt.subplot(2, 3, 6)
        plt.imshow(img_passed, cmap='gray')
        plt.title('Resultado Passa-Banda')
        plt.axis('off')

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig('4.png') 

        plt.show()
